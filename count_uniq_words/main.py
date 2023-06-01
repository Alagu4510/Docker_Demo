import re

def count_unique_words(file_path):
    unique_words = set()

    with open(file_path, 'r') as file:
        for line in file:
            line = re.sub(r'\[tooltip\]', '', line)  # Remove [tooltip]
            line = re.sub(r',', '', line)  # Remove commas
            words = re.findall(r'\b\w+\b', line)
            unique_words.update(words)

    return unique_words

def write_unique_words(file_path, output_path):
    unique_words = count_unique_words(file_path)

    with open(output_path, 'w') as output_file:
        for word in unique_words:
            output_file.write(word)

def main():
    input_file = input("Enter the path to the input.txt : ")
    output_file = 'unique_words.txt'

    unique_words = count_unique_words(input_file)
    print("Count of Unique Words:", len(unique_words))

    write_unique_words(input_file, output_file)
    print("Unique Words stored in", output_file)

if __name__ == '__main__':
    main()

import re
import pytest

def check_file_extension(file_path):
    return file_path.endswith('.txt')

def test_check_file_extension():
    assert check_file_extension('sample.txt') == True
    assert check_file_extension('sample.csv') == False

def remove_tool_tip_reference(text):
    return re.sub(r'\[tooltip\]', '', text)

def test_remove_tool_tip_reference():
    assert remove_tool_tip_reference('This is a sample text file.') == 'This is a sample text file.'
    assert remove_tool_tip_reference('This is a sample text file. [tooltip]') == 'This is a sample text file.'

def remove_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def test_remove_whitespace():
    assert remove_whitespace(' This is a sample text file. ') == 'This is a sample text file.'
    assert remove_whitespace('\nThis is a\nsample text file.\n') == 'This is a sample text file.'