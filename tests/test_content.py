#!/usr/bin/env python3

# File: tests/test_content.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2025-12-31
# Description: Test content operations
# License: MIT

"""
Test content operations
"""
import pytest
import json
import pickle
from pathlib3 import Path


class TestContentOperations:
    """Test content reading/writing operations"""
    
    def test_lines(self, tmp_path):
        """Test reading lines"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("line1\nline2\nline3\n")
        
        lines = file_path.lines()
        assert lines == ["line1", "line2", "line3", ""]
        
        # Test with strip
        lines_stripped = file_path.lines(strip=True)
        assert lines_stripped == ["line1", "line2", "line3", ""]
    
    def test_lines_with_whitespace(self, tmp_path):
        """Test lines with whitespace handling"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("  line1  \n  line2  \n")
        
        lines = file_path.lines(strip=False)
        assert lines == ["  line1  ", "  line2  ", ""]
        
        lines_stripped = file_path.lines(strip=True)
        assert lines_stripped == ["line1", "line2", ""]
    
    def test_read_json(self, tmp_path):
        """Test JSON reading"""
        file_path = Path(tmp_path) / "data.json"
        data = {"key": "value", "number": 42, "list": [1, 2, 3]}
        
        file_path.write_text(json.dumps(data))
        
        read_data = file_path.read_json()
        assert read_data == data
    
    def test_write_json(self, tmp_path):
        """Test JSON writing"""
        file_path = Path(tmp_path) / "data.json"
        data = {"key": "value", "number": 42}
        
        file_path.write_json(data)
        
        assert file_path.exists()
        read_data = json.loads(file_path.read_text())
        assert read_data == data
    
    def test_write_json_with_indent(self, tmp_path):
        """Test JSON writing with custom indent"""
        file_path = Path(tmp_path) / "data.json"
        data = {"key": "value"}
        
        file_path.write_json(data, indent=4)
        
        content = file_path.read_text()
        assert "    " in content  # Should have 4-space indent
    
    def test_read_pickle(self, tmp_path):
        """Test pickle reading"""
        file_path = Path(tmp_path) / "data.pkl"
        data = {"key": "value", "number": 42, "list": [1, 2, 3]}
        
        file_path.write_bytes(pickle.dumps(data))
        
        read_data = file_path.read_pickle()
        assert read_data == data
    
    def test_write_pickle(self, tmp_path):
        """Test pickle writing"""
        file_path = Path(tmp_path) / "data.pkl"
        data = {"key": "value", "number": 42}
        
        file_path.write_pickle(data)
        
        assert file_path.exists()
        read_data = pickle.loads(file_path.read_bytes())
        assert read_data == data
    
    def test_hash_sha256(self, tmp_path):
        """Test SHA256 hashing"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("hello world")
        
        hash_value = file_path.hash()
        assert len(hash_value) == 64  # SHA256 produces 64 hex characters
        
        # Same content should produce same hash
        file_path2 = Path(tmp_path) / "file2.txt"
        file_path2.write_text("hello world")
        assert file_path.hash() == file_path2.hash()
    
    def test_hash_md5(self, tmp_path):
        """Test MD5 hashing"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("hello world")
        
        hash_value = file_path.hash("md5")
        assert len(hash_value) == 32  # MD5 produces 32 hex characters
    
    def test_checksum_alias(self, tmp_path):
        """Test checksum as alias for hash"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("hello world")
        
        assert file_path.checksum() == file_path.hash()
    
    def test_count_lines(self, tmp_path):
        """Test line counting"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("line1\nline2\nline3\n")
        
        count = file_path.count_lines()
        assert count == 4  # 3 lines + 1 empty line at end


class TestSearchAndFilter:
    """Test search and filter operations"""
    
    def test_find_files(self, tmp_path):
        """Test finding files"""
        # Create test structure
        (Path(tmp_path) / "file1.txt").touch()
        (Path(tmp_path) / "file2.py").touch()
        (Path(tmp_path) / "sub").mkdir()
        (Path(tmp_path) / "sub" / "file3.txt").touch()
        (Path(tmp_path) / "sub" / "dir").mkdir()
        
        # Find all txt files
        txt_files = Path(tmp_path).find_files("*.txt")
        assert len(txt_files) == 2
        
        # Find all files
        all_files = Path(tmp_path).find_files()
        assert len(all_files) == 3
    
    def test_find_dirs(self, tmp_path):
        """Test finding directories"""
        # Create test structure
        (Path(tmp_path) / "dir1").mkdir()
        (Path(tmp_path) / "dir2").mkdir()
        (Path(tmp_path) / "file.txt").touch()
        (Path(tmp_path) / "dir1" / "subdir").mkdir()
        
        # Find all directories
        dirs = Path(tmp_path).find_dirs()
        assert len(dirs) == 3
        
        # Find specific directories
        subdirs = Path(tmp_path).find_dirs("sub*")
        assert len(subdirs) == 1
    
    def test_walk(self, tmp_path):
        """Test directory walking"""
        # Create test structure
        (Path(tmp_path) / "file1.txt").touch()
        (Path(tmp_path) / "sub").mkdir()
        (Path(tmp_path) / "sub" / "file2.txt").touch()
        
        # Walk the tree
        walked = list(Path(tmp_path).walk())
        assert len(walked) >= 2  # At least root and sub directory
        
        # Check structure
        root_walk = walked[0]
        assert root_walk[0] == Path(tmp_path)
        assert "sub" in root_walk[1]  # subdirectories
        assert "file1.txt" in root_walk[2]  # files


class TestComparison:
    """Test comparison operations"""
    
    def test_same_content_identical(self, tmp_path):
        """Test same content detection for identical files"""
        file1 = Path(tmp_path) / "file1.txt"
        file2 = Path(tmp_path) / "file2.txt"
        
        content = "hello world"
        file1.write_text(content)
        file2.write_text(content)
        
        assert file1.same_content(file2)
    
    def test_same_content_different(self, tmp_path):
        """Test same content detection for different files"""
        file1 = Path(tmp_path) / "file1.txt"
        file2 = Path(tmp_path) / "file2.txt"
        
        file1.write_text("hello")
        file2.write_text("world")
        
        assert not file1.same_content(file2)
    
    def test_same_content_different_size(self, tmp_path):
        """Test same content with different sizes (optimization)"""
        file1 = Path(tmp_path) / "file1.txt"
        file2 = Path(tmp_path) / "file2.txt"
        
        file1.write_text("short")
        file2.write_text("much longer content")
        
        # Should return False quickly without computing hashes
        assert not file1.same_content(file2)