from automate_parse import FileRenamer


def print_input():
    """Checking if the user has provided a path or not."""
    if path:
        print(
            f"\n>> File renaming operation will be held on '{path}' this path on your machine. <<\n"
        )
    else:
        print(
            f"\n>> File renaming operation will be held on 'files_demo' directory. <<\n"
        )


def main():
    print("** Make sure that you are passing the correct path. **\n")
    path = input("Enter a working directory path: ")
    print_input()
    mark_char = input("Enter the char name that has to be replaced: ")
    change_char = input("Enter the char name that will be replaced with: ")

    renamer = FileRenamer(path, mark_char, change_char)
    renamer.rename_files()


if __name__ == "__main__":
    main()
