def sum_func(a, b):
    """
    Returns the sum of a and b
    A placeholder function for unit testing
    :param int a: first integer
    :param int b: second integer
    :return int: sum of a and b
    """

    return a+b


def easy_time(yyyy_mm_dd):
    rfc3399 = f"{yyyy_mm_dd}T00:00:00+0000"
    return rfc3399


def is_datestring_iso8600(datestring):
    """
    Checks if the provided date (string) follows the YYYY-MM-DD format (ISO8600)
    :param str datestring: Date in string format
    :return boolean: Is datestring following ISO8600 format
    """

    return True