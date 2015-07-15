# WILL COME BACK TO LATER

import pandas as pd 
import numpy as np
import statsmodels.api as sm

# Downloaded from https://www.lendingclub.com/info/download-data.action
lendingClub = pd.read_csv('LoanStats3a.csv')

print lendingClub.head()