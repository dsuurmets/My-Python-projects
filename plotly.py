# %%
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
df = pd.read_csv('/Users/user/Downloads/winequality-red.csv') # ,sep=';')
df.head()

# %%
df['sulphates_rank'] = pd.qcut(df['sulphates'],2)
df['alcohol_rank'] = pd.qcut(df['alcohol'],2)
Y ='alcohol'
X ='quality'
df

# %%
df_count = df['quality'].value_counts()
df_count = pd.DataFrame(df_count).reset_index()
df_count.columns = ['Quality','Count']
df_count

# %%
fig = px.bar(df_count, x='Quality', y='Count',width=500, height=400)
fig.show()
plotly.offline.plot(fig, filename='plotly_barrr.html') 

# %%
plotly.offline.plot(fig,filename='plotly_offline_plot.html',auto_open=False)

# %%
#https://github.com/dataman-git/codes_for_articles/blob/master/Plot%20with%20Plotly%20for%20article.ipynb
#instead of df_pie, put df_count
fig = px.pie(df, values='Count',names='Quality', title='Wine quality',width=600, 
             height=400)
fig.show()

plotly.offline.plot(fig, filename='plotly_pie.html')

# %%
fig = px.histogram(df, x="quality",
            width=600, height=400)
fig.show()
plotly.offline.plot(fig, filename='plotly_histogram.html') 
# %%
fig = px.box(df, y="alcohol",width=600, height=400)
fig.show()
plotly.offline.plot(fig, filename='plotly_box0.html') 
# %%
