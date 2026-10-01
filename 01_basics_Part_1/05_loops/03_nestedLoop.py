#  nested loop

for i in range (10) :
    for j in range (5):
        print("hello world")



# break continue always apply to nearest or ineer for loop

for i in range (4) :
    for j in range (1,13):
        if j%4 == 0:
            break
        print(j)