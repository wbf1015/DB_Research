import pandas as pd
from decimal import Decimal
import numpy as np
import csv

org_data = pd.read_csv("./repair_value/energy_repaired4.csv")[["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]].to_numpy()

'''
i 代表行索引
j 代表列索引
'''

'''
测试语句
print(len(org_data))
print(len(org_data[0]))
print(org_data[0])
print(type(org_data[0][0]))
testDouble = (Decimal(org_data[0][0]))
print(testDouble, type(testDouble))
'''

# 把所有数字值全部转换为Decimal
count = 1
for i in range(0, len(org_data)):
    for j in range(0, len(org_data[0])):
        if org_data[i][j] == '_nan_':
            count += 1
            continue
        org_data[i][j] = Decimal(org_data[i][j])

# 输出_nan_所占的数据比率
rate = Decimal(count) / Decimal(len(org_data)) * Decimal(len(org_data[0]))
print('置信度较低的cell比率为: ', rate)

# 计算每一列的平均值
average_list = []
for i in range(0, len(org_data[0])):
    data_count = Decimal(0)
    index_count = 0
    for j in range(0, len(org_data)):
        if org_data[j][i] == '_nan_':
            continue
        else:
            data_count += Decimal(org_data[j][i])
            index_count += 1

    average_temp = Decimal(data_count / index_count)
    average_list.append(average_temp)

print('逐列平均值计算完成:', average_list)

'''
index_i作为行索引
index_j作为列索引
'''


def findNear(index_i, index_j):
    ans = Decimal(0)
    bias = 1
    while True:
        if index_i - bias < 0:
            continue
        else:
            if index_i - bias != '_nan_':
                ans = org_data[index_i - bias][index_j]
                return ans
        if index_i + bias >= len(org_data):
            continue
        else:
            if index_j + bias != '_nan_':
                ans = org_data[index_i + bias][index_j]
                return ans

        bias += 1
        if index_i + bias >= len(org_data) & index_i - bias < 0:
            print('error,结果不可信')


# 填补每一列的平均值
for i in range(0, len(org_data[0])):
    for j in range(0, len(org_data)):
        if org_data[j][i] == '_nan_':
            filled_value = findNear(j, i)  # 这里是j代表行数
            org_data[j][i] = filled_value

print('对_nan_值填补完成')

header = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]

filled_data = []
for i in range(0, len(org_data)):
    temp_data = list(org_data[i])
    filled_data.append(temp_data)

with open('filled_repaired_value_near/energy_repaired_filled_4.csv', 'w', newline='') as file_obj:
    writer = csv.writer(file_obj)
    writer.writerow(header)
    for energy in filled_data:
        writer.writerow(energy)

print('数据填充完成并保存csv到本地')
