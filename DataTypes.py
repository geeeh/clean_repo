def data_types(my_vars):
    if isinstance(my_vars, str):
        return len(my_vars)
    elif my_vars== None:
        return "no value"
    elif isinstance(my_vars, bool):
        return my_vars

    elif isinstance(my_vars, int):
        if my_vars<100:
            return "less than 100"
        elif my_vars>100:
            return"more than 100"
        else:
            return "equal to 100"
    elif isinstance(my_vars, list):
        if len(my_vars)>=3:
            return my_vars[2]
        else:
            return None


    else:
        return "please input data"

