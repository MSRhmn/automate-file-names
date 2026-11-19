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
        planned = renamer.rename_files()
        if not planned:
            print("No matching files found.")
            return

        print("Planned renames:")
        for source, destination in planned:
            print(f"  {source.name} -> {destination.name}")

        answer = input("Apply these changes? [y/N]: ").strip().lower()
        if answer != "y":
            print("No files were renamed.")
            return

        renamer.apply_renames(planned)
        print(f"Renamed {len(planned)} file(s).")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
