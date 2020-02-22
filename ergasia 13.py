def luhn(card_number):
    tl=list(str(card_number))
    ml=[]
    l1 = tl[-2::-2]
    l2= tl[::-2]
    l2 = [int (n) for n in l2]
    ml=[int(n) for n in l1]
    l1 = [int(n)*2 for n in l1]
    tl=l1

    for x in l1:
        sum1=0
        if x>9:
            idx = l1.index(x)
            tl.pop(idx)
            while el:
                y = x%10
                sum1+=y
                x = x//10 
            tl.insert(idx, sum1)
    l1_sum=sum(tl)
    l2_sum = sum(l2)
    final_sum = l1_sum+ l2_sum
    if final_sum%10==0:
        return True
    return False

card_number= input("dwse arithmo kartas: ")
result=luhn(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
