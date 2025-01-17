"""
 OpenVINO DL Workbench
 Class for handling layers from IR

 Copyright (c) 2018 Intel Corporation

 LEGAL NOTICE: Your use of this software and any required dependent software (the “Software Package”) is subject to
 the terms and conditions of the software license agreements for Software Package, which may also include
 notices, disclaimers, or license terms for third party or open source software
 included in or with the Software Package, and your use indicates your acceptance of all such terms.
 Please refer to the “third-party-programs.txt” or other similarly-named text file included with the Software Package
 for additional details.
 You may obtain a copy of the License at
      https://software.intel.com/content/dam/develop/external/us/en/documents/intel-openvino-license-agreements.pdf
"""
from defusedxml import ElementTree

from wb.utils.per_layer_report.layer import Layer
from wb.utils.per_layer_report.utils import SPATIAL_PARAMS_NAMES, cast_value, cast_to_number


class OriginalLayer(Layer):
    def __init__(self, xml_layer: ElementTree):
        super().__init__(xml_layer)
        self.positional_data = self.positional_data_from_xml(xml_layer)
        self.params = self.spatial_and_specific_params(xml_layer)
        self.blob_data = self.get_blob_data(xml_layer)

    def json(self):
        return {
            **super().json(),
            'positionalData': self.positional_data,
            **self.params,
            'blobData': self.blob_data,
        }

    @staticmethod
    def spatial_and_specific_params(xml_layer: ElementTree) -> dict:
        result = {}

        params = OriginalLayer.data_params_from_xml(xml_layer)

        specific_params = {}
        for param, value in params.items():
            if OriginalLayer.if_spatial_param(param):
                continue
            specific_params[param] = cast_to_number(value)

        result['specificParams'] = specific_params

        spatial_params = OriginalLayer.parse_spatial_params(params)
        result['spatialParams'] = spatial_params

        return result

    @staticmethod
    def parse_spatial_params(params: dict) -> dict:
        processed_params = {}
        for param, value in params.items():
            if not OriginalLayer.if_spatial_param(param):
                continue
            processed_params[param] = cast_value(value)
        return processed_params

    @staticmethod
    def if_spatial_param(param_name: str) -> bool:
        param_name = param_name.replace('_', '-')
        if param_name in SPATIAL_PARAMS_NAMES:
            return True
        return False

    @staticmethod
    def get_blob_data(xml_layer: ElementTree) -> dict:
        result = {}
        blobs = xml_layer.find('blobs')
        if blobs is None:
            return {
                'attribs.weights.offset': 'Not available',
                'attribs.weights.size': 'Not available',
                'attribs.biases.offset': 'Not available',
                'attribs.biases.size': 'Not available'
            }
        for blob in blobs.iter():
            if blob is blobs:
                continue
            for attribute, value in blob.attrib.items():
                result['attribs.{}.{}'.format(blob.tag, attribute)] = int(value)
        return result
