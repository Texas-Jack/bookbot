# This is our main page for our project


from stats import sort_chars

import sys 


# Check for the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get file paths from command line arguments

book_path = sys.argv[1]

# Function to count words
def count_words(book_path):
    with open(book_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)
    

# Lets add a title and some text at the top of the report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
word_count = count_words(book_path)
print(f"Found {word_count} total words")
print("----------- Character Count ----------")

# Count and Sort Characters
try:
    result = sort_chars(book_path)
    for char, count in result:
        print(f"{char}: {count}")
except FileNotFoundError:
    print(f"Error: File '{book_path}' not found.")
    sys.exit(1)


# Add a footer
print("============= END ===============")




















