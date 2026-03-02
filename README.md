# MPDD IoT Environments

This repository contains experiments and utilities for MPDD (Multi-Phase Data Distribution) in IoT environments.

## Repository Structure

- **Experiment 1/**: Contains the first experiment with MPDD Framework using Airline Dataset
  - `Experiment_1_MPDD_Framework_Airline_Dataset.ipynb`: Jupyter notebook for the experiment
  - `README`: Experiment documentation

## Utilities

### File Moving Utility

Need to move files between folders? We've got you covered!

The repository includes a Python utility script that makes it easy to move files from one folder to another safely and efficiently.

📖 **[View the complete File Moving Guide](FILE_MOVE_GUIDE.md)**

#### Quick Start

```bash
# Move a file to another folder
python move_file.py "source/file.txt" "destination/"

# Move and rename a file
python move_file.py "source/file.txt" "destination/newname.txt"

# Create destination folders automatically
python move_file.py "source/file.txt" "new_folder/file.txt" --create-dirs

# Force overwrite without confirmation
python move_file.py "source/file.txt" "destination/file.txt" --force
```

#### Get Help

```bash
python move_file.py --help
```

For detailed usage instructions, examples, and troubleshooting, see the [FILE_MOVE_GUIDE.md](FILE_MOVE_GUIDE.md).

## Requirements

- Python 3.6 or higher (for utilities)
- Jupyter Notebook (for running experiments)

## Getting Started

1. Clone this repository
2. Install required dependencies (if any)
3. Navigate to the experiment folder you want to work with
4. Use the file moving utility when you need to reorganize files

## Contributing

If you need help with moving files or organizing the repository, refer to the [File Moving Guide](FILE_MOVE_GUIDE.md).

## License

Please refer to the repository license for terms of use.
