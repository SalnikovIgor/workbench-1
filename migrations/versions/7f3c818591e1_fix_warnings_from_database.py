"""Fix warnings from database on DL Workbench start

Revision ID: 7f3c818591e1
Revises: 1e1c4fc30e7c
Create Date: 2021-02-15 10:32:30.463171

"""

"""
 OpenVINO DL Workbench
 Migration: Fix warnings from database on DL Workbench start

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
revision = '7f3c818591e1'
down_revision = '1e1c4fc30e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('project_report_export_job_project_id_fkey', 'project_report_export_job', type_='foreignkey')
    op.drop_column('project_report_export_job', 'project_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_report_export_job', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('project_report_export_job_project_id_fkey', 'project_report_export_job', 'projects', ['project_id'], ['id'])
    # ### end Alembic commands ###