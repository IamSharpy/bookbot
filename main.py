from stats import analyze_words, count_chars, sort_chars, num_words
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_content = f.read()
        return file_content

def main():
    # Check if we have the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line argument
    filepath = sys.argv[1]
    
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {filepath}...")
    print("---------- Word Count ----------")
    
    book_content = get_book_text(filepath)
    word_count = num_words(book_content)
    print(f"Found {word_count} total words")
    
    print("---------- Character Count ----------")
    char_counts = count_chars(book_content)
    sorted_chars = sort_chars(char_counts)
    
    # Print only alphabetical characters
    for char_info in sorted_chars:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    
    print("========== END ==========")

main()