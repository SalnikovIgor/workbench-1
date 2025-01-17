"""
 OpenVINO DL Workbench
 Class for ORM model describing target machine CPU information

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
import re
from typing import Optional

from sqlalchemy import Column, Integer, String

from wb.main.enumerates import CPUPlatformTypeEnum
from wb.main.models.base_model import BaseModel
from wb.main.models.enumerates import CPU_PLATFORM_TYPE_ENUM_ENUM_SCHEMA


class CPUInfoModel(BaseModel):
    __tablename__ = 'cpu_info'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=True)
    platform_type = Column(CPU_PLATFORM_TYPE_ENUM_ENUM_SCHEMA, nullable=True)
    processor_family = Column(String, nullable=True)
    processor_number = Column(String, nullable=True)
    cores_number = Column(Integer, nullable=True)
    frequency = Column(String, nullable=True)

    def __init__(self, name: str,
                 platform_type: CPUPlatformTypeEnum,
                 processor_family: Optional[str],
                 processor_number: Optional[str],
                 cores_number: int,
                 frequency: str):
        self.name = self.format_special_symbols(name)
        self.platform_type = platform_type
        if processor_family:
            self.processor_family = self.format_special_symbols(processor_family)
        else:
            self.processor_family = re.split(r' *cpu', self.name, flags=re.RegexFlag.IGNORECASE)[0]
        self.processor_number = processor_number
        self.cores_number = cores_number
        self.frequency = frequency

    @staticmethod
    def format_special_symbols(name: str) -> str:
        return name.replace(b'\xc2\xae'.decode('utf-8'), '(R)').replace(b'\xe2\x84\xa2'.decode('utf-8'), '(TM)')

    def json(self) -> dict:
        return {
            'name': self.name,
            'platformType': self.platform_type.value,
            'processorFamily': self.processor_family,
            'processorNumber': self.processor_number,
            'coresNumber': self.cores_number,
            'frequency': self.frequency,
        }
