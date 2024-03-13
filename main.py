from automate_parse import FileRenamer


def main():
    print("** Make sure that you are passing the correct path **\n")
    path = input("Enter a working directory path: ")
    mark_char = input("Enter the char name that has to be replaced: ")
    change_char = input("Enter the char name that will be replaced with: ")

    renamer = FileRenamer(path, mark_char, change_char)
    renamer.rename_files()


if __name__ == "__main__":
    main()
