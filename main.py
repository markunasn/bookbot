def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(word_count(text))
      

def read_book(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)
main()