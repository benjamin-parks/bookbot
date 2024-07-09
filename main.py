def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    count = get_word_count(text)
    print(f"{count} words are found in the document. \n")
    let_count = get_letter_count(text)
    for letter, count in let_count.items():
        print(f"The '{letter}' character was found {count} times.")
    print("\n--- End of report ---")
    
   

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

# get count of each letter in the text
def get_letter_count(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count  
    
    
    
    
    
main()