from math import sqrt

import pandas as pd
from decimal import Decimal
import numpy as np
import csv

repaired_data = pd.read_csv("./filled_repaired_value_near/energy_repaired_filled_4.csv")[
    ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]].to_numpy()
org_data = pd.read_csv("energy.csv")[["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]].to_numpy()
mask = pd.read_csv("./mask/energy_0.1_4.csv")[["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]].to_numpy()

RMSE_count = Decimal(0)
item_count = Decimal(0)
'''
test sentence
print(len(repaired_data))
print(len(org_data))
print(len(mask))
'''

for i in range(0, len(repaired_data)):
    for j in range(0, len(org_data[0])):
        if mask[i][j] == 1:
            temp = Decimal(org_data[i][j] - repaired_data[i][j])
            temp = Decimal(temp ** 2)
            RMSE_count += temp
            item_count += 1

print('near_average_4')
print('RMSE_TOTAL = ', RMSE_count)
print('ITEM_TOTAL = ', item_count)
RMSE = sqrt(Decimal(RMSE_count)/Decimal(item_count))

print('本次RMSE为: ',RMSE)
