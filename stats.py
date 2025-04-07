
import sys


def get_num_words(book_path):
    with open (book_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words),"words found in the document")




def count_characters(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.lower()
        char_count = {}
        for char in words:
             if char in char_count:
                 char_count[char] += 1
             else:
                char_count[char] = 1
    print(char_count,"Characters found")
    return char_count
    



# Function to sort our count character function
def sort_chars(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.lower()
        char_count = {}
        for char in words:
             if char in char_count:
                 char_count[char] += 1
             else:
                char_count[char] = 1
        
        sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_chars
    


   # Lets bring our sys.argv into the function

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]  # Get the book path from command line arguments
    get_num_words(book_path) 
    sorted_characters = sort_chars(book_path)

    for char, count in sorted_characters:
        print(f"{char}: {count}")








