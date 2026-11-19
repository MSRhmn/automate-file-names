from automate_parse import FileRenamer


def print_info(path):
    """Show which directory will be used for renaming."""
    print("** Make sure that you are passing the correct path. **\n")
    if path:
        print(
            f"\n>> File renaming operation will be held on '{path}' this path on your machine. <<\n"
        )
    else:
        print(
            f"\n>> File renaming operation will be held on 'files_demo' directory. <<\n"
        )


def main():
    path = input("Enter a working directory path: ")
    print_info(path)
    mark_char = input("Enter the char name that has to be replaced: ")
    change_char = input("Enter the char name that will be replaced with: ")

    try:
        renamer = FileRenamer(path, mark_char, change_char)
        renamer.rename_files()
    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
