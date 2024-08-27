
def find_most_repeated(wordstr):
    words = wordstr.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1   
            
    most_repeated_word = max(word_count, key=word_count.get)
    most_repeated_word_count = word_count[most_repeated_word]     
    return (most_repeated_word, most_repeated_word_count)

input_string = input("enter string : ")
word, word_count = find_most_repeated(input_string)
print(f"word: {word}-{word_count}")


