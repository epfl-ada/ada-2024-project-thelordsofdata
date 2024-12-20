import numpy as np
import pandas as pd
import plotly.express as px
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sentence_transformers import SentenceTransformer, util
from collections import defaultdict
import seaborn as sns

# Generates the line plots for foreign percentage and domestic in function of the years
def generate_year_plot(df):
    average_percentages = df.groupby('Year')[['Foreign_Percentage', 'Domestic_Percentage']].mean()
    average_percentages = average_percentages.reset_index()
    average_percentages = average_percentages[(average_percentages['Year'] >= 2000) & (average_percentages['Year'] <= 2019)]
    average_percentages = average_percentages.rename(columns={'Foreign_Percentage':'Foreign Percentage', 'Domestic_Percentage':'Domestic Percentage'})

    fig = px.line(average_percentages, 
            x='Year', 
            y=['Domestic Percentage', 'Foreign Percentage'], 
            title='Average Percentages Over Time',
            labels={'value': 'Percentage', 'variable': 'Percentages'}
    )
    fig.update_layout(title=dict(text="Impact of Budget on Foreign Percentage", x=0.5, xanchor='center'))
    fig.show()

