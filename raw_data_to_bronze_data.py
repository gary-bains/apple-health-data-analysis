#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json
import sys

raw_file = 'raw_data/export.xml'
bronze_file = 'bronze_data/records.jsonl'
relevant_year = '2025'
relevant_record_types = [
    'HKQuantityTypeIdentifierBodyMass',
    'HKQuantityTypeIdentifierLeanBodyMass',
    'HKQuantityTypeIdentifierBodyFatPercentage',
    'HKQuantityTypeIdentifierHeartRate',
    'HKQuantityTypeIdentifierRestingHeartRate',
    'HKQuantityTypeIdentifierWalkingHeartRateAverage',
    'HKQuantityTypeIdentifierHeartRateVariabilitySDNN',
]


def parse_health_export() -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    record_types: list[str] = []

    for _, elem in ET.iterparse(raw_file):
        if elem.tag == 'Record':
            records.append(elem.attrib)
            if elem.attrib['type'] not in record_types:
                record_types.append(elem.attrib['type'])

    return records, record_types


def is_record_relevant(record: dict) -> bool:
    return record['creationDate'].startswith(relevant_year) and record['type'] in relevant_record_types


def write_all_records_json_file(records: list[dict]):
    with open(bronze_file, 'w') as txt_file:
        for record in records:
            if is_record_relevant(record):
                txt_file.write(json.dumps(record) + '\n')


def main() -> int:
    records, record_types = parse_health_export()
    print('Found following record types')
    print(record_types)

    print('Writing JSONL file...')
    write_all_records_json_file(records)

    return 0


if __name__ == '__main__':
    sys.exit(main())
