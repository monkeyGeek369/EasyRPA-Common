
def str_is_empty(str):
    """str_is_empty judge str is empty

    Args:
        str (str): str

    Returns:
        bool: bool
    """
    if not str:
        return True
    if len(str) <= 0:
        return True
    return False

def str_is_not_empty(str):
    """str_is_not_empty judge str is not empty

    Args:
        str (str): str

    Returns:
        bool: bool
    """
    return not str_is_empty(str)