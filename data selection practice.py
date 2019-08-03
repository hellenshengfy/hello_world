import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas=pd.read_csv('gas_prices.csv')


print(gas.iloc[2:4,1:3])
print(gas.iloc[[2,3],[1,2])?????