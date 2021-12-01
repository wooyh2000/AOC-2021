file = open("number.txt", "r")
getallen =[]
for line in file:
    getal = int(line.strip())
    getallen.append(int(getal))
count_hoger = 0
waardeVorig = 180

for waarde in getallen:

    if waarde > waardeVorig:
        count_hoger +=1
    waardeVorig = waarde
print(count_hoger)