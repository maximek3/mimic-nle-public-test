"""This script contains all the steps to extract MIMIC-NLE from MIMIC-CXR"""
import argparse

from utils.json_processing import read_jsonl_lines, write_jsonl_lines 
from utils.preprocess_mimic import extract_sentences


def assign_sentences(query_file, data):
    nles = []
    for line in query_file:
        nle_content = line
        source_data = data[line['sentence_ID']]
        nle_content['nle'] = source_data['sentence']
        nle_content['report_ID'] = source_data['report_ID']
        nle_content['patient_ID'] = source_data['patient_ID']
        nles.append(nle_content)
    return nles


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reports_path", type=str, help="path to MIMIC-CXR reports"
    )
    args = parser.parse_args()
    
    reports_sample = extract_sentences(args.reports_path)
    
    for subset in ["dev", "test", "train"]:
        query_file = read_jsonl_lines(f"mimic-nle/query/{subset}-query.json")
        nles = assign_sentences(query_file, reports_sample)
        write_jsonl_lines(f"mimic-nle/mimic-nle-{subset}.json", nles)
    
    a = 2