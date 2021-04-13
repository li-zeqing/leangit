#以1个月为一个周期，连续学习10天能力值不变,从第11天开始至第30天每天能力增长N
#对于不同的N，当连续学习360天后能力值（年终值）是多少
def dayUp(N):
    dayup = 1.0
    for j in range(12):
        for i in range(30):
            if i >=10 :
                dayup = dayup *(1+N)
            else:
                pass
    return dayup
dayfactor = (0.01,0.02,0.04,0.06,0.08,0.1)
print(len(dayfactor))
for i in range(len(dayfactor)):
    print("N=",dayfactor[i])
    print("年终值：",dayUp(dayfactor[i]))
