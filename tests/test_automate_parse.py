import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from automate_parse import FileRenamer
from main import main


class FileRenamerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_renamer(self, find="old", replace="new"):
        return FileRenamer(self.directory, find, replace)

    def test_preview_returns_matches_without_renaming(self):
        source = self.directory / "old name.txt"
        source.touch()

        planned = self.make_renamer().rename_files()

        self.assertEqual(planned, [(source, self.directory / "new name.txt")])
        self.assertTrue(source.exists())
        self.assertFalse((self.directory / "new name.txt").exists())

    def test_non_matching_files_are_skipped(self):
        unchanged = self.directory / "keep.txt"
        unchanged.touch()

        self.assertEqual(self.make_renamer().plan_renames(), [])
        self.assertTrue(unchanged.exists())

    def test_empty_search_text_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Search text"):
            self.make_renamer(find="").plan_renames()

    def test_existing_destination_blocks_the_whole_plan(self):
        source = self.directory / "old.txt"
        destination = self.directory / "new.txt"
        source.touch()
        destination.touch()

        with self.assertRaises(FileExistsError):
            self.make_renamer().plan_renames()

        self.assertTrue(source.exists())
        self.assertTrue(destination.exists())

    def test_apply_renames_changes_matching_filename(self):
        source = self.directory / "old.txt"
        source.touch()

        planned = self.make_renamer().plan_renames()
        self.make_renamer().apply_renames(planned)

        self.assertFalse(source.exists())
        self.assertTrue((self.directory / "new.txt").exists())

    def test_apply_rejects_a_plan_that_became_unsafe(self):
        source = self.directory / "old.txt"
        source.touch()
        planned = self.make_renamer().plan_renames()
        (self.directory / "new.txt").touch()

        with self.assertRaises(FileExistsError):
            self.make_renamer().apply_renames(planned)

        self.assertTrue(source.exists())

    def test_cli_defaults_to_preview(self):
        source = self.directory / "old.txt"
        source.touch()
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            main(["--directory", str(self.directory), "--find", "old", "--replace", "new"])

        self.assertTrue(source.exists())
        self.assertIn("Preview only", output.getvalue())

    def test_cli_apply_flag_performs_rename(self):
        source = self.directory / "old.txt"
        source.touch()
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            main([
                "--directory", str(self.directory),
                "--find", "old",
                "--replace", "new",
                "--apply",
            ])

        self.assertFalse(source.exists())
        self.assertTrue((self.directory / "new.txt").exists())
        self.assertIn("Renamed 1 file", output.getvalue())


if __name__ == "__main__":
    unittest.main()
