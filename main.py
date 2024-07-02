def main(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        word_count = count_words(file_contents)
        char_count = num_characters(file_contents)
        print_report(file, word_count, char_count)

# returns the number of words in a string
def count_words(str):
    return len(str.split())

# returns the number of times each lowercase character appears in a string
def num_characters(str):
    # Make all characters in the string lowercase
    lowered_string = str.lower()

    # Map initial ccurances of each letter to 0
    char_occurances = { 
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, 
        "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, 
        "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, 
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, 
        "y": 0, "z": 0
    }

    # Update occurances of each letter
    for char in lowered_string:
        if char in char_occurances:
            char_occurances[char] += 1

    return char_occurances

# prints a report of the word and character data to the console
def print_report(file, word_count, char_occurances):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document\n")
    
    # Create a list of characters and their counts
    char_list = [{"char": k, "num": v} for k, v in char_occurances]

    # Sort the characters by number of occurances
    char_list.sort()
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")

if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    main(file_path)