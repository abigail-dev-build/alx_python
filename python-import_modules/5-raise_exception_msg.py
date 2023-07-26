def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("This is a custom name exception.")
except NameError as e:
    print("Caught a name exception:", e)
