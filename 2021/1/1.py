with open("input.txt", 'r') as f:
    a = [int(i.rstrip()) for i in f.readlines()]

counter = 0
for i in range(0, len(a)-1):
    if a[i+1] > a[i]:
        counter +=1
print(1, counter)

counter=0
for i in range(0, len(a)-3):
    window1 = a[i] +a[i+1] + a[i+2]
    window2 = a[i+1] + a[i+2] + a[i+3]
    if window2 > window1:
        counter+=1
print(2, counter)

