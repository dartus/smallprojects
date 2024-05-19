zerostring = input("Enter a binary number")

def consecutive_zeroes(binary1):
    zerocount = 0
    result = 0
    binarylength = len(binary1)
    for i in range (binarylength): #so the code will go into this for loop
        if binary1[i] == "0": #when a zero is found zerocount is incrimented 
            zerocount += 1
        else: #if no zero count then zerocount is zero
            zerocount = 0
        result = max(result, zerocount) #LAST step of the for loop so it has to do this everytime. Checks whether result or zerocount is higher. 
        #Whatever is higher becomes RESULT. So if result is 4 next time it may check whether zerocount which is 3 is higher. That way we can check the longest sequence of consecutive numbers.
    print(result) 
    
        
        
   
    
consecutive_zeroes(zerostring)





