def main(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        word_count = count_words(file_contents)
        char_occurances = num_characters(file_contents)
        print_report(file_path, word_count, char_occurances)

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
def print_report(file_path, word_count, char_occurrences): 
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Create a sorted dictionary of characters and their counts
    sorted_char_occurrences = sorted(char_occurrences.items(), key = lambda item: item[1], reverse = True)
    
    for char, count in sorted_char_occurrences:
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report of {file_path} ---")

if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    main(file_path)