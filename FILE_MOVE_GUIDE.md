# File Moving Utility Guide

This repository includes a Python utility script (`move_file.py`) that helps you move files from one folder to another.

## Problem Statement

**"HOW CAN I MOVE THE FILE FROM ONE FOLDER TO THE ANOTHER"**

This utility provides a simple and safe way to move files between folders in the repository.

## Usage

### Basic Syntax

```bash
python move_file.py <source_path> <destination_path> [options]
```

### Examples

#### 1. Move a file to a different folder (with new name)

```bash
python move_file.py "Experiment 1/old_file.txt" "Experiment 2/new_file.txt"
```

#### 2. Move a file to an existing folder (keeps same filename)

```bash
python move_file.py "Experiment 1/file.txt" "Experiment 2/"
```

#### 3. Move a file and create destination folders automatically

```bash
python move_file.py "Experiment 1/file.txt" "Experiment 3/subfolder/" --create-dirs
```

#### 4. Force overwrite without confirmation

```bash
python move_file.py "Experiment 1/file.txt" "Experiment 2/file.txt" --force
```

## Command-Line Options

- `source`: Path to the source file you want to move (required)
- `destination`: Path to the destination file or folder (required)
- `--create-dirs`: Automatically create destination directories if they don't exist
- `--force`: Force overwrite existing files without asking for confirmation

## Features

✅ **Safe Operations**: 
- Checks if source file exists before moving
- Verifies source is a file (not a directory)
- Asks for confirmation before overwriting existing files

✅ **Flexible Destinations**:
- Move to a new filename in a different folder
- Move to an existing folder (keeps original filename)
- Automatically create destination folders with `--create-dirs`

✅ **User-Friendly**:
- Clear error messages
- Interactive confirmation for overwrites
- Helpful examples in `--help` output

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Getting Help

To see all available options and examples:

```bash
python move_file.py --help
```

## Common Use Cases in This Repository

### Moving experiment files between folders

```bash
# Move a notebook from Experiment 1 to Experiment 2
python move_file.py "Experiment 1/notebook.ipynb" "Experiment 2/"
```

### Reorganizing files

```bash
# Move and rename a README file
python move_file.py "Experiment 1/README" "Experiment 2/README.md"
```

### Creating new experiment folders

```bash
# Move files to a new experiment folder (create it automatically)
python move_file.py "Experiment 1/data.csv" "Experiment 3/data.csv" --create-dirs
```

## Error Handling

The script includes comprehensive error handling for common issues:

- **Source file doesn't exist**: Clear error message
- **Destination folder doesn't exist**: Option to create with `--create-dirs`
- **File already exists at destination**: Prompts for confirmation (unless `--force` is used)
- **Permission errors**: Displays the actual error message

## Alternative Methods

If you prefer to use command-line tools directly:

### Using `mv` command (Linux/Mac/Git Bash)

```bash
mv "source/file.txt" "destination/file.txt"
```

### Using Windows Command Prompt

```cmd
move "source\file.txt" "destination\file.txt"
```

### Using Git

```bash
git mv "source/file.txt" "destination/file.txt"
```

The Python utility provides additional safety checks and cross-platform compatibility compared to these alternatives.
