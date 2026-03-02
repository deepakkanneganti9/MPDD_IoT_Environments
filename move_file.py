#!/usr/bin/env python3
"""
File Moving Utility for MPDD IoT Environments
This script helps move files from one folder to another within the repository.
"""

import os
import shutil
import argparse
import sys


def move_file(source_path, destination_path, create_dirs=False, force=False):
    """
    Move a file from source path to destination path.
    
    Args:
        source_path (str): Path to the source file
        destination_path (str): Path to the destination (file or directory)
        create_dirs (bool): Whether to create destination directories if they don't exist
        force (bool): Force overwrite without confirmation
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if source file exists
        if not os.path.exists(source_path):
            print(f"Error: Source file '{source_path}' does not exist.")
            return False
        
        # Check if source is a file
        if not os.path.isfile(source_path):
            print(f"Error: Source path '{source_path}' is not a file.")
            return False
        
        # If destination is a directory, append the filename
        if os.path.isdir(destination_path):
            filename = os.path.basename(source_path)
            destination_path = os.path.join(destination_path, filename)
        
        # Create destination directories if requested
        dest_dir = os.path.dirname(destination_path)
        if dest_dir and not os.path.exists(dest_dir):
            if create_dirs:
                os.makedirs(dest_dir, exist_ok=True)
                print(f"Created directory: {dest_dir}")
            else:
                print(f"Error: Destination directory '{dest_dir}' does not exist.")
                print("Use --create-dirs flag to create it automatically.")
                return False
        
        # Check if destination file already exists (only check files, not directories)
        if os.path.exists(destination_path) and os.path.isfile(destination_path):
            if not force:
                response = input(f"File '{destination_path}' already exists. Overwrite? (y/n): ")
                if response.lower() != 'y':
                    print("Operation cancelled.")
                    return False
            # If force is True, the file will be overwritten automatically by shutil.move
        
        # Move the file
        shutil.move(source_path, destination_path)
        print(f"Successfully moved '{source_path}' to '{destination_path}'")
        return True
        
    except Exception as e:
        print(f"Error moving file: {str(e)}")
        return False


def main():
    """Main function to handle command-line arguments and execute file move."""
    parser = argparse.ArgumentParser(
        description='Move files from one folder to another within the repository',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Move a file to a different folder
  python move_file.py "Experiment 1/file.txt" "Experiment 2/file.txt"
  
  # Move a file to an existing folder (keeps same filename)
  python move_file.py "Experiment 1/file.txt" "Experiment 2/"
  
  # Move a file and create destination folders if they don't exist
  python move_file.py "Experiment 1/file.txt" "Experiment 3/subfolder/" --create-dirs
        """
    )
    
    parser.add_argument(
        'source',
        help='Path to the source file to move'
    )
    
    parser.add_argument(
        'destination',
        help='Path to the destination (file or directory)'
    )
    
    parser.add_argument(
        '--create-dirs',
        action='store_true',
        help='Create destination directories if they do not exist'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force overwrite without confirmation'
    )
    
    args = parser.parse_args()
    
    # Check if source file exists before doing anything
    if not os.path.exists(args.source):
        print(f"Error: Source file '{args.source}' does not exist.")
        sys.exit(1)
    
    # Handle force flag - remove destination file if it exists
    if args.force:
        if os.path.isdir(args.destination):
            dest_file = os.path.join(args.destination, os.path.basename(args.source))
        else:
            dest_file = args.destination
        
        if os.path.exists(dest_file) and os.path.isfile(dest_file):
            try:
                os.remove(dest_file)
                print(f"Removed existing file: {dest_file}")
            except FileNotFoundError:
                # File was already removed by another process, that's okay
                pass
            except Exception as e:
                print(f"Error removing existing file: {e}")
                sys.exit(1)
    
    # Execute the move operation
    success = move_file(args.source, args.destination, args.create_dirs, args.force)
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
