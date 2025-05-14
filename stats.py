def num_words(bookcontent):
    words = bookcontent.split()
    word_count = len(words)
    return word_count

def analyze_words(content):
    word_count = num_words(content)
    print(f"{word_count} words found in the document")

def count_chars(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_chars(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list