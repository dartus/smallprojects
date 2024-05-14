zerostring = input("Enter a binary number")

def consecutive_zeroes(binary1):
    zerocount = 0
    binarylength = len(binary1)
    for i in range (binarylength+1):
        if binary1[i] == "0":
            if binary1[i] == binary1[i + 1]:
                zerocount = zerocount + 1

consecutive_zeroes(zerostring)





