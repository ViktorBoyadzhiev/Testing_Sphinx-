from general_subblocks.subfunctions1 import first_function
from general_subblocks.subfunctions2 import my_first_sub_function, my_second_sub_function


def to_execute():
    """This function will be calling my subfunctions. The purpose of this dummy program is to test Sphinx lib"""
    first_function()
    my_first_sub_function()
    my_second_sub_function()


to_execute()
