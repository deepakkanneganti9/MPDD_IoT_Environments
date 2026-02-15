# MPDD IoT Environments

This repository contains experiments and datasets for MPDD (Multi-Protocol Data Distribution) in IoT environments.

## Repository Structure

- `Experiment 1/` - Contains the first experiment with Airline Dataset

## How to Move Files Between Folders

There are several ways to move files from one folder to another in this repository:

### Method 1: Using Git Command Line

To move a file while preserving its Git history:

```bash
# Move a single file
git mv "source/folder/filename.ext" "destination/folder/filename.ext"

# Commit the change
git commit -m "Move filename.ext to destination folder"
```

**Example:**
```bash
git mv "Experiment 1/data.csv" "Experiment 2/data.csv"
git commit -m "Move data.csv to Experiment 2"
```

### Method 2: Using the Provided Python Utility

We provide a Python utility script `move_files.py` that makes it easy to move files:

```bash
python move_files.py "source/path/file.ext" "destination/path/file.ext"

# For automation (skip confirmation prompts)
python move_files.py "source/path/file.ext" "destination/path/file.ext" --force
```

The script will:
- Create the destination directory if it doesn't exist
- Move the file using Git to preserve history
- Show you the status of the operation
- Prompt for confirmation if destination file exists (unless --force is used)

**Example:**
```bash
python move_files.py "Experiment 1/notebook.ipynb" "Experiment 2/notebook.ipynb"

# Non-interactive mode for scripts
python move_files.py "old/data.csv" "new/data.csv" --force
```

### Method 3: Manual Move with Git Add

If you've already moved files manually:

```bash
# Let Git know about the move
git add -A

# Git will detect the rename/move automatically
git commit -m "Reorganize files"
```

## Creating New Folders

To create a new folder structure:

```bash
mkdir -p "New Folder Name"
git mv "old/location/file.ext" "New Folder Name/file.ext"
git commit -m "Move file to new folder"
```

## Best Practices

1. **Always use `git mv`** instead of regular `mv` to preserve file history
2. **Commit moves separately** from content changes for clearer history
3. **Use descriptive commit messages** that explain what was moved and why
4. **Create destination folders first** if using manual operations
5. **Check git status** after moving to ensure everything is tracked correctly

## Tips

- You can move multiple files in one commit
- Use quotes around folder/file names with spaces
- The Python utility handles spaces in names automatically
- Moving files preserves their entire Git history
