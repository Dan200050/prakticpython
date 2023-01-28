print('Vvedite cheslitel i znamenatel 1 droby')
ches1 = int(input())
znam1 = int(input())
print('Vvedite cheslitel i znamenatel 2 droby')
ches2 = int(input())
znam2 = int(input())
obk = int()
obd = int()
otv = int()
for i in range(1, znam1 * znam2):
    if znam1 < znam2:
        if znam1 * i % znam2 == 0:
            obk = znam1 * i
            ches1 = ches1 * (obk // znam1)
            ches2 = ches2 * (obk // znam2)
            otv = abs(ches1 - ches2)
            if obk % otv == 0:
                obk = obk // otv
                otv = otv // otv
                break
            else:
                obd1 = otv
                while obk % obd1 != 0:
                    obd1 = obk % obd1
                    obd = obd1
            otv = otv // obd
            obk = obk // obd
            break
    else:
        if znam2 * i % znam1 == 0:
            obk = znam2 * i
            ches1 = ches1 * (obk // znam1)
            ches2 = ches2 * (obk // znam2)
            otv = abs(ches1 - ches2)
            if obk % otv == 0:
                obk = obk // otv
                otv = otv // otv
                break
            else:
                obd1 = otv
                while obk % obd1 != 0:
                    obd1 = obk % obd1
                obd = obd1
            otv = otv // obd
            obk = obk // obd
            break
print(otv, '/', obk, sep='')
