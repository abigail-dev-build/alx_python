import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    print(f"Number of argument(s): {num_args}", end=" ")

    if num_args == 0:
        print(".")
    elif num_args == 1:
        print("argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print("arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
