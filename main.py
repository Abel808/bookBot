

def main ():
    link = 'books/frankenstein.txt'
    txt = open_book(link)
    print(word_count(txt))

def open_book(path):
    with open(path) as f:
        contents = f.read()
        return contents

def word_count(txt):
    total_words = 0
    str_arr= txt.split()
    
    total_words = len(str_arr)
    # for char in str_arr:
    #     if char == type('string'):
    #         total_words +=1

    return total_words

main ()