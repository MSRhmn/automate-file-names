import argparse

from automate_parse import FileRenamer


def build_parser():
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Preview or rename files by replacing text in their names."
    )
    parser.add_argument(
        "--directory",
        required=True,
        help="directory to scan",
    )
    parser.add_argument(
        "--find",
        required=True,
        help="text to find in each filename",
    )
    parser.add_argument(
        "--replace",
        required=True,
        help="replacement text; use an empty string to remove matches",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="apply the previewed changes; without this flag, files are unchanged",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        renamer = FileRenamer(args.directory, args.find, args.replace)
        planned = renamer.rename_files()
        if not planned:
            print("No matching files found.")
            return

        print("Planned renames:")
        for source, destination in planned:
            print(f"  {source.name} -> {destination.name}")

        if not args.apply:
            print("Preview only; rerun with --apply to rename these files.")
            return

        renamer.apply_renames(planned)
        print(f"Renamed {len(planned)} file(s).")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
