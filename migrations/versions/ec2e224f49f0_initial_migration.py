"""Initial migration

Revision ID: ec2e224f49f0
Revises: 
Create Date: 2020-09-14 16:19:58.302706

"""

"""
 OpenVINO DL Workbench
 Migration: Initial migration

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
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec2e224f49f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artifacts',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=30), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('size', sa.Float(), nullable=True),
    sa.Column('checksum', sa.String(), nullable=True),
    sa.Column('progress', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('queued', 'running', 'ready', 'error', 'cancelled', 'archived', 'warning', name='statusenum'), nullable=False),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cpu_info',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('platform_type', sa.Enum('celeron', 'atom', 'core', 'xeon', name='cpuplatformtypeenum'), nullable=True),
    sa.Column('processor_family', sa.String(), nullable=True),
    sa.Column('processor_number', sa.String(), nullable=True),
    sa.Column('cores_number', sa.Integer(), nullable=True),
    sa.Column('frequency', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('omz_topologies',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('framework', sa.Enum('openvino', 'caffe', 'caffe2', 'mxnet', 'onnx', 'tf', 'pytorch', 'tf2', 'tf2_keras', name='supportedframeworksenum'), nullable=False),
    sa.Column('license_url', sa.String(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('task_type', sa.Enum('classification', 'object_detection', 'instance_segmentation', 'semantic_segmentation', 'generic', name='taskenum'), nullable=False),
    sa.Column('topology_type', sa.Enum('classificator', 'generic', 'ssd', 'tiny_yolo_v2', 'yolo_v2', 'mask_rcnn', 'segmentation', name='taskmethodenum'), nullable=False),
    sa.Column('advanced_configuration', sa.Text(), nullable=True),
    sa.Column('inputs', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proxies',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('host', sa.String(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('system_resources',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cpu_usage', sa.Float(), nullable=True),
    sa.Column('ram_total', sa.Float(), nullable=True),
    sa.Column('ram_used', sa.Float(), nullable=True),
    sa.Column('ram_available', sa.Float(), nullable=True),
    sa.Column('ram_percentage', sa.Float(), nullable=True),
    sa.Column('swap_total', sa.Float(), nullable=True),
    sa.Column('swap_used', sa.Float(), nullable=True),
    sa.Column('swap_available', sa.Float(), nullable=True),
    sa.Column('swap_percentage', sa.Float(), nullable=True),
    sa.Column('disk_total', sa.Float(), nullable=True),
    sa.Column('disk_used', sa.Float(), nullable=True),
    sa.Column('disk_available', sa.Float(), nullable=True),
    sa.Column('disk_percentage', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topologies_metadata',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('topology_type', sa.Enum('classificator', 'generic', 'ssd', 'tiny_yolo_v2', 'yolo_v2', 'mask_rcnn', 'segmentation', name='taskmethodenum'), nullable=True),
    sa.Column('task_type', sa.Enum('classification', 'object_detection', 'instance_segmentation', 'semantic_segmentation', 'generic', name='taskenum'), nullable=True),
    sa.Column('advanced_configuration', sa.Text(), nullable=True),
    sa.Column('inputs', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('login_token_hash', sa.String(), nullable=False),
    sa.Column('salt', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wb_info',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('version', sa.String(), nullable=False),
    sa.Column('dev_cloud_user', sa.String(), nullable=True),
    sa.Column('dev_cloud_file_system_prefix', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workbench_session',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ttl_seconds', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('datasets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset_type', sa.Enum('imagenet', 'voc', 'coco', 'common_semantic_segmentation', 'not_annotated', name='datasettypesenum'), nullable=True),
    sa.Column('number_images', sa.Integer(), nullable=False),
    sa.Column('labels_number', sa.Integer(), nullable=True),
    sa.Column('max_label_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['artifacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('files',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('artifact_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('size', sa.Float(), nullable=True),
    sa.Column('uploaded_blob_size', sa.Float(), nullable=True),
    sa.Column('progress', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('queued', 'running', 'ready', 'error', 'cancelled', 'archived', 'warning', name='statusenum'), nullable=False),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artifact_id'], ['artifacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_precisions',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topology_id', sa.Integer(), nullable=False),
    sa.Column('precision', sa.Enum('fp32', 'fp16', 'i8', 'i1', 'mixed', 'unknown', name='modelprecisionenum'), nullable=False),
    sa.ForeignKeyConstraint(['topology_id'], ['omz_topologies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('targets',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('target_type', sa.Enum('local', 'remote', 'dev_cloud', name='targettypeenum'), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('host', sa.String(), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('home_directory', sa.String(), nullable=True),
    sa.Column('cpu_info_id', sa.Integer(), nullable=True),
    sa.Column('system_resources_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cpu_info_id'], ['cpu_info.id'], ),
    sa.ForeignKeyConstraint(['system_resources_id'], ['system_resources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topologies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('optimized_from', sa.Integer(), nullable=True),
    sa.Column('converted_from', sa.Integer(), nullable=True),
    sa.Column('downloaded_from', sa.Integer(), nullable=True),
    sa.Column('metadata_id', sa.Integer(), nullable=False),
    sa.Column('precisions', sa.Text(), nullable=True),
    sa.Column('framework', sa.Enum('openvino', 'caffe', 'caffe2', 'mxnet', 'onnx', 'tf', 'pytorch', 'tf2', 'tf2_keras', name='supportedframeworksenum'), nullable=True),
    sa.Column('source', sa.Enum('omz', 'original', 'ir', name='modelsourceenum'), nullable=True),
    sa.ForeignKeyConstraint(['converted_from'], ['topologies.id'], ),
    sa.ForeignKeyConstraint(['downloaded_from'], ['omz_topologies.id'], ),
    sa.ForeignKeyConstraint(['id'], ['artifacts.id'], ),
    sa.ForeignKeyConstraint(['metadata_id'], ['topologies_metadata.id'], ),
    sa.ForeignKeyConstraint(['optimized_from'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_metadata',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('viewed_warning', sa.Boolean(), nullable=False),
    sa.Column('agreed_cookies', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('dataset_generation_configs',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('result_dataset_id', sa.Integer(), nullable=False),
    sa.Column('number_images', sa.Integer(), nullable=False),
    sa.Column('channels', sa.Integer(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('dist_law', sa.String(), nullable=False),
    sa.Column('dist_law_params', sa.JSON(), nullable=False),
    sa.Column('status', sa.Enum('queued', 'running', 'ready', 'error', 'cancelled', 'archived', 'warning', name='statusenum'), nullable=False),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['result_dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('result_dataset_id')
    )
    op.create_table('dataset_tasks',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('task_type', sa.Enum('classification', 'object_detection', 'instance_segmentation', 'semantic_segmentation', 'generic', name='taskenum'), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dev_cloud_targets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inactive', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('device_name', sa.String(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('optimization_capabilities', sa.Text(), nullable=False),
    sa.Column('range_infer_requests', sa.Text(), nullable=False),
    sa.Column('range_streams', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['target_id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('local_targets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pipelines',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('accuracy', 'remote_profiling', 'local_profiling', 'dev_cloud_profiling', 'local_int8_calibration', 'remote_int8_calibration', 'create_profiling_bundle', 'create_int8_calibration_bundle', 'download_log', 'download_model', 'deployment_manager', 'setup', 'ping', name='pipelinetypeenum'), nullable=False),
    sa.ForeignKeyConstraint(['target_id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('remote_targets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('private_key_path', sa.String(), nullable=True),
    sa.Column('http_proxy_id', sa.Integer(), nullable=True),
    sa.Column('https_proxy_id', sa.Integer(), nullable=True),
    sa.Column('os', sa.String(), nullable=True),
    sa.Column('has_root_privileges', sa.Boolean(), nullable=True),
    sa.Column('has_internet_connection', sa.Boolean(), nullable=True),
    sa.Column('python_version', sa.String(), nullable=True),
    sa.Column('pip_version', sa.String(), nullable=True),
    sa.Column('error', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['http_proxy_id'], ['proxies.id'], ),
    sa.ForeignKeyConstraint(['https_proxy_id'], ['proxies.id'], ),
    sa.ForeignKeyConstraint(['id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.Column('optimization_type', sa.Enum('inference', 'int8calibration', 'winograd_autotune', name='optimizationtypesenum'), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['topologies.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobs',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('job_type', sa.String(length=50), nullable=True),
    sa.Column('job_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('parent_job', sa.Integer(), nullable=True),
    sa.Column('pipeline_id', sa.Integer(), nullable=True),
    sa.Column('progress', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('queued', 'running', 'ready', 'error', 'cancelled', 'archived', 'warning', name='statusenum'), nullable=False),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['parent_job'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['pipeline_id'], ['pipelines.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('accuracy_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('accuracy', sa.Float(), nullable=True),
    sa.Column('accuracy_config', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('compound_inferences_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('inference_time', sa.Integer(), nullable=False),
    sa.Column('num_single_inferences', sa.Integer(), nullable=False),
    sa.Column('started_timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('convert_keras_to_tf',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('topology_id', sa.Integer(), nullable=False),
    sa.Column('keras_file_path', sa.String(), nullable=False),
    sa.Column('output_path', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['topology_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('download_log',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('tab_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('downloadable_artifacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artifact_type', sa.Enum('model', 'deployment_package', 'bundle_package', 'log', 'job_bundle', 'remote_job_result', name='artifacttypesenum'), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['artifacts.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('get_devices_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('get_system_resources_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('int8_calibration_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('algorithm', sa.Enum('default', 'accuracy_aware', name='quantizationalgorithmenum'), nullable=True),
    sa.Column('preset', sa.Enum('performance', 'mixed', name='quantizationalgorithmpresetenum'), nullable=True),
    sa.Column('threshold', sa.Float(), nullable=True),
    sa.Column('subset_size', sa.Integer(), nullable=False),
    sa.Column('result_model_id', sa.Integer(), nullable=True),
    sa.Column('calibration_dataset_id', sa.Integer(), nullable=False),
    sa.Column('batch', sa.Integer(), nullable=False),
    sa.Column('calibration_config', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['calibration_dataset_id'], ['datasets.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['result_model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('job_execution_details',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('stage', sa.Enum('accuracy', 'preparing_setup_assets', 'uploading_setup_assets', 'configuring_environment', 'collecting_available_devices', 'collecting_system_information', 'preparing_profiling_assets', 'preparing_int8_calibration_assets', 'profiling', 'getting_remote_job_result', 'download_log', 'int8_calibration', 'remote_int8_calibration', 'model_analyzer', name='pipelinestageenum'), nullable=True),
    sa.Column('logs', sa.Text(), nullable=True),
    sa.Column('progress', sa.Float(), nullable=True),
    sa.Column('status', sa.Enum('queued', 'running', 'ready', 'error', 'cancelled', 'archived', 'warning', name='statusenum'), nullable=True),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.Column('warning_message', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('model_download',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('precision', sa.Text(), nullable=False),
    sa.Column('result_model_id', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['result_model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('model_downloader_convert_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('result_model_id', sa.Integer(), nullable=True),
    sa.Column('conversion_args', sa.Text(), nullable=True),
    sa.Column('path', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['result_model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('model_downloads_configs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('tab_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('model_optimizer',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('original_topology_id', sa.Integer(), nullable=False),
    sa.Column('result_model_id', sa.Integer(), nullable=False),
    sa.Column('mo_args', sa.Text(), nullable=True),
    sa.Column('detailed_error_message', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['original_topology_id'], ['topologies.id'], ),
    sa.ForeignKeyConstraint(['result_model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('model_optimizer_analysis',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('topology_id', sa.Integer(), nullable=False),
    sa.Column('information', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['topology_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('parse_dev_cloud_profiling_result_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('profiling_result_artifact_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['profiling_result_artifact_id'], ['artifacts.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('setup_target_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.Column('setup_bundle_path', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['remote_targets.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('topology_analysis_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('batch', sa.Integer(), nullable=False),
    sa.Column('g_flops', sa.Float(), nullable=True),
    sa.Column('g_iops', sa.Float(), nullable=True),
    sa.Column('maximum_memory', sa.Float(), nullable=True),
    sa.Column('minimum_memory', sa.Float(), nullable=True),
    sa.Column('m_params', sa.Float(), nullable=True),
    sa.Column('sparsity', sa.Float(), nullable=True),
    sa.Column('ir_version', sa.Text(), nullable=True),
    sa.Column('is_obsolete', sa.Boolean(), nullable=True),
    sa.Column('topology_type', sa.Text(), nullable=True),
    sa.Column('num_classes', sa.Integer(), nullable=True),
    sa.Column('has_background', sa.Boolean(), nullable=True),
    sa.Column('mo_params', sa.Text(), nullable=True),
    sa.Column('has_batchnorm', sa.Boolean(), nullable=True),
    sa.Column('is_int8', sa.Boolean(), nullable=True),
    sa.Column('is_winograd', sa.Boolean(), nullable=True),
    sa.Column('topology_specific', sa.Text(), nullable=True),
    sa.Column('outputs', sa.Text(), nullable=True),
    sa.Column('inputs', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('upload_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('artifact_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artifact_id'], ['artifacts.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('winograd_autotune_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('result_model_id', sa.Integer(), nullable=True),
    sa.Column('inference_time', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['result_model_id'], ['topologies.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('create_int8_calibration_bundle_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('bundle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bundle_id'], ['downloadable_artifacts.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('create_profiling_bundle_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('tab_id', sa.String(), nullable=True),
    sa.Column('bundle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bundle_id'], ['downloadable_artifacts.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('deployment_bundle_configs',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('include_model', sa.Boolean(), nullable=False),
    sa.Column('model_name', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gpu_drivers', sa.Boolean(), nullable=True),
    sa.Column('vpu_drivers', sa.Boolean(), nullable=True),
    sa.Column('setup_script', sa.Boolean(), nullable=True),
    sa.Column('get_devices_script', sa.Boolean(), nullable=True),
    sa.Column('get_resources_script', sa.Boolean(), nullable=True),
    sa.Column('benchmark', sa.Boolean(), nullable=True),
    sa.Column('pot', sa.Boolean(), nullable=True),
    sa.Column('deployment_bundle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deployment_bundle_id'], ['downloadable_artifacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('single_inference_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('compound_job_id', sa.Integer(), nullable=True),
    sa.Column('latency', sa.Float(), nullable=True),
    sa.Column('throughput', sa.Float(), nullable=True),
    sa.Column('total_execution_time', sa.Float(), nullable=True),
    sa.Column('exec_graph', sa.Text(), nullable=True),
    sa.Column('runtime_representation', sa.Text(), nullable=True),
    sa.Column('layer_time_distribution', sa.Text(), nullable=True),
    sa.Column('batch', sa.Integer(), nullable=False),
    sa.Column('nireq', sa.Integer(), nullable=False),
    sa.Column('started_timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['compound_job_id'], ['compound_inferences_jobs.job_id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('trigger_dev_cloud_profiling_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('setup_bundle_id', sa.Integer(), nullable=False),
    sa.Column('profiling_bundle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['profiling_bundle_id'], ['downloadable_artifacts.id'], ),
    sa.ForeignKeyConstraint(['setup_bundle_id'], ['downloadable_artifacts.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('upload_artifact_to_target_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('artifact_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.Column('destination_directory', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artifact_id'], ['downloadable_artifacts.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['targets.id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('create_setup_bundle_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('tab_id', sa.String(), nullable=True),
    sa.Column('deployment_bundle_config_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deployment_bundle_config_id'], ['deployment_bundle_configs.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('deployment_manager_jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('tab_id', sa.String(), nullable=True),
    sa.Column('deployment_bundle_config_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deployment_bundle_config_id'], ['deployment_bundle_configs.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('deployment_targets',
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deployment_bundle_config_id', sa.Integer(), nullable=False),
    sa.Column('target', sa.Enum('cpu', 'gpu', 'myriad', 'hddl', 'opencv', 'python36', 'python37', name='deploymenttargetenum'), nullable=False),
    sa.ForeignKeyConstraint(['deployment_bundle_config_id'], ['deployment_bundle_configs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deployment_targets')
    op.drop_table('deployment_manager_jobs')
    op.drop_table('create_setup_bundle_jobs')
    op.drop_table('upload_artifact_to_target_jobs')
    op.drop_table('trigger_dev_cloud_profiling_jobs')
    op.drop_table('single_inference_jobs')
    op.drop_table('deployment_bundle_configs')
    op.drop_table('create_profiling_bundle_jobs')
    op.drop_table('create_int8_calibration_bundle_jobs')
    op.drop_table('winograd_autotune_jobs')
    op.drop_table('upload_jobs')
    op.drop_table('topology_analysis_jobs')
    op.drop_table('setup_target_jobs')
    op.drop_table('parse_dev_cloud_profiling_result_jobs')
    op.drop_table('model_optimizer_analysis')
    op.drop_table('model_optimizer')
    op.drop_table('model_downloads_configs')
    op.drop_table('model_downloader_convert_jobs')
    op.drop_table('model_download')
    op.drop_table('job_execution_details')
    op.drop_table('int8_calibration_jobs')
    op.drop_table('get_system_resources_jobs')
    op.drop_table('get_devices_jobs')
    op.drop_table('downloadable_artifacts')
    op.drop_table('download_log')
    op.drop_table('convert_keras_to_tf')
    op.drop_table('compound_inferences_jobs')
    op.drop_table('accuracy_jobs')
    op.drop_table('jobs')
    op.drop_table('projects')
    op.drop_table('remote_targets')
    op.drop_table('pipelines')
    op.drop_table('local_targets')
    op.drop_table('devices')
    op.drop_table('dev_cloud_targets')
    op.drop_table('dataset_tasks')
    op.drop_table('dataset_generation_configs')
    op.drop_table('user_metadata')
    op.drop_table('topologies')
    op.drop_table('targets')
    op.drop_table('model_precisions')
    op.drop_table('files')
    op.drop_table('datasets')
    op.drop_table('workbench_session')
    op.drop_table('wb_info')
    op.drop_table('users')
    op.drop_table('topologies_metadata')
    op.drop_table('system_resources')
    op.drop_table('proxies')
    op.drop_table('omz_topologies')
    op.drop_table('cpu_info')
    op.drop_table('artifacts')
    # ### end Alembic commands ###
