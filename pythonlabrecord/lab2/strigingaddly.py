def adding(word):
    if word[-3:]=="ing":
        word=word+"ly"
    else:
        word=word+"ing"
    return word





word=input("enter a word")
print(adding(word))
