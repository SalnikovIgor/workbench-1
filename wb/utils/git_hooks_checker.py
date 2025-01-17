"""
 OpenVINO DL Workbench
 Class for checking installed git hooks

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
import enum
import os
import re


class GitHookTypesEnum(enum.Enum):
    pre_commit = 'pre_commit'
    pre_push = 'pre_push'


class GitHooksDependencyNotInstalledException(Exception):
    pass


class GitHooksFilesNotFoundException(Exception):
    pass


class GitHooksInvalidFilesHeadersException(Exception):
    pass


class GitHookChecker:
    _wb_root_path: str

    _git_hook_file_names = {
        GitHookTypesEnum.pre_commit: 'pre-commit',
        GitHookTypesEnum.pre_push: 'pre-push',
    }

    _file_header_pattern = r'^(# File generated by pre-commit:.+)'

    def __init__(self, wb_root_path: str):
        self._wb_root_path = wb_root_path

    @staticmethod
    def _log_installation_commands() -> None:
        print('From workbench repository root run the following command:')
        print('pre-commit install && pre-commit install --hook-type pre-push')

    @property
    def _git_hooks_path(self) -> str:
        return os.path.join(self._wb_root_path, '.git', 'hooks')

    def _get_hook_file_path(self, git_hook_type: GitHookTypesEnum) -> str:
        return os.path.join(self._git_hooks_path, self._git_hook_file_names[git_hook_type])

    def _is_git_hook_file_exist(self, git_hook_type: GitHookTypesEnum) -> bool:
        git_hook_file_path = self._get_hook_file_path(git_hook_type)
        return os.path.isfile(git_hook_file_path)

    def _check_files_existence(self) -> None:
        if not all(self._is_git_hook_file_exist(hook_type) for hook_type in GitHookTypesEnum):
            print('Git hook files do not exist in local repository, you need to activate them.')
            self._log_installation_commands()
            raise GitHooksFilesNotFoundException

    def _does_git_hook_file_header_match(self, git_hook_type: GitHookTypesEnum) -> bool:
        git_hook_file_path = self._get_hook_file_path(git_hook_type)
        with open(git_hook_file_path, 'r') as hook_file:
            for line in hook_file.readlines():
                if re.search(self._file_header_pattern, line):
                    return True
        return False

    def _check_files_headers(self) -> None:
        if not all(self._does_git_hook_file_header_match(hook_type) for hook_type in GitHookTypesEnum):
            print('Looks like you have your own Git hooks installed. You need to activate DL Workbench specific hooks.')
            self._log_installation_commands()
            raise GitHooksInvalidFilesHeadersException

    def check(self) -> None:
        try:
            # pylint: disable=unused-import
            import pre_commit
            self._check_files_existence()
            self._check_files_headers()
        except ImportError:
            print('`pre-commit` development dependency is not installed')
            print('Run from repository root directory `python -m pip install -r requirements_dev.txt`')
            raise GitHooksDependencyNotInstalledException
