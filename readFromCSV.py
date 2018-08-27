import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import seaborn as sns
import pandas as pd
import csv
import matplotlib.pyplot as plt


df_mean = pd.read_csv('df_mean.csv')
df_median=  pd.read_csv('df_median.csv')

sns.set_context("paper")
sns.set_style("darkgrid")
sns.regplot(data=df_mean, x=df_mean['hoops'], y=df_mean['steps'], fit_reg=False, color='#008FD5')
sns.regplot(data=df_median, x=df_median['hoops'], y=df_median['steps'], fit_reg=False, color='#FF8900')
# sns.regplot(x=mean_curve_df['hoops'], y=mean_curve_df['steps'], data=mean_curve_df, scatter_kws={'s':1}, fit_reg=False, color='#008FD5')
# sns.regplot(x=median_curve_df['hoops'], y=median_curve_df['steps'], data=median_curve_df, scatter_kws={'s':1}, fit_reg=False, color='#f49a41')

plt.show()