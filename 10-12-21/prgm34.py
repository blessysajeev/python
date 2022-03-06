wrd=input("enter the word:")
def word(wrd):
    wrd1 = wrd[-3:]
    if wrd1 != "ing":
        print(wrd+"ing")
    else:
        print(wrd+"ly")
word(wrd)