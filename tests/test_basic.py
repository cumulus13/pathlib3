#!/usr/bin/env python3

# File: tests/test_basic.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2025-12-31
# Description: Test basic utilities and path manipulation
# License: MIT

"""
Test basic utilities and path manipulation
"""
import pytest
from pathlib3 import Path


class TestBasicUtilities:
    """Test basic utility methods"""
    
    def test_ext(self):
        """Test extension extraction"""
        assert Path("file.txt").ext() == "txt"
        assert Path("file.tar.gz").ext() == "gz"
        assert Path("file").ext() == ""
        assert Path(".gitignore").ext() == ""
    
    def test_basename(self):
        """Test basename extraction"""
        assert Path("/home/user/file.txt").basename() == "file.txt"
        assert Path("file.txt").basename() == "file.txt"
    
    def test_base(self):
        """Test base name without extension"""
        assert Path("file.txt").base() == "file"
        assert Path("archive.tar.gz").base() == "archive.tar"
    
    def test_dirname(self):
        """Test directory name extraction"""
        p = Path("/home/user/file.txt")
        assert p.dirname() == "/home/user"
    
    def test_abspath(self):
        """Test absolute path"""
        p = Path("file.txt")
        abspath = p.abspath()
        assert abspath.endswith("file.txt")
        assert Path(abspath).is_absolute()


class TestPathManipulation:
    """Test path manipulation methods"""
    
    def test_join(self):
        """Test path joining"""
        p = Path("/home").join("user", "documents", "file.txt")
        assert str(p) == "/home/user/documents/file.txt"
    
    def test_split_ext(self):
        """Test extension splitting"""
        base, ext = Path("/home/user/file.txt").split_ext()
        assert base == "/home/user/file"
        assert ext == ".txt"
    
    def test_split_path(self):
        """Test path splitting"""
        parts = Path("/home/user/file.txt").split_path()
        assert "home" in parts
        assert "user" in parts
        assert "file.txt" in parts
    
    def test_change_ext(self):
        """Test extension changing"""
        p = Path("file.txt")
        assert str(p.change_ext("md")) == "file.md"
        assert str(p.change_ext(".json")) == "file.json"
    
    def test_normpath(self):
        """Test path normalization"""
        p = Path("/home//user/../user/file.txt")
        normalized = p.normpath()
        assert "//" not in str(normalized)


class TestBackwardCompatibility:
    """Test that all pathlib.Path methods still work"""
    
    def test_standard_pathlib_methods(self, tmp_path):
        """Test standard pathlib methods"""
        p = Path(tmp_path) / "test.txt"
        
        # Standard pathlib methods should work
        p.touch()
        assert p.exists()
        assert p.is_file()
        
        p.write_text("hello")
        assert p.read_text() == "hello"
        
        # Properties should work
        assert p.name == "test.txt"
        assert p.stem == "test"
        assert p.suffix == ".txt"
        assert p.parent == tmp_path