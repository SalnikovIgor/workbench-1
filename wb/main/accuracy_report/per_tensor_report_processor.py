"""
 OpenVINO DL Workbench
 PerTensorDistanceResultProcessor

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
import json
from pathlib import Path
from typing import Optional, List
from sqlalchemy.orm import Session

from wb.main.models import TensorDistanceAccuracyReportModel, ProjectsModel, TensorDistanceAccuracyReportEntityModel


class PerTensorReportProcessor:
    def __init__(self, report_file_path: Path, project_id: int):
        self._report_file_path = report_file_path
        self._project_id = project_id

    def process_results(self, session: Session):
        previous_report = self._get_previous_report(self._project_id, session)

        try:
            self._process_new_report(session)
            if previous_report:
                session.delete(previous_report)

            session.commit()

        except Exception as exception:
            session.rollback()
            raise exception

        finally:
            session.close()

    def _process_new_report(self, session: Session):
        with self._report_file_path.open() as results_file:
            results = json.load(results_file)

        output_names = results['output_names']
        project = session.query(ProjectsModel).get(self._project_id)
        report = self._create_report_record(project, output_names)
        report.write_record(session)

        flush_interval = 50
        for index, entity in enumerate(results['entities']):
            entity_model = self._create_entity_record(report_id=report.id,
                                                      report_entity=entity)
            session.add(entity_model)
            if index % flush_interval == 0:
                session.flush()

    @staticmethod
    def _get_previous_report(project_id: int, session: Session) -> Optional[TensorDistanceAccuracyReportModel]:
        return (
            session.query(TensorDistanceAccuracyReportModel)
                .filter_by(project_id=project_id)
                .first()
        )

    @staticmethod
    def _create_report_record(project: ProjectsModel, output_names: List[str]) -> TensorDistanceAccuracyReportModel:
        report = TensorDistanceAccuracyReportModel(
            output_names=list(output_names),
            project_id=project.id,
            target_dataset_id=project.dataset_id,
        )
        return report

    @staticmethod
    def _create_entity_record(report_id: int, report_entity: dict) -> TensorDistanceAccuracyReportEntityModel:
        return TensorDistanceAccuracyReportEntityModel(
            report_id=report_id,
            image_name=report_entity['image_name'],
            output_name=report_entity['output_name'],
            mse=report_entity['mse']
        )
