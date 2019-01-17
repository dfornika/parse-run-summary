import os
import unittest
import json

TEST_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

from parse_run_summary import parse_read_summary

class RunSummaryParserTest(unittest.TestCase):
    def setUp(self):
        self.test_data_path = os.path.join(TEST_DIR_PATH, 'data/summary.txt')
        with open(os.path.join(TEST_DIR_PATH, 'data/parsed_results/parsed_read_summary.json')) as read_summary_json:
            self.parsed_read_summary_json = json.load(read_summary_json)
            read_summary_json.close()

    def test_parse_read_summary(self):
        parsed_result = parse_read_summary(self.test_data_path)
        paired_results = zip(parsed_result, self.parsed_read_summary_json)
        for parsed_read_summary_record, parsed_read_summary_json_record in paired_results:
            self.assertDictEqual(parsed_read_summary_record, parsed_read_summary_json_record)

if __name__ == '__main__':
    unittest.main()
