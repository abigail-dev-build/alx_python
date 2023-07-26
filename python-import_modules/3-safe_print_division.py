def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        result = None
    finally: 
            # if result is not None:
                print("Inside result: {}".format(result))
                print("{:d} / {:d} = {}".format(a, b, result))
            # else:
            #      print("Inside result: {}".format(result))
    return result