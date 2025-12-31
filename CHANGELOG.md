# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-30

### Added
- Initial release of pathlib3
- `Path` class extending `pathlib.Path` with 40+ additional methods
- `PurePath3` class for path manipulation without I/O
- Basic utilities: `ext()`, `basename()`, `base()`, `dirname()`, `abspath()`
- Path manipulation: `normpath()`, `join()`, `split_ext()`, `split_path()`, `change_ext()`
- Directory operations: `ensure_dir()`, `ensure_parent()`, `touch_parent()`, `ls()`, `tree()`, `find()`
- File operations: `rm()`, `copy_to()`, `move_to()`, `append_text()`, `append_bytes()`, `backup()`
- File info: `size()`, `size_human()`, `mtime()`, `ctime()`, `atime()`, `age()`, `is_empty()`, `is_newer_than()`, `is_older_than()`
- Content operations: `lines()`, `read_json()`, `write_json()`, `read_pickle()`, `write_pickle()`, `hash()`, `checksum()`, `count_lines()`
- Search & filter: `find_files()`, `find_dirs()`, `walk()`
- Comparison: `same_content()`
- Full type hints support
- Comprehensive documentation
- Method chaining support

### Features
- 100% backward compatible with `pathlib.Path`
- Zero dependencies (only standard library)
- Python 3.6+ support
- Complete docstrings with examples
- PEP 561 compliant (type hints)

## [Unreleased]

### Planned
- Additional comparison methods
- Archive operations (zip, tar)
- Advanced search with regex
- File watching capabilities
- Symlink utilities