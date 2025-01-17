"""Remove Dataset Generation

Revision ID: 53845388c5b8
Revises: 9dd49b6b0552
Create Date: 2021-04-30 15:47:51.608819

"""

"""
 OpenVINO DL Workbench
 Migration: Remove dataset generation support

 Copyright (c) 2021 Intel Corporation

 LEGAL NOTICE: Your use of this software and any required dependent software (the “Software Package”) is subject to
 the terms and conditions of the software license agreements for Software Package, which may also include
 notices, disclaimers, or license terms for third party or open source software
 included in or with the Software Package, and your use indicates your acceptance of all such terms.
 Please refer to the “third-party-programs.txt” or other similarly-named text file included with the Software Package
 for additional details.
 You may obtain a copy of the License at
      https://software.intel.com/content/dam/develop/external/us/en/documents/intel-openvino-license-agreements.pdf
"""

from alembic import op
from sqlalchemy.ext.declarative import declarative_base

from migrations.utils import SQLEnumMigrator

# revision identifiers, used by Alembic.
revision = '53845388c5b8'
down_revision = '9dd49b6b0552'
branch_labels = None
depends_on = None

new_pipeline_types = (
    'accuracy',
    'remote_profiling',
    'local_profiling',
    'dev_cloud_profiling',
    'local_int8_calibration',
    'remote_int8_calibration',
    'dev_cloud_int8_calibration',
    'create_profiling_bundle',
    'download_log',
    'download_model',
    'deployment_manager',
    'setup',
    'ping',
    'inference_test_image',
    'generate_dataset',
    'upload_dataset',
    'export_project_report',
    'export_inference_report',
    'local_winograd_tuning',
    'export_project',
    'upload_model',
    'download_omz_model'
)

old_pipeline_types = (
    *new_pipeline_types,
    'generate_dataset',
)

new_pipeline_stages = (
    'accuracy',
    'preparing_setup_assets',
    'uploading_setup_assets',
    'configuring_environment',
    'collecting_available_devices',
    'collecting_system_information',
    'preparing_profiling_assets',
    'preparing_int8_calibration_assets',
    'profiling',
    'getting_remote_job_result',
    'download_log',
    'int8_calibration',
    'remote_int8_calibration',
    'model_analyzer',
    'wait_dataset_upload',
    'extract_dataset',
    'recognize_dataset',
    'validate_dataset',
    'export_project_report',
    'export_inference_report',
    'inference_test_image',
    'winograd_tuning',
    'export_project',
    'model_optimizer_scan',
    'convert_model',
    'convert_keras_model',
    'wait_model_upload',
    'download_omz_model',
    'convert_omz_model',
    'move_omz_model',
    'augment_dataset'
)

old_pipeline_stages = (
    *new_pipeline_stages,
    'generate_dataset',
)

pipeline_type_migrator = SQLEnumMigrator(
    table_column_pairs=(('pipelines', 'type'),),
    enum_name='pipelinetypeenum',
    from_types=old_pipeline_types,
    to_types=new_pipeline_types)
pipeline_stage_migrator = SQLEnumMigrator(
    table_column_pairs=(('job_execution_details', 'stage'),),
    enum_name='pipelinestageenum',
    from_types=old_pipeline_stages,
    to_types=new_pipeline_stages)

Base = declarative_base()


def upgrade():
    op.execute("UPDATE artifacts SET status = 'archived' FROM dataset_generation_job j WHERE j.result_dataset_id = id;")
    op.execute("DELETE FROM job_execution_details WHERE job_id IN (SELECT job_id FROM dataset_generation_job);")
    op.execute("DELETE FROM dataset_generation_job;")

    # migrate enums
    pipeline_type_migrator.upgrade()
    pipeline_stage_migrator.upgrade()

    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dataset_generation_job')
    ### end Alembic commands ###


def downgrade():
    raise NotImplementedError('downgrade is not supported')
