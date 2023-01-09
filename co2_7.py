char=input("enter a word")
if "ing" in char:
    w=char.replace("ing","ly")
    print(w)
else:
    if "ing" not in  char:
        print(char,end="ing")


# enter a wordchase
# chaseing