in_file = open('JHH4_A2_processed.txt', 'r')
count = 0
for line in in_file:
    if line[0] == 't':
        count += 1
print(count)
