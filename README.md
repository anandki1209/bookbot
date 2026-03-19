# BookBot

**BookBot** is a Python-based text analysis tool that reads book files and provides detailed statistical insights about the text. It was created as a Boot.dev project to learn Python fundamentals.

## Features

- **Word Count**: Calculates the total number of words in a book
- **Character Frequency Analysis**: Counts the occurrence of each character in the text
- **Sorted Statistics**: Displays character frequencies sorted from most to least frequent
- **Alphabetic Filtering**: Shows only alphabetic characters in the frequency report (ignores numbers and special characters)

## Project Structure

```
bookbot/
├── main.py          # Main entry point and book text processor
├── stats.py         # Statistical analysis functions
└── README.md        # Project documentation
```

## How It Works

### main.py
The main script orchestrates the analysis:
- Takes a file path as a command-line argument
- Reads the book content from the specified file
- Calculates total word count
- Analyzes character frequency
- Displays results in a formatted report

### stats.py
Contains utility functions for statistical analysis:
- `get_num_words(text)`: Counts the total number of words in text
- `count_occurence(text)`: Creates a frequency dictionary for all characters (case-insensitive)
- `sort_dict(items)`: Converts frequency dictionary to a sorted list ordered by frequency (highest first)

## Usage

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Output

The program displays a formatted report:
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 77325 total words
--------- Character Count -------
e: 11602
t: 8996
a: 8433
o: 8018
i: 7528
n: 7328
...
============= END ===============
```

## Requirements

- Python 3.x
- A text file containing the book content

## Learning Outcomes

This project demonstrates:
- Python file I/O operations
- String manipulation and text processing
- Dictionary and list data structures
- Function decomposition and modularity
- Command-line argument handling
- Data sorting and filtering

## Author

Created as a learning project on [Boot.dev](https://www.boot.dev)