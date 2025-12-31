# API Reference

Complete API reference for pathlib3.

## Path Class

```{eval-rst}
.. autoclass:: pathlib3.Path
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
```

## PurePath3 Class

```{eval-rst}
.. autoclass:: pathlib3.PurePath3
   :members:
   :undoc-members:
   :show-inheritance:
```

## Method Categories

### Basic Utilities

Methods for getting basic path information:

- `ext()` - Get extension without dot
- `basename()` - Get filename with extension
- `base()` - Get filename without extension
- `dirname()` - Get directory path
- `abspath()` - Get absolute path as string

### Path Manipulation

Methods for manipulating paths:

- `normpath()` - Normalize path
- `join(*args)` - Join path components
- `split_ext()` - Split into base and extension
- `split_path()` - Split into components list
- `change_ext(new_ext)` - Change file extension

### Directory Operations

Methods for working with directories:

- `ensure_dir()` - Create directory if doesn't exist
- `ensure_parent()` - Create parent directory
- `touch_parent()` - Create parent dirs and touch file
- `ls(pattern, only_files, only_dirs)` - List contents
- `tree(max_depth)` - Display directory tree
- `find(pattern, recursive)` - Find files matching pattern

### File Operations

Methods for file manipulation:

- `rm(recursive, missing_ok)` - Remove file/directory
- `copy_to(dest, overwrite)` - Copy to destination
- `move_to(dest)` - Move to destination
- `append_text(text)` - Append text to file
- `append_bytes(data)` - Append bytes to file
- `backup(suffix)` - Create backup copy

### File Information

Methods for getting file information:

- `size()` - Get size in bytes
- `size_human()` - Get human-readable size
- `mtime()` - Get modification time
- `ctime()` - Get creation time
- `atime()` - Get access time
- `age()` - Get age in seconds
- `is_empty()` - Check if empty
- `is_newer_than(other)` - Compare modification times
- `is_older_than(other)` - Compare modification times

### Content Operations

Methods for reading/writing content:

- `lines(encoding, strip)` - Read lines as list
- `read_json(encoding)` - Read JSON file
- `write_json(data, indent)` - Write JSON file
- `read_pickle()` - Read pickle file
- `write_pickle(data)` - Write pickle file
- `hash(algorithm)` - Calculate file hash
- `checksum(algorithm)` - Alias for hash
- `count_lines()` - Count lines in file

### Search & Filter

Methods for searching:

- `find_files(pattern)` - Find files recursively
- `find_dirs(pattern)` - Find directories recursively
- `walk()` - Walk directory tree

### Comparison

Methods for comparing files:

- `same_content(other)` - Check if files have same content

### Music File Metadata

Methods for working with music file metadata:

- `show_info()` - Display music file metadata
- `show_info(exts)` - Display metadata for music files in directory
- `music_tag()` - Get music file metadata as dict
- `music_tag(exts)` - Get metadata for music files in directory as list of dicts
