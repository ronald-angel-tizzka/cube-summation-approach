class FileHelper():
    @staticmethod
    def get_file(path):
        input_file = open(path)
        return input_file

    @staticmethod
    def write_2_file(data, path):
        file_output = open(path, 'w')
        file_output.write(data)

    @staticmethod
    def compare_files_data(path_1, path_2):
        """  Method used by tests to compare the content from 2 files.
        """
        file_1 = open(path_1, 'r')
        file_2 = open(path_2, 'r')

        text_1 = ','.join(map(lambda x: str(x).replace("\n", ""), file_1.readlines()))
        text_2 = ','.join(map(lambda x: str(x).replace("\n", ""), file_2.readlines()))

        return text_1 == text_2

