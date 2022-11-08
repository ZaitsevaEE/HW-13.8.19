bil=int(input("Сколько билетов хотите приобрести?"))
sum_price=0
for i in range(1,bil+1):
    vozr=int(input("Сколько лет посетителю?"))
    if vozr<18:
        sum_price +=0
    elif 18<=vozr<=25:
        sum_price +=990
    else:
        sum_price +=1390
if bil>3:
    print(sum_price*0.9)
else:
    print(sum_price)


