import os

print("*** Make sure that you are passing the correct path ***\n")

wd_path = input("Enter a working directory path: ")
mark_item = input("Enter the item name that has to be replaced: ")
change_item = input("Enter the item name that will be replaced with: ")


def check_path():
    """
    This function checks if the user has passed a path.
    Otherwise it will use the default demo path.
    """
    if wd_path:
        return os.chdir(wd_path)
    else:
        return os.chdir("./files_demo")


def main():

    check_path()

    # This listdir method from os module checks files/directories in the current working directory.
    for f in os.listdir():
        # isfile method checks if it is a file or not.
        if os.path.isfile(f):
            # This splitext method does as it says, splits the extension from file name.
            f_name, f_ext = os.path.splitext(f)
            # Check if the user has provided file modifying inputs.
            if mark_item and change_item:
                new_name = f_name.replace(mark_item, change_item) + f_ext
            else:
                new_name = f_name.replace(".", "-") + f_ext
            os.rename(f, new_name)


if __name__ == "__main__":
    main()
