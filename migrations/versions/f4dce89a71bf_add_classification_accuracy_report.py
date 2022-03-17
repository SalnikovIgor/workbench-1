"""Add classification accuracy report

Revision ID: f4dce89a71bf
Revises: 5181f24c23aa
Create Date: 2021-07-23 19:40:02.016769

"""

"""
 OpenVINO DL Workbench
 Migration: Add classification accuracy report

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
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4dce89a71bf'
down_revision = '5181f24c23aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accuracy_classification_report_image_classes',
                    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
                    sa.Column('last_modified', sa.DateTime(), nullable=True),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('report_id', sa.Integer(), nullable=True),
                    sa.Column('image_name', sa.String(), nullable=False),
                    sa.Column('annotation_class_id', sa.Integer(), nullable=False),
                    sa.Column('confidence_in_annotation_class_id', sa.Float(), nullable=False),
                    sa.Column('annotation_id_rank_in_predictions', sa.Integer(), nullable=False),
                    sa.Column('top_1_prediction', sa.Integer(), nullable=False),
                    sa.Column('top_1_prediction_confidence', sa.Float(), nullable=False),
                    sa.ForeignKeyConstraint(['report_id'], ['accuracy_report.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accuracy_classification_report_image_classes')
    # ### end Alembic commands ###