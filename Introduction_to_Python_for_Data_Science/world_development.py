# replicatig plots from training; scatter plot of GDP per capita vs life expectancy; with country populations size

import numpy as np
#import matplotlib.pyplot as plt
import json
import pandas as pd

#data sets we need, 1: Population 2: GDP, 3: life expectancy, 4: continent, 5: Country

with open('br.json') as json_data:
    d = json.load(json_data)
    print(type(d))

brazil = pd.DataFrame.from_dict('br.json')
print brazil ['Area']
cd
