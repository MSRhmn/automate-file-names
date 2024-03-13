from pathlib import Path


class FileRenamer:
    """A simple way to design file renaming class"""

    def __init__(self, path, mark_char, change_char):
        self.working_dir = self.check_path(path)
        self.mark_char = mark_char
        self.change_char = change_char

    def check_path(self, path):
        """
        This function checks if the user has passed a path.
        Otherwise it will use the default demo path.
        """
        if path:
            return Path(path).resolve()
        else:
            return Path("./files_demo").resolve()

    def rename_files(self):
        """Rename files in the working directory."""
        # This iterdir method from pathlib module checks files/directories in the current working directory.
        for f in self.working_dir.iterdir():
            # isfile method checks if it is a file or not.
            if f.is_file():
                # f.stem gets the file name while f.suffix has extension name.
                f_name, f_ext = f.stem, f.suffix
                if self.mark_char and self.change_char:
                    new_name = f_name.replace(self.mark_char, self.change_char) + f_ext
                f.rename(self.working_dir / new_name)
