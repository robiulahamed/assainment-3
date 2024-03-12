def check_all_true(bool_list):
    """
    Check if all elements in the list are True.
    """
    return all(bool_list)

def check_any_true(bool_list):
    """
    Check if any element in the list is True.
    """
    return any(bool_list)

# Example usage
bool_list = [True, False, True, True]

print("List of boolean values:", bool_list)
print("All elements are True:", check_all_true(bool_list))
print("Any element is True:", check_any_true(bool_list))