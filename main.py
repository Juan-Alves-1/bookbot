def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = count_letters(text)
    num_each_letter = count_each_letter(text)

    for letter, count in sorted(num_each_letter.items()):
        print(f"The letter '{letter}' appears {count} times")

'''To order by descending occurrence 
    for letter, count in sorted(num_each_letter.items(), key=lambda item: item[1], reverse=True):
    print(f"The letter '{letter}' appears {count} times")'''

# Split the text into words: str.split(sep=None, maxsplit=-1)
def count_words(text):
    words = text.split()
    return len(words)

# Count only alphabetical characters
def count_letters(text):
    return sum(char.isalpha() for char in text)

def count_each_letter(text):
    counts = {}
    for char in text.lower():  # Convert text to lowercase
        if char.isalpha():  # Check if character is a letter
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts


# Open and read text for other functions work
def get_book_text(path):
    with open(path) as f:
        return f.read()

# This is the idiomatic way to call the main function in a Python script.
if __name__ == "__main__":
    main()