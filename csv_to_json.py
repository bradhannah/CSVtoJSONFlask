import json
import ast
import csv

class CsvToJson:
    def __init__(self):
        self.init = 1

    def _csv_lines_to_dict(self, csv_lines):
        csv_dict = {}
        first = True
        i = 0
        header_list = None  #
        csv_dissected_rows = csv.reader(csv_lines, delimiter=',', skipinitialspace=True, strict=True)
        for csv_line in csv_dissected_rows:
            csv_line_split = csv_line
            if first:
                first = False
                header_list = csv_line_split
                header_list = list(map(lambda x: x.lstrip(), header_list))
            else:
                csv_line_dict = {}
                header_index = 0
                for header_item in header_list:
                    csv_line_dict[header_item] = self._try_eval(csv_line_split[header_index].lstrip())
                    header_index += 1
                csv_dict[csv_line_split[0].lstrip()] = csv_line_dict
        return csv_dict

    def keyed_csv_to_array(self, csv_lines):
        if type(csv_lines) != list:
            return "FAILED"
        csv_dict = self._csv_lines_to_dict(csv_lines)
        json_output = json.dumps(csv_dict, sort_keys=True)
        return json_output

    @staticmethod
    def _try_eval(val):
        if val == "" or " " in val:
            return val
        if val.casefold() == "true":
            return True
        if val.casefold() == "false":
            return False
        try:
            val = ast.literal_eval(val)
        except ValueError:
            pass
        return val
