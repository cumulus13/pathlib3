# pathlib3 Documentation

Welcome to **pathlib3** - an extended version of Python's `pathlib` with 40+ additional utility methods!

## What is pathlib3?

`pathlib3` extends Python's standard `pathlib.Path` class with convenient utility methods for common file and directory operations. It maintains 100% backward compatibility with `pathlib.Path` while adding powerful new features.

## Key Features

- ✅ **100% Compatible** with `pathlib.Path`
- ✅ **40+ New Methods** for file operations
- ✅ **Type Hints** for better IDE support
- ✅ **Method Chaining** support
- ✅ **Zero Dependencies** (only standard library)
- ✅ **Well Documented** with examples

## Quick Start

```python
from pathlib3 import Path

# Use all standard pathlib.Path methods
p = Path("myfile.txt")
p.exists()          # Standard pathlib
p.read_text()       # Standard pathlib

# Plus 40+ new methods!
p.ext()                    # "txt"
p.size_human()             # "1.5 KB"
p.ensure_parent().touch()  # Create parent dirs and file
p.copy_to("backup.txt")    # Copy file
```

## Installation

```bash
pip install pathlib3
```

## Documentation Contents

```{toctree}
:maxdepth: 2

quick_start
api
examples
```

## Support

- **GitHub**: [github.com/cumulus13/pathlib3](https://github.com/cumulus13/pathlib3)
- **Issues**: [GitHub Issues](https://github.com/cumulus13/pathlib3/issues)
- **PyPI**: [pypi.org/project/pathlib3](https://pypi.org/project/pathlib3)

## License

MIT License - see [LICENSE](LICENSE) file for details.