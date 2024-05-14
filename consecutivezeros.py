zerostring = input("Enter a binary number")

def consecutive_zeroes(binary1):
    zerocount = 1
    binarylength = len(binary1)
    for i in range (binarylength):
        if binary1[i] == "0":
            if binary1[i] == binary1[i - 1]:
                zerocount = zerocount + 1
            max = zerocount
        elif binary1[i] != "0":
            zerocount = 1
    if zerocount > max: 
        print(zerocount)
    else:
        print(max)

consecutive_zeroes(zerostring)





