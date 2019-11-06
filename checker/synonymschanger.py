from PyDictionary import PyDictionary
import nltk
import random


def get_input(input_filename):
    with open(input_filename, 'r') as f:
        file_contents = f.readlines()
    return file_contents  # returns lines of file as a list of strings


def convert(lines):
    new_lines = []
    dictionary = PyDictionary()
    for line in lines:
        pos = nltk.pos_tag(nltk.word_tokenize(line))  # assign parts of speech to words in the line
        new_line = line
        for word, part in pos:
            if part in ['JJ',  
                        'JJR',
                        'JJS',
                        'RB',  
                        'RBR',
                        'RBS']:
                try:
                    synonyms = dictionary.synonym(word)
                    synonym = random.choice(synonyms)  # chose a random synonym to replace word
                    if word[0].isupper():  # format new word as it appears in the original text
                        synonym = synonym.capitalize()
                    new_line = new_line.replace(word, synonym, 1)
                except TypeError:
                    pass
        new_lines.append(new_line)
    return new_lines


def main():
    text = "He is so small"
    new_text = convert(text)
    print(''.join(new_text))


if __name__ == "__main__":
    main()