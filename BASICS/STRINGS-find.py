s = "welcome to upgrade. It is a pleasure to welcome you to Bangalore. welcome to the course. I heartily welcome you"
l = s.split(" ")
count = 0
for i in range(len(l)):
    if l[i] in ('welcome') :
        count = count + 1
print (count)
