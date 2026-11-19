# Automate Names

Rename files in one directory by replacing text in their filenames. The tool
uses Python's standard library and does not recurse into subdirectories.

## Usage

Preview matching files in the default `files_demo` directory:

```sh
python3 main.py --find old --replace new
```

Choose a directory:

```sh
python3 main.py --directory ./inbox --find draft --replace final
```

The command prints the proposed changes and leaves files untouched by default.
Add `--apply` to apply the displayed plan:

```sh
python3 main.py --directory ./inbox --find draft --replace final --apply
```

Use an empty replacement value to remove matching text:

```sh
python3 main.py --directory ./inbox --find ' copy' --replace '' --apply
```

The tool checks the full plan for existing or duplicate destination names before
renaming. If the directory changes after preview, it checks the plan again and
stops if it is no longer safe.

## Tests

Run the standard-library test suite from the project directory:

```sh
python3 -m unittest discover -s tests
```
