def list_division(my_list_1, my_list_2, list_length):
    """Calculates the division of two lists"""
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            elif type(my_list_1[i]) not in (int, float) or
            type(my_list_2[i]) not in (int, float):
                raise TypeError
            elif my_list_2[i] == 0:
                raise ZeroDivisionError
            else:
                result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
