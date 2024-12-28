

def main ():
    link = 'books/frankenstein.txt'
    txt = open_book(link)
    final_char_count=char_count(txt)
    sortedans = sorter(final_char_count)
    report(sortedans)

def open_book(path):
    with open(path) as f:
        contents = f.read()
        return contents

def word_count(txt):
    str_arr= txt.split()
    total_words = len(str_arr)
    return total_words

def char_count(txt):
    str_arr= txt.split()
    char_list_count = {}
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    for word in str_arr:
        current_char_list = list(word)       

        for item in current_char_list:
            char_lower_case = item.lower()
            
            for char in alphabets:
                if char == char_lower_case:
                    if char in char_list_count:
                        char_list_count[char] += 1
                    else :
                        char_list_count[char] = 1 


    return char_list_count


def sorter(list):
    ans = []
    for item in list:
        ans.append({'char':item, 'count': list[item]})

    def get_key(dict):
        return (dict['count'])
    
    ans.sort(reverse=True, key=get_key)
    return ans


def report(final_list):
    for item in final_list:
       print (f"the {item['char']} character was found {item['count']}")


main ()
# The 'e' character was found 46043 times