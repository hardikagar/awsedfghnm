def find_unique_elements(word):
    upper=set()
    lower=set()
    for(letter in word):
        if(letter>='A' && letter<='Z'):
            upper.add(letter)
        elif(letter>='a' && letter<='z'):
            lower.add(letter)
    print(upper)
    print(lower)
            
str=input("Enter String: ")            
find_unique_elements(str)   
