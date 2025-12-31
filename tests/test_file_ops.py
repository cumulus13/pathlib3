#!/usr/bin/env python3

# File: tests/test_file_ops.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2025-12-31
# Description: Test file operations
# License: MIT

"""
Test file operations
"""
import pytest
from pathlib3 import Path


class TestDirectoryOperations:
    """Test directory operations"""
    
    def test_ensure_dir(self, tmp_path):
        """Test directory creation"""
        new_dir = Path(tmp_path) / "new" / "nested" / "dir"
        new_dir.ensure_dir()
        assert new_dir.exists()
        assert new_dir.is_dir()
    
    def test_ensure_parent(self, tmp_path):
        """Test parent directory creation"""
        file_path = Path(tmp_path) / "new" / "nested" / "file.txt"
        file_path.ensure_parent()
        assert file_path.parent.exists()
        assert file_path.parent.is_dir()
    
    def test_touch_parent(self, tmp_path):
        """Test touch with parent creation"""
        file_path = Path(tmp_path) / "new" / "file.txt"
        file_path.touch_parent()
        assert file_path.exists()
        assert file_path.is_file()
    
    def test_ls(self, tmp_path):
        """Test directory listing"""
        # Create test files
        (Path(tmp_path) / "file1.txt").touch()
        (Path(tmp_path) / "file2.txt").touch()
        (Path(tmp_path) / "file3.py").touch()
        (Path(tmp_path) / "subdir").mkdir()
        
        # Test listing all
        all_items = Path(tmp_path).ls()
        assert len(all_items) == 4
        
        # Test pattern matching
        txt_files = Path(tmp_path).ls("*.txt")
        assert len(txt_files) == 2
        
        # Test only files
        files = Path(tmp_path).ls(only_files=True)
        assert len(files) == 3
        
        # Test only directories
        dirs = Path(tmp_path).ls(only_dirs=True)
        assert len(dirs) == 1
    
    def test_find(self, tmp_path):
        """Test recursive find"""
        # Create nested structure
        (Path(tmp_path) / "file1.txt").touch()
        (Path(tmp_path) / "sub").mkdir()
        (Path(tmp_path) / "sub" / "file2.txt").touch()
        
        # Find all txt files
        txt_files = Path(tmp_path).find("*.txt")
        assert len(txt_files) == 2
    
    def test_tree(self, tmp_path):
        """Test directory tree generation"""
        # Create structure
        (Path(tmp_path) / "file.txt").touch()
        (Path(tmp_path) / "sub").mkdir()
        (Path(tmp_path) / "sub" / "nested.txt").touch()
        
        # Generate tree
        tree = Path(tmp_path).tree(max_depth=2)
        assert "file.txt" in tree
        assert "sub" in tree


class TestFileOperations:
    """Test file operations"""
    
    def test_copy_to(self, tmp_path):
        """Test file copying"""
        src = Path(tmp_path) / "source.txt"
        dst = Path(tmp_path) / "dest.txt"
        
        src.write_text("content")
        result = src.copy_to(dst)
        
        assert dst.exists()
        assert dst.read_text() == "content"
        assert result == dst
    
    def test_move_to(self, tmp_path):
        """Test file moving"""
        src = Path(tmp_path) / "source.txt"
        dst = Path(tmp_path) / "dest.txt"
        
        src.write_text("content")
        result = src.move_to(dst)
        
        assert not src.exists()
        assert dst.exists()
        assert dst.read_text() == "content"
    
    def test_rm_file(self, tmp_path):
        """Test file removal"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.touch()
        
        file_path.rm()
        assert not file_path.exists()
    
    def test_rm_directory(self, tmp_path):
        """Test directory removal"""
        dir_path = Path(tmp_path) / "dir"
        dir_path.mkdir()
        (dir_path / "file.txt").touch()
        
        dir_path.rm(recursive=True)
        assert not dir_path.exists()
    
    def test_rm_missing_ok(self, tmp_path):
        """Test rm with missing_ok"""
        file_path = Path(tmp_path) / "nonexistent.txt"
        
        # Should not raise error
        file_path.rm(missing_ok=True)
        
        # Should raise error
        with pytest.raises(FileNotFoundError):
            file_path.rm(missing_ok=False)
    
    def test_append_text(self, tmp_path):
        """Test text appending"""
        file_path = Path(tmp_path) / "file.txt"
        
        file_path.write_text("line1\n")
        file_path.append_text("line2\n")
        file_path.append_text("line3\n")
        
        content = file_path.read_text()
        assert content == "line1\nline2\nline3\n"
    
    def test_append_bytes(self, tmp_path):
        """Test bytes appending"""
        file_path = Path(tmp_path) / "file.bin"
        
        file_path.write_bytes(b'\x00\x01')
        file_path.append_bytes(b'\x02\x03')
        
        content = file_path.read_bytes()
        assert content == b'\x00\x01\x02\x03'
    
    def test_backup(self, tmp_path):
        """Test backup creation"""
        file_path = Path(tmp_path) / "important.txt"
        file_path.write_text("important content")
        
        backup_path = file_path.backup()
        
        assert backup_path.exists()
        assert backup_path.name == "important.txt.bak"
        assert backup_path.read_text() == "important content"


class TestFileInfo:
    """Test file information methods"""
    
    def test_size(self, tmp_path):
        """Test file size"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_text("hello world")
        
        size = file_path.size()
        assert size == 11  # "hello world" is 11 bytes
    
    def test_size_human(self, tmp_path):
        """Test human-readable size"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.write_bytes(b'\x00' * 1024)  # 1 KB
        
        size_human = file_path.size_human()
        assert "KB" in size_human or "B" in size_human
    
    def test_is_empty(self, tmp_path):
        """Test empty check"""
        file_path = Path(tmp_path) / "empty.txt"
        file_path.touch()
        
        assert file_path.is_empty()
        
        file_path.write_text("not empty")
        assert not file_path.is_empty()
    
    def test_age(self, tmp_path):
        """Test file age"""
        file_path = Path(tmp_path) / "file.txt"
        file_path.touch()
        
        age = file_path.age()
        assert age >= 0  # Should be very small
        assert age < 10  # Should be less than 10 seconds
    
    def test_comparison(self, tmp_path):
        """Test file time comparison"""
        old_file = Path(tmp_path) / "old.txt"
        old_file.touch()
        
        import time
        time.sleep(0.1)  # Ensure different timestamps
        
        new_file = Path(tmp_path) / "new.txt"
        new_file.touch()
        
        assert new_file.is_newer_than(old_file)
        assert old_file.is_older_than(new_file)