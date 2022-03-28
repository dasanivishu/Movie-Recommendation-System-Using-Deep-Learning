import pandas as pd
import numpy as np
np.random.seed(123)

ratings = pd.read_csv('rating.csv', parse_dates=['timestamp'])

rand_userIds = np.random.choice(ratings['userId'].unique(), 
                                size=int(len(ratings['userId'].unique())*0.3), 
                                replace=False)

ratings = ratings.loc[ratings['userId'].isin(rand_userIds)]
