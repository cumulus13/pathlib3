# pathlib3

**Extended `pathlib` with 40+ additional utility methods for Python 3.6+**

`pathlib3` is a powerful extension of Python's standard `pathlib` module. It provides a `Path3` class that inherits **ALL** functionality from `pathlib.Path` while adding 40+ convenient methods for common file and directory operations.

## 🚀 Features

- ✅ **100% Compatible** - All `pathlib.Path` methods work exactly as before
- ✅ **40+ New Methods** - Additional utilities for everyday file operations
- ✅ **Type Hints** - Full type hint support for better IDE experience
- ✅ **Method Chaining** - Chainable methods for fluent API style
- ✅ **Zero Dependencies** - Only uses Python standard library
- ✅ **Well Documented** - Comprehensive docstrings with examples

## 📦 Installation

```bash
pip install pathlib3
```

Or install from source:

```bash
git clone https://github.com/cumulus13/pathlib3.git
cd pathlib3
pip install -e .
```

## 🎯 Quick Start

```python
from pathlib3 import Path3 as Path

# Use all standard pathlib.Path methods
p = Path("myfile.txt")
p.exists()          # Standard pathlib
p.read_text()       # Standard pathlib
p.write_text("hi")  # Standard pathlib

# Plus 40+ new methods!
p.ext()                              # Get extension: "txt"
p.basename()                         # Get filename: "myfile.txt"
p.size_human()                       # Get size: "1.5 KB"
p.ensure_parent().touch()            # Create parent dirs and file
p.copy_to("backup.txt")              # Copy file
p.append_text("more content")        # Append to file
p.hash()                             # Get SHA256 hash
```

## 📚 Documentation

### Basic Utilities

Get file information easily:

```python
from pathlib3 import Path3 as Path

p = Path("/home/user/documents/report.pdf")

# File name operations
p.ext()          # "pdf" - extension without dot
p.basename()     # "report.pdf" - filename with extension
p.base()         # "report" - filename without extension  
p.dirname()      # "/home/user/documents" - directory path

# Path operations
p.abspath()      # Get absolute path as string
p.normpath()     # Normalize path (remove redundant separators)
```

### Path Manipulation

Manipulate paths with convenient methods:

```python
# Join paths
p = Path("/home").join("user", "documents", "file.txt")
# Result: /home/user/documents/file.txt

# Change extension
Path("file.txt").change_ext("md")        # file.md
Path("file.txt").change_ext(".json")     # file.json

# Split path
Path("/home/user/file.txt").split_ext()  # ("/home/user/file", ".txt")
Path("/home/user/file.txt").split_path() # ["/", "home", "user", "file.txt"]
```

### Directory Operations

Work with directories efficiently:

```python
# Create directories
Path("/tmp/new/folder").ensure_dir()     # Create if doesn't exist
Path("/tmp/new/file.txt").ensure_parent() # Create parent directories

# List directory contents
Path("/tmp").ls()                        # List all
Path("/tmp").ls("*.txt")                 # List text files only
Path("/tmp").ls(only_files=True)         # Only files
Path("/tmp").ls(only_dirs=True)          # Only directories

# Display directory tree
print(Path("/project").tree(max_depth=2))
# Output:
# /project
# ├── src/
# │   ├── main.py
# │   └── utils.py
# ├── tests/
# │   └── test_main.py
# └── README.md

# Find files recursively
Path("/tmp").find("*.py")                # Find all Python files
Path("/tmp").find_files("*.txt")         # Find text files only
Path("/tmp").find_dirs("test*")          # Find directories starting with "test"
```

### File Operations

Perform file operations with ease:

```python
# Copy and move
Path("source.txt").copy_to("dest.txt")
Path("source.txt").copy_to("dest.txt", overwrite=True)
Path("old.txt").move_to("new.txt")

# Create backup
Path("important.txt").backup()           # Creates important.txt.bak
Path("important.txt").backup(".backup")  # Creates important.txt.backup

# Remove files/directories
Path("file.txt").rm()                    # Remove file
Path("folder").rm(recursive=True)        # Remove directory recursively
Path("file.txt").rm(missing_ok=True)     # Don't error if doesn't exist

# Append content
Path("log.txt").append_text("New log entry\n")
Path("data.bin").append_bytes(b'\x00\x01')

# Create file with parent directories
Path("/tmp/new/folder/file.txt").touch_parent()
```

### File Information

Get detailed file information:

```python
# File size
Path("file.txt").size()                  # 1024 (bytes)
Path("file.txt").size_human()            # "1.0 KB"
Path("folder").size()                    # Total size of all files in folder

# Timestamps
Path("file.txt").mtime()                 # Modification time
Path("file.txt").ctime()                 # Creation time
Path("file.txt").atime()                 # Access time
Path("file.txt").age()                   # Age in seconds since last modification

# Checks
Path("file.txt").is_empty()              # True if file is empty
Path("new.txt").is_newer_than("old.txt") # Compare modification times
Path("old.txt").is_older_than("new.txt") # Compare modification times
```

### Content Operations

Read and write various file formats:

```python
# Read/write text with lines
lines = Path("file.txt").lines()         # Read as list of lines
lines = Path("file.txt").lines(strip=False)  # Keep whitespace

# JSON support
data = Path("config.json").read_json()
Path("output.json").write_json({"key": "value"})
Path("output.json").write_json(data, indent=4)

# Pickle support  
data = Path("data.pkl").read_pickle()
Path("data.pkl").write_pickle({"key": "value"})

# File hashing
Path("file.txt").hash()                  # SHA256 by default
Path("file.txt").hash("md5")             # MD5 hash
Path("file.txt").checksum()              # Alias for hash()

# Count lines
Path("code.py").count_lines()            # Number of lines in file
```

## Music tag info

Get music file metadata easily:

```python
from pathlib3 import Path
music_file = Path("/mnt/musics/album/file.mp3")
music_file.music_tag() # return dict 
music_file.show_info() # print music tag info

music_dir = Path("/mnt/musics/album")
music_dir.music_tag() # return list of dict
music_dir.music_tag(exts=['mp4','m4a']) # return list of dict for specified extensions
music_dir.show_info() # print music tag info for all music files
music_dir.show_info(exts=['mp4','m4a']) # print music tag info for specified extensions
```

### Comparison Operations

Compare files easily:

```python
# Check if files have same content
Path("file1.txt").same_content("file2.txt")  # True if identical
```

### File Validation

Validate configuration files:
```python
from pathlib3 import Path

# Validate JSON (built-in, always available)
is_valid, error = Path("config.json").validate()

# Validate YAML (requires: pip install pyyaml)
is_valid, error = Path("config.yaml").validate(strict=False)

# Validate TOML (built-in Python 3.11+, or: pip install tomli)
is_valid, error = Path("settings.toml").validate()

# Validate INI (built-in, always available)
is_valid, error = Path("app.ini").validate()
```

**Optional Dependencies:**
- YAML support: `pip install pyyaml`
- TOML support (Python <3.11): `pip install tomli`

### Advanced Usage

Walk directory tree:

```python
# Similar to os.walk()
for dirpath, dirnames, filenames in Path("/project").walk():
    print(f"Directory: {dirpath}")
    print(f"Subdirs: {dirnames}")
    print(f"Files: {filenames}")
```

Method chaining for fluent API:

```python
# Chain multiple operations
(Path("/tmp/report/data.txt")
    .ensure_parent()
    .write_text("Report data")
    .copy_to("/backup/data.txt"))

# Create, write, and backup in one go
(Path("config.json")
    .write_json({"setting": "value"})
    .backup())
```

## 🔄 Complete Method List

### Inherited from `pathlib.Path`
All standard methods are available: `exists()`, `is_file()`, `is_dir()`, `mkdir()`, `read_text()`, `write_text()`, `glob()`, `rglob()`, and [many more](https://docs.python.org/3/library/pathlib.html).

### New Methods in `Path3`

**Basic Utilities:**
- `.ext()` - Get extension without dot
- `.basename()` - Get filename with extension
- `.base()` - Get filename without extension
- `.dirname()` - Get directory path
- `.abspath()` - Get absolute path as string

**Path Manipulation:**
- `.normpath()` - Normalize path
- `.join(*args)` - Join path components
- `.split_ext()` - Split into base and extension
- `.split_path()` - Split into components list
- `.change_ext(new_ext)` - Change file extension

**Directory Operations:**
- `.ensure_dir()` - Create directory if doesn't exist
- `.ensure_parent()` - Create parent directory
- `.touch_parent()` - Create parent dirs and touch file
- `.ls(pattern, only_files, only_dirs)` - List contents
- `.tree(max_depth)` - Display directory tree
- `.find(pattern, recursive)` - Find files matching pattern

**File Operations:**
- `.rm(recursive, missing_ok)` - Remove file/directory
- `.copy_to(dest, overwrite)` - Copy to destination
- `.move_to(dest)` - Move to destination
- `.append_text(text, encoding, newline)` - Append text
- `.append_bytes(data)` - Append bytes
- `.backup(suffix)` - Create backup copy

**File Information:**
- `.size()` - Get size in bytes
- `.size_human()` - Get human-readable size
- `.mtime()` - Get modification time
- `.ctime()` - Get creation time
- `.atime()` - Get access time
- `.age()` - Get age in seconds
- `.is_empty()` - Check if empty
- `.is_newer_than(other)` - Compare modification times
- `.is_older_than(other)` - Compare modification times

**Content Operations:**
- `.lines(encoding, strip)` - Read lines as list
- `.read_json(encoding)` - Read JSON file
- `.write_json(data, indent)` - Write JSON file
- `.read_pickle()` - Read pickle file
- `.write_pickle(data)` - Write pickle file
- `.hash(algorithm)` - Calculate file hash
- `.checksum(algorithm)` - Alias for hash
- `.count_lines()` - Count lines in file

**Search & Filter:**
- `.find_files(pattern)` - Find files recursively
- `.find_dirs(pattern)` - Find directories recursively
- `.walk()` - Walk directory tree (like os.walk)

**Comparison:**
- `.same_content(other)` - Check if files have same content

## 🆚 Comparison with Standard pathlib

| Operation | Standard `pathlib` | `pathlib3` |
|-----------|-------------------|------------|
| Get extension | `p.suffix.lstrip('.')` | `p.ext()` |
| Get directory | `str(p.parent)` | `p.dirname()` |
| Absolute path | `str(p.absolute())` | `p.abspath()` |
| Create parent | `p.parent.mkdir(parents=True, exist_ok=True)` | `p.ensure_parent()` |
| File size | `p.stat().st_size` | `p.size()` |
| Human size | Custom function needed | `p.size_human()` |
| List files | `list(p.glob('*'))` | `p.ls()` |
| Copy file | `shutil.copy2(p, dest)` | `p.copy_to(dest)` |
| Append text | Open file, write, close | `p.append_text(text)` |
| JSON read | `json.loads(p.read_text())` | `p.read_json()` |
| File hash | Custom implementation | `p.hash()` |
| Directory tree | Custom recursive function | `p.tree()` |

## 💡 Tips & Best Practices

### Use Method Chaining

```python
# Create a file with all parent directories
(Path("/deep/nested/structure/file.txt")
    .ensure_parent()
    .write_text("content"))

# Process and backup config
(Path("config.json")
    .read_json()
    # ... process data ...
    .write_json(processed_data)
    .backup())
```

### Import as `Path` for Drop-in Replacement

```python
# Instead of: from pathlib import Path
from pathlib3 import Path3 as Path

# Now use Path as normal, with extra methods available!
```

### Combine with Standard pathlib Features

```python
# Use pathlib features with Path3 extensions
p = Path.home() / "documents" / "report.txt"
p.ensure_parent().write_text("Report content")

# Glob patterns with extensions
for file in Path("/logs").find("*.log"):
    if file.age() > 86400:  # Older than 1 day
        print(f"Old log: {file.basename()} - {file.size_human()}")
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of Python's excellent `pathlib` module
- Inspired by the need for more convenient path operations
- Thanks to all contributors!

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/cumulus13/pathlib3/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cumulus13/pathlib3/discussions)
- **Documentation**: [Read the Docs](https://pathlib3.readthedocs.io)

## 🔗 Links

- **PyPI**: https://pypi.org/project/pathlib3/
- **GitHub**: https://github.com/cumulus13/pathlib3
- **Documentation**: https://pathlib3.readthedocs.io

---

## Author

[Hadi Cahyadi](mailto:cumulus13@gmail.com)

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cumulus13)

[![Donate via Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cumulus13)

[Support me on Patreon](https://www.patreon.com/cumulus13)