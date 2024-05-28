num = input("Enter a large number and I will add commas to separate the thousands, enter end to stop program")
def format_number(number):
   
     # newnum = number[:4] + ',' + number[4:]
     # print(newnum) 
     #for i in range(len(number)):
     if number[0] != '0':
          number = number[:1] + ',' + number[1:]
          print(number)
          for i in range (len(number)):
               if number[i] == ',':
                    number = number[:i+4] + ',' + number[i+4:]
          print(number)
               
      

format_number(num)