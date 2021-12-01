file = open("number.txt", "r")
getallen =[]
for line in file:
    getal = int(line.strip())
    getallen.append(int(getal))

count_larger = 0
count_smaller = 0
count_same = 0
som1 = 0
som2 = 0
i = 0
for i in range(len(getallen)-3):
    som1 = getallen[i] + getallen[i + 1] + getallen[i + 2]
    som2 = getallen[i + 1] + getallen[i + 2] + getallen[i + 3]

    if som2 > som1:
        count_larger +=1
    elif som2 < som1:
        count_smaller +=1
    elif som1 == som2:
        count_same +=1

print("groter: " + str(count_larger))
print("kleiner: " + str(count_smaller))
print("gelijk: " + str(count_same))
