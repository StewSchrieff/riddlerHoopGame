
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import seaborn as sns
import pandas as pd
import csv
import matplotlib.pyplot as plt


class game:
    def __init__(self, length):
        self.length = length
        self.blue = 0
        self.red = length + 1
        self.time = 0
        self.completed = False
        self.winner = ""
        pass

    def __repr__(self):
        s = "t: "
        s = s + str(self.time)
        s = s + "\nBlue: "
        s = s + str(self.blue)

        s = s + "\nRed: "
        s = s + str(self.red)
        return s

    def step(self):
        # here we simulate a step
        self.time += 1
        if(self.blue + 1 > self.red - 1):
            # resolve conflict
            self.resolve_conflict()
        else:
            self.blue = self.blue + 1
            self.red = self.red - 1
        self.check_for_end()

    def resolve_conflict(self):
        # dist = self.red - self.blue
        # if dist == 1:


        # Meet halfway
        rps = self.play_r_p_s()
        if rps == 0:
            # Tie
            return
        if rps == 1:
            # Blue wins
            self.red = self.length + 1
            self.blue += 1
            return
        if rps == 2:
            # Red Wins
            self.red -= 1
            self.blue = 0

    def check_for_end(self):
        self.completed = (self.blue == self.length) \
                         or (self.red == 1)
        if(self.completed):
            # print("WINNER")
            if(self.blue <= 1):
                self.winner = "Red"
            else:
                self.winner = "Blue"




    def play_r_p_s(self):
        return random.randint(0,3)



list_of_means = []
list_of_medians = []

# for how_many_hoops in range(5,200, 20):
for how_many_hoops in range(5,600, 10):
    red_win = []
    blue_win = []
    for i in range(1,20):
        print(how_many_hoops)
        x = game(how_many_hoops)
        while(not x.completed):
            x.step()
        # print(x.winner)
        # print(x.time)
        if x.winner == "Blue":
            blue_win.append(x.time)
        else:
            red_win.append(x.time)


    blue_win = pd.DataFrame(blue_win)
    red_win = pd.DataFrame(red_win)

    red_min = blue_win.min()
    blue_mean = blue_win.mean()
    blue_median = blue_win.median()

    red_min = red_win.min()
    red_mean = red_win.mean()
    red_median = red_win.median()

    mean = (float(red_mean) + float(blue_mean)) / 2
    mean = mean
    concat = red_win.append(blue_win)
    concatMedian = concat.median()
    concatMean = float(concat.mean())
    median = float(concatMedian)
    # print(median)
    # print(mean)

    list_of_means.append((how_many_hoops, concatMean))
    list_of_medians.append((how_many_hoops, median))
# in order for the games to last 30 min, we need the avg game to last 60 * 30 sec
# or 1800 steps.
# print(list_of_tuples)

# print(list_of_tuples)
df_mean = pd.DataFrame.from_records(list_of_means, columns=['hoops', 'steps'])
df_median = pd.DataFrame.from_records(list_of_medians, columns=['hoops', 'steps'])

z = np.polyfit(df_mean['hoops'], df_mean['steps'], 3)
f = np.poly1d(z)

mean_curve = []
# iterate_me = np.linspace(5,400, 10000)
for ex in range(5,600, 1):
    eff = f(ex)
    mean_curve.append((ex,eff))

mean_curve_df = pd.DataFrame.from_records(mean_curve, columns=['hoops','steps'])




z = np.polyfit(df_median['hoops'], df_median['steps'], 3)
f = np.poly1d(z)

median_curve = []
for ex in range(5,600, 1):
    eff = f(ex)
    median_curve.append((ex,eff))

median_curve_df = pd.DataFrame.from_records(median_curve, columns=['hoops','steps'])


# print(df)
# print(len(blue_win))
# print(len(red_win))


# concatenated = pd.concat([red_win.assign(dataset='blue_win'), blue_win.assign(dataset='red_win')])
# sns.scatterplot(x='time', y='ATR', data=concatenated,
#                 hue='Asset Subclass', style='dataset')

# sns.kdeplot(red_win)

# print(concatenated.columns)

# min_length = min(len(blue_win), len(red_win))
# print(min_length)
# sns.jointplot(x=blue_win[range(1,min_length)], y=red_win[range(1,min_length)])
# sns.regplot(x='index', y=concatenated[0], data=concatenated.reset_index())
# sns.distplot(a=red_win, bins=40)

print(mean_curve_df.head())
print(median_curve_df.head())
sns.set_context("paper")
sns.set_style("darkgrid")
sns.regplot(data=df_mean, x=df_mean['hoops'], y=df_mean['steps'], fit_reg=False, color='#008FD5')
sns.regplot(data=df_median, x=df_median['hoops'], y=df_median['steps'], fit_reg=False, color='#f49a41')
sns.regplot(x=mean_curve_df['hoops'], y=mean_curve_df['steps'], data=mean_curve_df, scatter_kws={'s':1}, fit_reg=False, color='#008FD5')
sns.regplot(x=median_curve_df['hoops'], y=median_curve_df['steps'], data=median_curve_df, scatter_kws={'s':1}, fit_reg=False, color='#f49a41')

plt.show()


# print("Hello")
# Only uncomment if you want to overwrite the accurate data already stored
# df_mean.to_csv('df_mean.csv')
# df_median.to_csv('df_median.csv')


# print(random.randint(0,2))
