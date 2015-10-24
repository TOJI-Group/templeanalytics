import plotly.plotly as py
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)
scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
        [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
df['text'] = df['state'] + '<br>' +\
        'Beef '+df['beef']+' Dairy '+df['dairy']+'<br>'+\
        'Fruits '+df['total fruits']+' Veggies ' + df['total veggies']+'<br>'+\
        'Wheat '+df['wheat']+' Corn '+df['corn']

print(df)
