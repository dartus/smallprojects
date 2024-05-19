num = input("Enter a large number and I will add commas to separate the thousands, enter end to stop program")
def format_number(num):
    while num.lower() != 'end':
        try: 
            int(num)
        except ValueError:
            print("Please enter a valid number")
        else:
            str(num)
            x = num.split()
            print(x)

