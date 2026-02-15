#!/usr/bin/env python3
"""
Utility script to move files from one folder to another using Git.

This script ensures that file history is preserved by using 'git mv' command.
It also creates destination directories if they don't exist.

Usage:
    python move_files.py <source_path> <destination_path>

Example:
    python move_files.py "Experiment 1/data.csv" "Experiment 2/data.csv"
"""

import os
import sys
import subprocess
from pathlib import Path


def move_file(source, destination):
    """
    Move a file from source to destination using git mv.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Convert to Path objects
    source_path = Path(source)
    dest_path = Path(destination)
    
    # Check if source file exists
    if not source_path.exists():
        print(f"❌ Error: Source file '{source}' does not exist.")
        return False
    
    # Check if source is a file (not a directory)
    if not source_path.is_file():
        print(f"❌ Error: '{source}' is not a file.")
        return False
    
    # Create destination directory if it doesn't exist
    dest_dir = dest_path.parent
    if not dest_dir.exists():
        print(f"📁 Creating destination directory: {dest_dir}")
        dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if destination file already exists
    if dest_path.exists():
        response = input(f"⚠️  Destination file '{destination}' already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("❌ Operation cancelled.")
            return False
    
    try:
        # Use git mv to preserve history
        print(f"🔄 Moving '{source}' to '{destination}'...")
        result = subprocess.run(
            ['git', 'mv', str(source), str(destination)],
            capture_output=True,
            text=True,
            check=True
        )
        
        print("✅ File moved successfully!")
        print(f"   From: {source}")
        print(f"   To:   {destination}")
        print("\n💡 Don't forget to commit the change:")
        print(f"   git commit -m \"Move {source_path.name} to {dest_dir}\"")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error moving file: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python move_files.py <source_path> <destination_path>")
        print("\nExample:")
        print('  python move_files.py "Experiment 1/data.csv" "Experiment 2/data.csv"')
        sys.exit(1)
    
    source = sys.argv[1]
    destination = sys.argv[2]
    
    print("=" * 60)
    print("File Movement Utility")
    print("=" * 60)
    
    success = move_file(source, destination)
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
