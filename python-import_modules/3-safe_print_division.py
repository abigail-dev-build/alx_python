def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        result = None
    finally: 
            print("Inside result: {}".format(result))
            print("{:d} / {:d} = {}".format(a, b, result))

safe_print_division(12, 0)