"""
 OpenVINO DL Workbench
 Class for creating ORM local profiling pipeline model and dependent models

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

from sqlalchemy.orm import Session

from wb.main.enumerates import PipelineTypeEnum, PipelineStageEnum, TestInferVisualizationTypesEnum
from wb.main.models.inference_test_image_job_model import InferenceTestImageJobModel
from wb.main.models.pipeline_model import PipelineModel
from wb.main.pipeline_creators.pipeline_creator import PipelineCreator


class InferenceTestImagePipelineCreator(PipelineCreator):
    pipeline_type = PipelineTypeEnum.inference_test_image

    _job_type_to_stage_map = {
        InferenceTestImageJobModel.get_polymorphic_job_type(): PipelineStageEnum.inference_test_image,
    }

    def __init__(self, target_id: int, topology_id: int, device_id: int, test_image_id: int,
                 visualization_type: TestInferVisualizationTypesEnum):
        super().__init__(target_id)
        self.topology_id = topology_id
        self.device_id = device_id
        self.test_image_id = test_image_id
        self.visualization_type = visualization_type

    def _create_pipeline_jobs(self, pipeline: PipelineModel, session: Session):
        inference_job = InferenceTestImageJobModel(
            {'topologyId': self.topology_id, 'deviceId': self.device_id, 'pipelineId': pipeline.id}
        )
        inference_job.test_image_id = self.test_image_id
        inference_job.visualization_type = self.visualization_type
        self._save_job_with_stage(inference_job, session)
