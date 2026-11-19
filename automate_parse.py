from pathlib import Path


class FileRenamer:
    """Rename files in one directory by replacing text in their names."""

    def __init__(self, path, mark_char, change_char):
        self.working_dir = self.check_path(path)
        self.mark_char = mark_char
        self.change_char = change_char

    def check_path(self, path):
        """Use the demo directory when no path is supplied."""
        return Path(path) if path else Path("./files_demo")

    def rename_files(self):
        """Rename matching files in the working directory.

        Raises:
            FileNotFoundError: If the working directory does not exist.
            NotADirectoryError: If the supplied path is not a directory.
            ValueError: If the search text is empty.
            OSError: If a file cannot be renamed.
        """
        if not self.working_dir.exists():
            raise FileNotFoundError(
                f"Directory '{self.working_dir}' does not exist."
            )
        if not self.working_dir.is_dir():
            raise NotADirectoryError(
                f"Path '{self.working_dir}' is not a directory."
            )
        if not self.mark_char:
            raise ValueError("Search text must not be empty.")

        for file_path in self.working_dir.iterdir():
            if not file_path.is_file() or self.mark_char not in file_path.name:
                continue

            new_name = file_path.name.replace(self.mark_char, self.change_char)
            file_path.rename(self.working_dir / new_name)
