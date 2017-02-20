from service.summation.rows import RowQuery, RowUpdate


class MatrixUtils(object):

    @staticmethod
    def validate_sum(current_row_v, x1v, x2v, y1v, y2v, z1v, z2v):
        return x1v <= current_row_v.x <= x2v \
               and y1v <= current_row_v.y <= y2v \
               and z1v <= current_row_v.z <= z2v

    @staticmethod
    def generate_uuid(xv, yv, zv, matrix_size):
        return str(xv) + "-" + str(yv) + "-" + str(zv)

    @staticmethod
    def execute_query(line, table_dictionary):
        row_query = RowQuery(line)
        sum_value = 0
        for current_key in table_dictionary:
            current_row = RowUpdate(list(table_dictionary[current_key]))
            if MatrixUtils.validate_sum(current_row, row_query.x1, row_query.x2, row_query.y1, row_query.y2,
                                        row_query.z1, row_query.z2):
                sum_value += current_row.new_value
        return sum_value

    @staticmethod
    def execute_update(line, table_dictionary, matrix_size):
        row_update = RowUpdate(line)
        table_dictionary[MatrixUtils.generate_uuid(row_update.x, row_update.y, row_update.z, matrix_size)] = \
            (row_update.x, row_update.y, row_update.z, row_update.new_value)


