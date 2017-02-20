import unittest
from service.persistence.file_helper import FileHelper
from service.summation.cube_summation import CubeSummation


class TestSummation(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSummation, self).__init__(*args, **kwargs)

    def test_summation_passed(self):
        file_path = 'test_file3.txt'
        _out = 'out_'
        _expected = 'ex_'
        input_file = FileHelper.get_file(file_path)
        cube_summation = CubeSummation(input_file)
        result_summation = cube_summation.calculate()
        FileHelper.write_2_file(result_summation, _out + file_path)
        self.assertTrue((FileHelper.compare_files_data(_expected+ file_path, _out + file_path)))

    def test_summation_wrong(self):
        file_path = 'test_file3.txt'
        _out = 'out_'
        _expected = 'ex_'
        input_file = FileHelper.get_file(file_path)
        cube_summation = CubeSummation(input_file)
        result_summation = cube_summation.calculate()
        FileHelper.write_2_file(result_summation, _out + file_path)
        self.assertFalse((FileHelper.compare_files_data(file_path, _out + file_path)))