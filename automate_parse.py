from pathlib import Path

print("** Make sure that you are passing the correct path **\n")

path = input("Enter a working directory path: ")
mark_char = input("Enter the char name that has to be replaced: ")
change_char = input("Enter the char name that will be replaced with: ")


def check_path():
    """
    This function checks if the user has passed a path.
    Otherwise it will use the default demo path.
    """
    if path:
        return Path(path).resolve()
    else:
        return Path("./files_demo").resolve()


def main():

    working_dir = check_path()

    # This iterdir method from pathlib module checks files/directories in the current working directory.
    for f in working_dir.iterdir():
        # isfile method checks if it is a file or not.
        if f.is_file():
            # f.stem gets the file name while f.suffix has extension name.
            f_name, f_ext = f.stem, f.suffix
            if mark_char and change_char:
                new_name = f_name.replace(mark_char, change_char) + f_ext
            f.rename(working_dir / new_name)


if __name__ == "__main__":
    main()
