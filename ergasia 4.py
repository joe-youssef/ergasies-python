def ASCII (astring):
    number_string=[ord(x) for x in astring]
    print (number_string)
    sum1=""
    for x in number_string:
        sum1+=str(x)
    print(sum1)
    for x in range(2,int(sum1)):
        if (int(sum1) % x) == 0:
         return ("οχι πρωτος")
        else:
         return ("πρωτος")


astring=input("δωσε μια λεξη: ")
print(ASCII (astring))

