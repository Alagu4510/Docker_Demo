# Unique Word Counter

This program counts the number of unique words in a text file and writes them to an output file.
It also includes some utility functions for file extension checking and text manipulation.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the files.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the program files.
4. Run the program using the command: `python unique_word_counter.py`
5. Enter the path to the input text file when prompted.
6. The program will count the number of unique words and display the result.
7. The program will also generate an output file named `unique_words.txt` containing the unique words found in the input file.
8. Build the Docker image using the command: `docker build -t word-counter .
9. Run the Docker container with the command: `docker run word-counter`

## Utility Functions

The program includes the following utility functions:

- `check_file_extension(file_path)`: Checks if a file has a `.txt` extension.
- `remove_tool_tip_reference(text)`: Removes `[tooltip]` references from a given text.
- `remove_whitespace(text)`: Removes excess whitespace from a given text.

## Testing

The program includes unit tests for the utility functions using pytest. To run the tests:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the program files.
3. Run the command: `pytest`


