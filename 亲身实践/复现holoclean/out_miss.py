import pandas as pd
import numpy as np

org_data = pd.read_csv("energy_missing_0.csv")[["0", "1", "2", "3", "4", "5", "6", "7", "8"]].to_numpy()
