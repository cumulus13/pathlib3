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

## Handling None Values

pathlib3 safely handles `None` values:
```python
from pathlib3 import Path

# Path(None) returns current directory
p = Path(None)  # Path('.')

other_dir = None # if some variable is None
p = Path(other_dir, "my_dir")  # Path('my_dir')

# Use safe() for explicit None handling
p = Path.safe(None)           # Path('.')
p = Path.safe(None, '/tmp')   # Path('/tmp')

# Use from_optional() to preserve None
p = Path.from_optional(None)        # None
p = Path.from_optional("file.txt")  # Path('file.txt')

# with multiple args
b = Path(None, "subdir")    # Path('subdir')
print(b)                    # subdir

# Normal usage still works
g = Path("normal.txt")
print(g)                    # normal.txt
```

## Get Metadata

```python
from pathlib3 import Path, PIL_AVAILABLE, PYPDF2_AVAILABLE

# Check available libraries
print(f"Image support: {PIL_AVAILABLE}")
print(f"PDF support: {PYPDF2_AVAILABLE}")

# Get image metadata
meta = Path("photo.jpg").metadata()
print(meta['width'], meta['height'])
print(meta['exif']['camera_make'])

# Get PDF metadata
meta = Path("document.pdf").metadata()
print(f"Pages: {meta['pages']}")
print(f"Author: {meta['author']}")

# Get audio metadata
meta = Path("song.mp3").metadata()
print(f"Artist: {meta['artist']}")
print(f"Duration: {meta['length_human']}")

# Simple summary
print(Path("photo.jpg").metadata_simple())

# Raw metadata
meta = Path("photo.jpg").metadata(raw=True)
print(meta['exif_raw'])  # All EXIF data
```

## Send as Email Attachment

```python
from pathlib3 import Path, EmailConfig

# Setup email config (Gmail example)
config = EmailConfig.gmail(
    username='your.email@gmail.com',
    password='your_app_password'  # Get from: https://myaccount.google.com/apppasswords
)

# Send single file
Path('report.pdf').email_as_attachment(
    to='boss@company.com',
    subject='Monthly Report',
    body='Please find the monthly report attached.',
    config=config
)

# Send to multiple people
Path('invoice.pdf').email_as_attachment(
    to=['client@company.com', 'manager@company.com'],
    subject='Invoice #12345',
    body='Your invoice is attached.',
    cc='accounting@company.com',
    bcc='archive@company.com',
    config=config
)

html_body = """
<html>
  <body>
    <h2>Monthly Report</h2>
    <p>Dear Boss,</p>
    <p>Please find the <strong>monthly report</strong> attached.</p>
    <p>Best regards,<br>Your Name</p>
  </body>
</html>
"""

Path('report.pdf').email_as_attachment(
    to='boss@company.com',
    subject='Monthly Report',
    body='Plain text version',
    body_html=html_body,
    config=config
)

# Send email with multiple files
Path.send_email(
    to='client@company.com',
    subject='Project Deliverables',
    body='Please find all project files attached.',
    config=config,
    attachments=[
        'report.pdf',
        'presentation.pptx',
        'data.xlsx',
        Path('images/chart.png')
    ]
)

# Gmail
config_gmail = EmailConfig.gmail('user@gmail.com', 'app_password')

# Outlook/Hotmail
config_outlook = EmailConfig.outlook('user@outlook.com', 'password')

# Office 365
config_o365 = EmailConfig.office365('user@company.com', 'password')

# Yahoo
config_yahoo = EmailConfig.yahoo('user@yahoo.com', 'password')

# Custom SMTP server
config_custom = EmailConfig(
    smtp_server='mail.mycompany.com',
    smtp_port=587,
    username='user@mycompany.com',
    password='password',
    use_tls=True
)

html_with_image = """
<html>
  <body>
    <h2>Check out this chart:</h2>
    <img src="cid:chart.png" alt="Sales Chart">
  </body>
</html>
"""

Path('chart.png').email_as_attachment(
    to='team@company.com',
    subject='Sales Chart',
    body_html=html_with_image,
    config=config,
    inline_images=True
)

try:
    Path('report.pdf').email_as_attachment(
        to='boss@company.com',
        subject='Report',
        body='Attached.',
        config=config
    )
    print("Email sent successfully!")
    
except ConnectionError as e:
    print(f"Failed to send: {e}")
    
except ValueError as e:
    print(f"Invalid input: {e}")

```

## Image Manipulation

Perform basic image operations:

```python
from pathlib3 import Path

# Multiple ICO files (one per size)
Path('logo.png').to_ico()
# Creates: logo_16.ico, logo_32.ico, logo_48.ico, ...

# Single multi-size ICO (Windows style)
Path('app.png').to_ico(multi_size=True)
# Creates: app.ico (contains all sizes)

# Custom sizes
Path('icon.png').to_ico(
    sizes=[16, 32, 64, 128],
    multi_size=True
)

# Favicon for website
Path('logo.png').to_ico(
    sizes=[16, 32, 48],
    output_path='favicon.ico',
    multi_size=True
)

# Resize to width (auto height)
Path('photo.jpg').resize(width=1920)

# Resize to fit in 1024x1024
Path('image.png').resize(max_size=1024)

# Exact dimensions (may distort)
Path('banner.jpg').resize(
    width=1200,
    height=400,
    keep_aspect=False
)

# Create thumbnail
Path('photo.jpg').resize(
    max_size=300,
    output_path='thumb.jpg',
    quality=85
)

# Quick thumbnail
Path('photo.jpg').thumbnail()  # photo_thumb.jpg (256px max)

# Small square thumbnail
Path('image.png').thumbnail(size=128, square=True)

# Custom output
Path('photo.jpg').thumbnail(
    size=200,
    output_path='thumbnails/photo_small.jpg'
)

# PNG to JPEG
Path('transparent.png').convert_format('jpg')

# JPEG to WebP (smaller file size)
Path('photo.jpg').convert_format('webp', quality=80)

# Any to PNG (lossless)
Path('image.bmp').convert_format('png')

# JPEG to PNG (preserve transparency)
Path('logo.jpg').convert_format('png')

# Batch resize
for img in Path('photos').find_files('*.jpg'):
    img.resize(max_size=1920, output_path=f'resized/{img.name}')

# Create thumbnails for all images
for img in Path('.').find_files('*.png'):
    img.thumbnail(size=256)

# Convert all PNG to WebP
for png in Path('images').find_files('*.png'):
    png.convert_format('webp', quality=85)
```