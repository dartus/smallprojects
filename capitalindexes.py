string = input("Please input a word. I will return the index of the capital letters ")
indexes = []
def capitalIndexes(capitalstring):
    for i in range (len(capitalstring)):
        if ord(capitalstring[i]) >= 65 and ord(capitalstring[i])<=90: 
            indexes.append(i)
    return print(indexes)

capitalIndexes(string)
            


