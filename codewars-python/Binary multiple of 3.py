import re

PATTERN = re.compile( r"^(0*1(01*0)*1)*0*$")

def is_divisible_by_3(binary_string):
    return bool(re.match(PATTERN, binary_string))


