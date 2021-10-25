from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px

url='https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
print("This could take several minutes")
df = pd.read_csv(
    url, converters={'fips': lambda x: str(x)}
    )
url2="https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
unique_states = df['state'].unique()
plt.style.use("seaborn-talk")

# Get last date to see which states have the most cases currently
last_date = df['date'].max()
df_last_date = df[ df['date'] == last_date]
series_last_date = df_last_date.groupby('state')['cases'].sum().sort_values(ascending=False)
print(series_last_date)

labels = []
values = []
state_count = 5
other_total = 0
for state in series_last_date.index:
    if state_count > 0:
        labels.append(state)
        values.append(series_last_date[state])
        state_count -= 1
    else:
        other_total += series_last_date[state]
labels.append("Other")
values.append(other_total)

wedge_dict = {
    'edgecolor': 'black',
    'linewidth': 2        
}

explode = (0, 0.1, 0, 0, 0, 0)
#this part is for pie chart
plt.title(f"Total Cases on {last_date}")
plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%', wedgeprops=wedge_dict)
plt.show()

#this part is for USA map
df_frame=df_last_date.groupby('state')['cases'].sum().to_frame()
df_frame= pd.merge(df_frame, pd.read_csv(url2), left_on=df_frame.index, right_on='State')

fig = px.choropleth(df_frame,
                    locationmode="USA-states",
                    locations=df_frame['Abbreviation'],
                    color='cases',
                    color_continuous_scale='magma',
                    range_color=(0, df_frame['cases'].max()),
                    scope='usa'
                    )
fig.write_image("usa.png", engine="kaleido") 
