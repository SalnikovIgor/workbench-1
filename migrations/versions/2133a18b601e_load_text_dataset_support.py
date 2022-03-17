"""Load text dataset support

Revision ID: 2133a18b601e
Revises: dd938f7a0c63
Create Date: 2021-11-11 10:59:53.415935

"""

"""
 OpenVINO DL Workbench
 Migration: Load text dataset support

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
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from migrations.utils import SQLEnumMigrator

# revision identifiers, used by Alembic.
revision = '2133a18b601e'
down_revision = 'dd938f7a0c63'
branch_labels = None
depends_on = None

old_dataset_types = (
    'imagenet',
    'voc',
    'coco',
    'common_semantic_segmentation',
    'common_super_resolution',
    'lfw',
    'vggface2',
    'wider_face',
    'open_images',
    'not_annotated',
)

new_dataset_types = (
    *old_dataset_types,
    'csv'
)

dataset_type_migrator = SQLEnumMigrator(
    (('datasets', 'dataset_type'),),
    'datasettypesenum',
    old_dataset_types,
    new_dataset_types
)

old_task_enums = (
    'classification',
    'object_detection',
    'instance_segmentation',
    'semantic_segmentation',
    'inpainting',
    'style_transfer',
    'super_resolution',
    'face_recognition',
    'landmark_detection',
    'generic',
    'custom'
)

new_task_enums = (
    *old_task_enums,
    'text_classification',
    'textual_entailment'
)

task_enum_migrator = SQLEnumMigrator(
    table_column_pairs=(
        ('dataset_tasks', 'task_type'), ('omz_topologies', 'task_type'), ('topologies_metadata', 'task_type')
    ),
    enum_name='taskenum',
    from_types=old_task_enums,
    to_types=new_task_enums
)

old_pipeline_stages = (
    'accuracy',
    'preparing_setup_assets',
    'uploading_setup_assets',
    'configuring_environment',
    'collecting_available_devices',
    'collecting_system_information',
    'preparing_profiling_assets',
    'preparing_int8_calibration_assets',
    'preparing_accuracy_assets',
    'profiling',
    'getting_remote_job_result',
    'download_log',
    'int8_calibration',
    'remote_int8_calibration',
    'augment_dataset',
    'extract_dataset',
    'generate_dataset',
    'recognize_dataset',
    'validate_dataset',
    'wait_dataset_upload',
    'export_project_report',
    'export_inference_report',
    'wait_model_upload',
    'model_analyzer',
    'model_optimizer_scan',
    'convert_keras_model',
    'convert_model',
    'setup_environment',
    'download_omz_model',
    'convert_omz_model',
    'move_omz_model',
    'inference_test_image',
    'export_project',
    'winograd_tuning',
)

new_pipeline_stages = (
    *old_pipeline_stages,
    'extract_text_dataset',
    'validate_text_dataset',
)

pipeline_stage_enum_migrator = SQLEnumMigrator(
    table_column_pairs=(('job_execution_details', 'stage'),),
    enum_name='pipelinestageenum',
    from_types=old_pipeline_stages,
    to_types=new_pipeline_stages
)

csv_dataset_separators = (
    'tab',
    'comma',
    'semicolon',
    'colon',
    'pipe',
)

csv_dataset_separator_enum = postgresql.ENUM(*csv_dataset_separators, name='csvdatasetseparatorenum', create_type=True)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pipeline_stage_enum_migrator.upgrade()
    dataset_type_migrator.upgrade()
    task_enum_migrator.upgrade()

    op.create_table('extract_text_dataset_jobs',
                    sa.Column('job_id', sa.Integer(), nullable=False),
                    sa.Column('columns', sa.ARRAY(sa.Integer()), nullable=False),
                    sa.Column('header', sa.Boolean(), nullable=False),
                    sa.Column('encoding', sa.String(), nullable=False),
                    sa.Column('separator', csv_dataset_separator_enum, nullable=False),
                    sa.ForeignKeyConstraint(['job_id'], ['extract_dataset_jobs.job_id'], ),
                    sa.PrimaryKeyConstraint('job_id')
                    )
    op.create_table('validate_text_dataset_jobs',
                    sa.Column('job_id', sa.Integer(), nullable=False),
                    sa.Column('task_type', postgresql.ENUM(name='taskenum', create_type=False), nullable=False),
                    sa.ForeignKeyConstraint(['job_id'], ['validate_dataset_jobs.job_id'], ),
                    sa.PrimaryKeyConstraint('job_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('validate_text_dataset_jobs')
    op.drop_table('extract_text_dataset_jobs')

    task_enum_migrator.downgrade()
    dataset_type_migrator.downgrade()
    pipeline_stage_enum_migrator.downgrade()
    # ### end Alembic commands ###