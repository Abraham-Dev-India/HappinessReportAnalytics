import warnings
warnings.filterwarnings("ignore")        
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
import seaborn as sns
import squarify
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sklearn
from sklearn.manifold import TSNE
import matplotlib.patches as mpatches


#get data
df = pd.read_csv('world-happiness-report-2021.csv')

print(df['Country name'][2])
df2 = pd.read_csv('world-happiness-report.csv')
pop = pd.read_csv('population_by_country_2020.csv')




df3 = df2.loc[df2['Country name'].isin(['China','India','Pakistan','Afghanistan','Bhutan','Nepal','United States'])]
df3.reset_index(inplace = True)

df4 = df.loc[df['Country name'].isin(['China','India','Pakistan','Afghanistan','Bhutan','Nepal','United States'])]
df4.reset_index(inplace = True)

#print(df2.loc[df2['Country name'].isin(['Afghanistan','India'])])
# create a figure and axis
fig, ax = plt.subplots()


#create colour dictionary
colors = {'China':'r','India':'b','Pakistan':'g','Afghanistan':'y','Bhutan':'m','Nepal':'c','United States':'k'}
#print(df3['Country name'][len(df3['Life Ladder'])])


red_patch = mpatches.Patch(color='r', label='China')
blue_patch = mpatches.Patch(color='b', label='India')
green_patch = mpatches.Patch(color='g', label='Pakistan')
yellow_patch = mpatches.Patch(color='y', label='Afghanistan')
magenta_patch = mpatches.Patch(color='m', label='Bhutan')
cyan_patch = mpatches.Patch(color='c', label='Nepal')
black_patch = mpatches.Patch(color='k', label='United States')


for i in range(len(df3['Perceptions of corruption'])):
    ax.scatter(df3['Perceptions of corruption'][i], df3['Life Ladder'][i],color=colors[df3['Country name'][i]])
ax.legend(handles=[red_patch,blue_patch,green_patch,yellow_patch,magenta_patch,cyan_patch,black_patch])


# scatter the sepal_length against the sepal_width
#ax.scatter(df2['Life Ladder'], df2['Perceptions of corruption'])


# set a title and labels
ax.set_title('Happiness')
ax.set_xlabel('Perceptions of corruption')
ax.set_ylabel('Life Ladder')

#print(df3.head(100))
# get columns to plot
columns = df3.columns.drop(['year','Generosity',
'Positive affect','Negative affect','Social support','index',
'Perceptions of corruption','Healthy life expectancy at birth','Freedom to make life choices',
'Country name'])
# create x data
x_data = range(0, df3.shape[0])

# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, df3[column], label=column)
# set title and legend
ax.set_title('Happiness')
ax.legend()


# create a figure and axis 
fig, ax = plt.subplots() 

# count the occurrence of each class 
data = df['Ladder score'].value_counts() 
# get x and y data 
#points = data.index 
#frequency = data.values 
country = df4['Country name'].to_list()
ladderscore = df4['Ladder score'].to_list()
colorList = ['red','blue','yellow','orange','cyan','black']

# create bar chart 
ax.barh(country, ladderscore,color=colorList) 
# set title and labels 
ax.set_title('India and neighbouring countries') 
ax.set_xlabel('Ladder score') 
ax.set_ylabel('Country')





#df['Ladder score'].value_counts().sort_index().plot.barh()




plt.show()