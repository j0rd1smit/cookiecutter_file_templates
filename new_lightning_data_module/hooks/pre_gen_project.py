import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

file_name = '{{ cookiecutter.data_module_file_name }}'
class_name = '{{ cookiecutter.data_module_class_name }}'


if not re.match(MODULE_REGEX, file_name):
    print('ERROR: %s is not a valid Python module file name!' % file_name)

    # exits with status 1 to indicate failure
    sys.exit(1)


if not re.match(MODULE_REGEX, class_name):
    print('ERROR: %s is not a valid Python module file name!' % class_name)

    # exits with status 1 to indicate failure
    sys.exit(1)