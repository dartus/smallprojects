string = input("Enter some letters and I will return the middle letter")

def mid(midstring):
    stringlen = len(midstring)
    letters = []
    middle = stringlen // 2
    if stringlen % 2 == 0:
        print(' " " ')
    else:
        print(midstring[middle])
        
    
    #for i in range(stringlen):
     #   letters.append(string[i])
    #print(letters)

mid(string)

    #midlen = len(midstring) 
    #middle = midlen // 2
   # notmid = " "
   # if midlen % 2 == 0: 
   #     print(notmid)
   # else:
   #     return midstring[middle]

#mid(string)
