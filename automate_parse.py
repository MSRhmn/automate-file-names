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

    def plan_renames(self):
        """Return validated (source, destination) pairs without changing files.

        Raises:
            FileNotFoundError: If the working directory does not exist.
            NotADirectoryError: If the supplied path is not a directory.
            ValueError: If the search text is empty.
            FileExistsError: If multiple files map to one destination or a
                destination already exists.
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

        planned = []
        destinations = set()
        for file_path in self.working_dir.iterdir():
            if not file_path.is_file() or self.mark_char not in file_path.name:
                continue

            new_name = file_path.name.replace(self.mark_char, self.change_char)
            destination = self.working_dir / new_name
            if destination == file_path:
                continue
            if destination in destinations:
                raise FileExistsError(
                    f"More than one file would be renamed to '{destination.name}'."
                )
            if destination.exists() or destination.is_symlink():
                raise FileExistsError(
                    f"Cannot rename '{file_path.name}': '{destination.name}' already exists."
                )
            destinations.add(destination)
            planned.append((file_path, destination))

        return planned

    def rename_files(self, apply_changes=False):
        """Preview matching renames, applying them only when explicitly asked.

        Returns the validated list of (source, destination) pairs.
        """
        planned = self.plan_renames()
        if apply_changes:
            self.apply_renames(planned)
        return planned

    def apply_renames(self, planned):
        """Apply a previously previewed plan if it is still current and safe."""
        current_plan = self.plan_renames()
        if current_plan != planned:
            raise RuntimeError("The directory changed after preview; review the plan again.")

        for source, destination in planned:
            source.rename(destination)
