def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(word_count(text))
    print(char_count(text))
      

def read_book(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    counts = {}
    text = book.lower()
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

main()
