BookBot is my first project!
(I used ChatGBT to learn how to write a useful README file)

# Character Count Report

This project reads a text file and generates a report of the number of
words and the number of occurrences of each character in the file.

## Description

This Python script reads a text file, counts the number of words, and
counts the occurrences of each character (all characters are made lowercase).
It then prints a report of these counts.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/JosiahBizure/bookbot
    ```
2. Navigate to the project directory:
    ```bash
    cd your_filepath/bookbot
    ```
3. Ensure you have Python installed (the script is compatible with Python 3).

## Usage

1. Place the text file you want to analyze in the `books` directory.
2. Update the `file_path` variable in the `main` function to the path of your text file.
3. Run the script:
    ```bash
    python3 main.py
    ```

## Example Output
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24613 times
The 'n' character was found 24367 times
The 's' character was found 21155 times
The 'r' character was found 20818 times
The 'h' character was found 19725 times
The 'd' character was found 16863 times
The 'l' character was found 12739 times
The 'm' character was found 10604 times
The 'u' character was found 10407 times
The 'c' character was found 9243 times
The 'f' character was found 8731 times
The 'y' character was found 7914 times
The 'w' character was found 7638 times
The 'p' character was found 6121 times
The 'g' character was found 5974 times
The 'b' character was found 5026 times
The 'v' character was found 3833 times
The 'k' character was found 1755 times
The 'x' character was found 677 times
The 'j' character was found 504 times
The 'q' character was found 324 times
The 'z' character was found 243 times
--- End report of books/frankenstein.txt ---
