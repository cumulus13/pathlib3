# Examples

Practical examples of using pathlib3.

## Basic File Operations

```python
from pathlib3 import Path

# Create a file with parent directories
p = Path("/tmp/new/folder/file.txt")
p.touch_parent()

# Get file information
print(f"Extension: {p.ext()}")
print(f"Size: {p.size_human()}")
print(f"Age: {p.age()} seconds")

# Copy and backup
p.copy_to("/backup/file.txt")
p.backup()  # Creates file.txt.bak
```

## Working with JSON

```python
from pathlib3 import Path

# Write JSON
config = {"host": "localhost", "port": 8080}
Path("config.json").write_json(config)

# Read JSON
config = Path("config.json").read_json()
print(config["host"])

# Update and save
config["port"] = 9090
Path("config.json").write_json(config, indent=4)
```

## Directory Tree Operations

```python
from pathlib3 import Path

# Create nested structure
base = Path("/tmp/project")
base.ensure_dir()

(base / "src").ensure_dir()
(base / "src" / "main.py").touch()
(base / "src" / "utils.py").touch()
(base / "tests").ensure_dir()
(base / "README.md").touch()

# Display tree
print(base.tree(max_depth=2))

# Find all Python files
py_files = base.find_files("*.py")
for f in py_files:
    print(f"Found: {f}")
```

## File Management

```python
from pathlib3 import Path

# Organize files by extension
source_dir = Path("/downloads")
for file in source_dir.ls(only_files=True):
    ext = file.ext()
    if ext:
        dest_dir = Path(f"/organized/{ext}")
        dest_dir.ensure_dir()
        file.move_to(dest_dir / file.name)
```

## Log File Processing

```python
from pathlib3 import Path

# Process log files
log_file = Path("/var/log/app.log")

# Get file info
print(f"Log size: {log_file.size_human()}")
print(f"Lines: {log_file.count_lines()}")

# Append new log entry
log_file.append_text("[INFO] Application started\n")

# Backup old logs
if log_file.size() > 10_000_000:  # 10 MB
    backup = log_file.backup(f".{log_file.mtime()}")
    log_file.write_text("")  # Clear log
```

## File Comparison and Verification

```python
from pathlib3 import Path

# Compare files
file1 = Path("original.txt")
file2 = Path("copy.txt")

if file1.same_content(file2):
    print("Files are identical")

# Verify file integrity
checksum = Path("download.zip").hash("sha256")
print(f"SHA256: {checksum}")

# Compare with expected
expected = "abc123..."
if checksum == expected:
    print("File verified!")
```

## Batch Operations

```python
from pathlib3 import Path

# Process all text files
docs_dir = Path("/documents")
for txt_file in docs_dir.find_files("*.txt"):
    # Create backup
    txt_file.backup()
    
    # Convert to markdown
    lines = txt_file.lines()
    md_file = txt_file.change_ext("md")
    md_file.write_text("\n".join(lines))
    
    print(f"Converted: {txt_file.basename()} -> {md_file.basename()}")
```

## Method Chaining

```python
from pathlib3 import Path

# Chain multiple operations
result = (Path("/tmp/data.json")
    .ensure_parent()
    .write_json({"status": "ok"})
    .copy_to("/backup/data.json")
    .hash())

print(f"Checksum: {result}")

# Complex workflow
(Path("/reports/2024/")
    .ensure_dir()
    .join("summary.txt")
    .touch()
    .append_text("Report Summary\n")
    .append_text("=" * 50 + "\n"))
```

## Cleanup Operations

```python
from pathlib3 import Path
import time

# Clean old cache files
cache_dir = Path("/tmp/cache")
max_age = 86400  # 1 day in seconds

for file in cache_dir.find_files():
    if file.age() > max_age:
        print(f"Removing old file: {file.basename()}")
        file.rm()

# Clean empty directories
for dir_path in cache_dir.find_dirs():
    if dir_path.is_empty():
        print(f"Removing empty dir: {dir_path}")
        dir_path.rm()
```

## Data Processing

```python
from pathlib3 import Path

# Process CSV data
data_file = Path("data.csv")
lines = data_file.lines()

# Process each line
results = []
for line in lines[1:]:  # Skip header
    # ... process line ...
    results.append(processed)

# Save results as JSON
output = Path("results.json")
output.write_json(results, indent=2)

# Create summary
summary = Path("summary.txt")
summary.write_text(f"Processed {len(results)} records\n")
summary.append_text(f"Output: {output.abspath()}\n")
summary.append_text(f"Size: {output.size_human()}\n")
```

## Music tag info
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

## Validate File Integrity

```python
from pathlib3 import Path, YAML_AVAILABLE, TOML_AVAILABLE

# Check available libraries
print(f"YAML support: {YAML_AVAILABLE}")
print(f"TOML support: {TOML_AVAILABLE}")

# Validate JSON (always works)
is_valid, error = Path("config.json").validate()
if is_valid:
    print("Valid JSON!")
else:
    print(f"Invalid: {error}")

# Validate YAML (needs PyYAML)
is_valid, error = Path("config.yaml").validate(strict=False)
if not is_valid:
    print(f"Error: {error}")

# Auto-detect from extension
Path("settings.toml").validate()  # Auto-detects TOML

# Manual file type
Path("data.txt").validate(file_type='json')  # Force JSON validation
```









