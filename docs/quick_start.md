# Quick Start Guide

Get started with pathlib3 in minutes!

## Installation

Install pathlib3 using pip:

```bash
pip install pathlib3
```

## Basic Usage

### Import and Use

```python
from pathlib3 import Path

# Create a Path object
p = Path("myfile.txt")

# All standard pathlib methods work
p.touch()
p.write_text("Hello World")
content = p.read_text()

# Plus 40+ new methods!
print(p.ext())        # "txt"
print(p.basename())   # "myfile.txt"
print(p.size_human()) # "11 B"
```

### Drop-in Replacement for pathlib

You can use `Path` from pathlib3 as a drop-in replacement:

```python
# Instead of: from pathlib import Path
from pathlib3 import Path

# All your existing code works exactly the same!
home = Path.home()
cwd = Path.cwd()
files = list(home.glob("*.txt"))
```

## Common Tasks

### Working with Files

```python
from pathlib3 import Path

# Create file with parent directories
p = Path("/tmp/new/folder/file.txt")
p.touch_parent()  # Creates all parent dirs and the file

# Copy files
p.copy_to("/backup/file.txt")

# Move files
p.move_to("/archive/file.txt")

# Append content
p.append_text("New line\n")

# Get file info
print(f"Size: {p.size_human()}")
print(f"Modified: {p.mtime()}")
print(f"Age: {p.age()} seconds")
```

### Working with Directories

```python
from pathlib3 import Path

# Create directories
Path("/tmp/project/src").ensure_dir()

# List directory contents
files = Path("/tmp").ls("*.txt")
only_files = Path("/tmp").ls(only_files=True)
only_dirs = Path("/tmp").ls(only_dirs=True)

# Find files recursively
py_files = Path("/project").find_files("*.py")

# Display directory tree
print(Path("/project").tree(max_depth=2))
```

### Working with JSON

```python
from pathlib3 import Path

# Write JSON
data = {"name": "John", "age": 30}
Path("config.json").write_json(data)

# Read JSON
config = Path("config.json").read_json()

# Pretty print
Path("config.json").write_json(data, indent=4)
```

### Method Chaining

Chain methods for fluent operations:

```python
from pathlib3 import Path

# Create, write, and backup in one chain
(Path("/tmp/data.txt")
    .ensure_parent()
    .write_text("Important data")
    .backup())

# Process and save
result = (Path("/tmp/input.json")
    .read_json()
    # ... process data ...
    .write_json(processed_data)
    .hash())
```

## Next Steps

- Read the [API Reference](api.md) for complete method documentation
- Check out [Examples](examples.md) for more use cases
- Browse the [GitHub repository](https://github.com/cumulus13/pathlib3)

## Need Help?

- [GitHub Issues](https://github.com/cumulus13/pathlib3/issues) - Report bugs or request features
- [GitHub Discussions](https://github.com/cumulus13/pathlib3/discussions) - Ask questions