"""
 OpenVINO DL Workbench
 Class for managing of bundle for remote execution

 Copyright (c) 2020 Intel Corporation

 LEGAL NOTICE: Your use of this software and any required dependent software (the “Software Package”) is subject to
 the terms and conditions of the software license agreements for Software Package, which may also include
 notices, disclaimers, or license terms for third party or open source software
 included in or with the Software Package, and your use indicates your acceptance of all such terms.
 Please refer to the “third-party-programs.txt” or other similarly-named text file included with the Software Package
 for additional details.
 You may obtain a copy of the License at
      https://software.intel.com/content/dam/develop/external/us/en/documents/intel-openvino-license-agreements.pdf
"""
import logging as log
import os
import shutil
import stat
from typing import Callable, Tuple, Generator, Any, Dict, Union


class BundleComponent:
    def __init__(self, source_path: str, bundle_path: str, follow_symlinks: bool = True, executable: bool = False,
                 dependencies: Tuple['BundleComponent', ...] = ()):
        self.source_path = source_path
        self.bundle_path = bundle_path
        self.follow_symlinks = follow_symlinks
        self.executable = executable
        self.dependencies = dependencies


class ComponentsParams:
    def __init__(self):
        self.components: Dict[str, Dict[str, Union[bool, BundleComponent]]] = {}

    def enable_dependencies(self, dependencies: list):
        for component_name in self.components:
            if dependencies and component_name not in dependencies:
                continue
            self.components[component_name]['enabled'] = True

    def get_components(self) -> Generator[BundleComponent, Any, None]:
        return (component['component'] for _, component in self.components.items() if component['enabled'])

    @property
    def count(self) -> int:
        return len(list(self.get_components()))


class BundleCreator:
    def __init__(self, log_callback: Callable[[str, float], None]):
        self._progress = 0
        self._log_callback = log_callback

    def create(self, components: ComponentsParams,
               destination_bundle: str) -> str:
        raise NotImplementedError

    def log(self, message: str, progress_increase: float = 0):
        self._progress = min(self._progress + progress_increase, 99)
        log.debug(message)
        log.debug('full progress - %d', self._progress)
        self._log_callback(message, self._progress)

    @staticmethod
    def _extract_archive(archive_path: str, extract_dir: str):
        if not os.path.isfile(archive_path):
            raise FileNotFoundError(f'Archive not found in {archive_path}')
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir, exist_ok=True)
        shutil.unpack_archive(filename=archive_path, extract_dir=extract_dir, format='gztar')

    @staticmethod
    def _copy_to_dir(source_path: str, dst_path: str, follow_symlinks: bool = True, executable: bool = False):
        if not os.path.exists(source_path):
            raise FileNotFoundError(f'Source path not found in {source_path}')
        if os.path.isfile(source_path):
            filename = os.path.basename(source_path)
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            dst_path = os.path.join(dst_path, filename)
            shutil.copy(source_path, dst_path)
            if executable:
                BundleCreator._make_executable(dst_path)
        else:
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(source_path, dst_path, symlinks=not follow_symlinks)

    @staticmethod
    def _copy_component(component: BundleComponent, root_bundle_path: str):
        source = component.source_path
        for dep_component in component.dependencies:
            BundleCreator._copy_component(dep_component, root_bundle_path)
        destination = os.path.join(root_bundle_path, component.bundle_path)
        BundleCreator._copy_to_dir(source, destination, component.follow_symlinks,
                                   component.executable)

    @staticmethod
    def _make_executable(script_path: str):
        script_st = os.stat(script_path)
        os.chmod(script_path, script_st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
