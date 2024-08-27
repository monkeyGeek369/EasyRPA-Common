def num_is_empty(num):
    """num_is_empty judge num is empty

    Args:
        num (int): int

    Returns:
        bool: bool
    """
    if not num:
        return True
    if num <= 0:
        return True
    return False

def num_is_not_empty(num):
    """num_is_not_empty judge num is not empty

    Args:
        num (int): int

    Returns:
        bool: bool
    """
    return not num_is_empty(num)
