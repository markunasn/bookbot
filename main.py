def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    #print(word_count(text))
    #print(char_count(text))
    report(text, book_path) 

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
        if char.isalpha():    
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts
def sort_on(dict):
    return dict["count"]
def convert_char_count(char_dict):
    converted = []
    for key in char_dict.keys():
        tmp = {"char" : key , "count" : char_dict[key]}
        converted.append(tmp)
    return converted
def report(book, path):
    wc = word_count(book)
    cc = convert_char_count(char_count(book))
    cc.sort(reverse=True, key = sort_on)
    
    print(f"--- Report for {path} ---")
    print(f"{wc} words found in document")
    for c in cc:
        print(f"The character {c['char']} was found {c['count']} times")
    print("--- End of Report ---")
    



main()
