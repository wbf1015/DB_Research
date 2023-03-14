import pandas as pd
import numpy as np
import csv

header = ['tid', 'attribute', 'correct_val']

org_data = pd.read_csv("energy.csv")[["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]].to_numpy()
# print(type(org_data[0]))
# l = list(org_data[0])
# print(type(l))
l = []
for i in range(0, 21):
    t = tuple(org_data[0])
    for j in range(1, 10):
        s1 = str(i)
        s2 = 'T' + str(j)
        s3 = t[j - 1]
        temp = []
        s1 = s1
        s2 = s2
        temp.append(s1)
        temp.append(s2)
        s3 = str(s3)
        temp.append(s3)
        l.append(temp)

i = 0
with open('energy_clean_5.csv', 'w',newline='') as file_obj:
    writer = csv.writer(file_obj)
    writer.writerow(header)
    for energy in l:
        writer.writerow(energy)

print('finish')
