n = int(input("Enter No. of days: "))

input_string = input("Enter the temps of each day with space ")

list  = input_string.split()
a = int(list[1])

for i in range(len(list)):
    if int(list[i]) <= 15:
       print ('cooler')
    if int(list[i]) > 15:
       print ('heater')

