def make_part(column_width, separete, line):
    one_part = separete + " "
    one_part += "".join(line + " " for i in range(column_width))
    return one_part

def make_one_part(column_width, is_blank_line):
    if is_blank_line:
        return make_part(column_width, "|", " ")
    return make_part(column_width, "+", "-")

def make_horizontal_line(column_width, horizontal_number, is_blank_line):
    horizontal_line = ""
    for i in range(horizontal_number):
        horizontal_line += make_one_part(column_width, is_blank_line)
    if is_blank_line:
        return horizontal_line + "|"
    return horizontal_line + "+"

def write_part_of_column(separete_line, blank_line, column_height):
    print(separete_line)
    for i in range(column_height):
        print(blank_line)

def write_lattice_by_lines(separete_line, blank_line, column_height, vertical_number):
    for i in range(vertical_number):
        write_part_of_column(separete_line, blank_line, column_height)
    print(separete_line)

def write_lattice(column_width, column_height, horizontal_number, vertical_number):
    blank_line = make_horizontal_line(column_width, horizontal_number, True)
    separete_line = make_horizontal_line(column_width, horizontal_number, False)
    write_lattice_by_lines(separete_line, blank_line, column_height, vertical_number)

if __name__ == "__main__":
    write_lattice(4, 4, 3, 3)
