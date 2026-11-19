# Automate Names

Rename files in one directory by replacing text in their filenames. The tool
uses Python's standard library and does not recurse into subdirectories.

## Usage

The target directory is required so the tool never silently chooses a folder
and renames files there by mistake. The repository includes sample files in
`examples/rename_demo`; copy them into an ignored working directory before
trying an actual rename:

```sh
cp -R examples/rename_demo .rename-demo-work
python3 main.py --directory .rename-demo-work --find draft --replace final
```

The command prints proposed changes and leaves files untouched by default.
Add `--apply` to apply the displayed plan to your working copy:

```sh
python3 main.py --directory .rename-demo-work --find draft --replace final --apply
```

You can use any directory you choose instead of `.rename-demo-work`.

Use an empty replacement value to remove matching text:

```sh
python3 main.py --directory .rename-demo-work --find ' copy' --replace '' --apply
```

The tool checks the full plan for existing or duplicate destination names before
renaming. If the directory changes after preview, it checks the plan again and
stops if it is no longer safe.

## Tests

Run the standard-library test suite from the project directory:

```sh
python3 -m unittest discover -s tests
```
