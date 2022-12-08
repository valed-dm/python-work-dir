# Scenario
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements:
# the student's first name,
# the student's last name,
# and the number of point the student received during certain classes.

# The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

# The file may look as follows:

# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5
# samplefile.txt

# Your task is to write a program which:

# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report, just like this one:
# Andrew Cox 	 1.5
# Anna Boleyn 	 15.5
# John Smith 	 7.0
# output

# ------------------------------------------------------------------------
# Note:
# your program must be fully protected against all possible failures:
#   the file's non-existence,
#   the file's emptiness,
#   or any input data failures;
# encountering any data error should cause immediate program termination,
# and the erroneous should be presented to the user;
# implement and use your own exceptions hierarchy -
# we've presented it in the editor;

# the second exception should be raised when a bad line is detect,
# and the third when the source file exists but is empty.

# Tip: Use a dictionary to store the students' data.
# ------------------------------------------------------------------------

import sys
from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, std_data):
        StudentsDataException.__init__(self)
        print(
            'source data doesn\'t match expected format: [first name, last name, points(str: int or float)]\ndata received:', std_data)


class FileEmpty(StudentsDataException):
    def __init__(self, path):
        StudentsDataException.__init__(self)
        print('file contains no data:', path)


std_dict = {}

prompt_1 = 'Please, enter file path. Print exit to abort: '
prompt_2 = 'Please, enter another file path. Print exit to abort: '


def is_float(val):
    try:
        num = float(val)
    except ValueError:
        return False
    return True


def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True


def is_str_to_number(val):
    if is_float(val) or is_int(val):
        return True
    return False


def user_input(prompt):
    global file_path
    while True:
        try:
            file_path = input(prompt)
            assert len(file_path) > 0
            if file_path == 'exit':
                sys.exit('Student results calculation successfully stopped.')
            break
        except AssertionError:
            print('An error occured: nothing entered.')
            continue


def student_res():
    try:
        s = open(file_path, 'rt')
        # print(s.read())
        line = s.readline()
        if line == '':
            raise FileEmpty(file_path)

        while line != '':
            std_data = line.split()

            if len(std_data) != 3:
                raise BadLine(std_data)
            elif not is_str_to_number(std_data[2]):
                raise BadLine(std_data)
            else:
                # print(std_data)
                std_name = str(std_data[0]) + ' ' + str(std_data[1])
                if not std_name in std_dict:
                    std_dict[std_name] = float(std_data[2])
                else:
                    std_dict[std_name] += float(std_data[2])
                line = s.readline()

    except IOError as e:
        print('An error occurred while reading:', strerror(e.errno))
        calc(prompt_2)
    except FileEmpty:
        calc(prompt_2)
    except BadLine:
        calc(prompt_2)
    except StudentsDataException as e:
        print('An unexpected error occurred: ', strerror(e.errno))
        exit(e.errno)

    s.close()


def calc(prompt):
    user_input(prompt)
    student_res()


calc(prompt_1)

std_dict = dict(sorted(std_dict.items(), key=lambda item: item[0]))
for key in std_dict:
    print(key, std_dict[key])


# testing text file_path = '/Users/dmitrijvaledinskij/Python/data/std_results.txt'
# testing empty file_path = '/Users/dmitrijvaledinskij/Python/data/empty.txt'
# testing broken_1 file_path = '/Users/dmitrijvaledinskij/Python/data/std_results_broken_1.txt'
# testing broken_2 file_path = '/Users/dmitrijvaledinskij/Python/data/std_results_broken_2.txt'
# testing broken_3 file_path = '/Users/dmitrijvaledinskij/Python/data/std_results_broken_3.txt'
# testing broken_4 file_path = '/Users/dmitrijvaledinskij/Python/data/std_results_broken_4.txt'
