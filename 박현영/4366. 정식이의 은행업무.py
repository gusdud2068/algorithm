T= int(input())

for tc in range(1,1+T):
    jinsoo2 = list(input())
    jinsoo3= list(input())

    change2=[]
    for i in range(len(jinsoo2)):
        hap=0
        if jinsoo2[i] == "1":
            jinsoo2[i]="0"
            for j in range(len(jinsoo2)):
                hap+=int(jinsoo2[-j-1])*(2**j)
            change2.append(hap)
            jinsoo2[i]="1"
        elif jinsoo2[i] == "0":
            jinsoo2[i] = "1"
            for j in range(len(jinsoo2)):
                hap += int(jinsoo2[-j-1])*(2 ** j)
            change2.append(hap)
            jinsoo2[i] = "0"
    change3=[]
    for k in range(len(jinsoo3)):
        hap=0
        if jinsoo3[k] == "2":
            jinsoo3[k] = "0"
            for l in range(len(jinsoo3)):
                hap+=int(jinsoo3[-l-1])*(3**l)
            change3.append(hap)
            hap=0
            jinsoo3[k] = "1"
            for l in range(len(jinsoo3)):
                hap += int(jinsoo3[-l - 1]) * (3 ** l)
            change3.append(hap)
            jinsoo3[k] = "2"

        elif jinsoo3[k] == "1":
            jinsoo3[k] = "0"
            for l in range(len(jinsoo3)):
                hap += int(jinsoo3[-l - 1]) * (3 ** l)
            change3.append(hap)
            hap = 0
            jinsoo3[k] = "2"
            for l in range(len(jinsoo3)):
                hap += int(jinsoo3[-l - 1]) * (3 ** l)
            change3.append(hap)
            jinsoo3[k] = "1"

        elif jinsoo3[k] == "0":
            jinsoo3[k] = "1"
            for l in range(len(jinsoo3)):
                hap += int(jinsoo3[-l - 1]) * (3 ** l)
            change3.append(hap)
            hap = 0
            jinsoo3[k] = "2"
            for l in range(len(jinsoo3)):
                hap += int(jinsoo3[-l - 1]) * (3 ** l)
            change3.append(hap)
            jinsoo3[k] = "0"

    for m in change3:
        for k in change2:
            if m==k:
                ans=m
    print(f"#{tc} {ans}")