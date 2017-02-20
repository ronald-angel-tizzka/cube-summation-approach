from service.persistence.file_helper import FileHelper
from service.summation.cube_summation import CubeSummation


file_path = 'test_file3.txt'
_out = 'out_'
_expected = 'ex_'
input_file = FileHelper.get_file(file_path)
cube_summation = CubeSummation(input_file)
result_summation = cube_summation.calculate()
FileHelper.write_2_file(result_summation, _out + file_path)
print(FileHelper.compare_files_data(_expected+ file_path, _out + file_path))

