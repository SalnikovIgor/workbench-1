"""
 OpenVINO DL Workbench
 Error classes for DevCloud related jobs

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
from requests import Response

from wb.error.general_error import GeneralError
from wb.error.code_registry import CodeRegistry


class DevCloudGeneralError(GeneralError):
    code = CodeRegistry.get_dev_cloud_general_error_code()


class DevCloudNotRunningError(DevCloudGeneralError):
    code = CodeRegistry.get_dev_cloud_not_running_error_code()


class DevCloudHTTPError(DevCloudGeneralError):
    response: Response

    def __init__(self, message: str, response: Response):
        super().__init__(message)
        self.response = response


class DevCloudHandshakeHTTPError(DevCloudHTTPError):
    code = CodeRegistry.get_dev_cloud_handshake_error_code()


class DevCloudDevicesHTTPError(DevCloudHTTPError):
    code = CodeRegistry.get_dev_cloud_devices_error_code()


class DevCloudRemoteJobHTTPError(DevCloudHTTPError):
    code = CodeRegistry.get_dev_cloud_remote_job_error_code()


class DevCloudSocketError(DevCloudGeneralError):
    code = CodeRegistry.get_dev_cloud_remote_job_error_code()