import numpy as np
import pandas as pd
import plotly.express as px
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sentence_transformers import SentenceTransformer, util
from collections import defaultdict
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.express as px

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


def create_box_plot(df, column, y_axis_title, title, log=False): 
    df['Foreign_higher'] = df.copy(deep=True)['Foreign_higher'].replace({
        0: "Domestic % > 50%",
        1: "Foreign % > 50%"
    })


    # Box plot grouped by Rating and Foreign_higher
    fig_box = px.box(df,
        x='Foreign_higher', 
        y=column,  
        color='Foreign_higher', 
        title="Box Plot for Two Classes",
        labels={'value': 'Percentage', 'variable': 'Type'},
        color_discrete_map={"Domestic % > 50%": "blue", "Foreign % > 50%": "red"},  # Customize colors
    )

    fig_box.update_layout(
        title={
            "text": f"Distribution of {title} by Class",
            "x": 0.5,  # Center the title
            "xanchor": "center",  # Anchor the title to the center
        },
        xaxis_title="Class",
        yaxis_title=y_axis_title,
        legend_title="Key",
        width=1100,  
        height=500
    )
    if log:
        fig_box.update_yaxes(
            type="log",
            tickvals=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9],  
            ticktext=["10", "100", "1k", "10k", "100k", "1M", "10M ", "100M", "1B"],  
            title_text=f"Log Scale of {y_axis_title}" 
        
        )
    return fig_box


# Grouped bar chart for counts of movies by Rating and Foreign_higher
def create_bar_plot(df, title, column): 
        
    fig_bar = px.histogram(
        df,
        x="Foreign_higher",
        color="Foreign_higher",  # Separate by Foreign_higher
        title=f"{title} by Class",
        color_discrete_map={"Domestic % > 50%": "blue", "Foreign % > 50%": "red"},  # Optional: Customize colors
    )

    # Update the layout of the bar chart
    fig_bar.update_layout(
        xaxis_title="Class",
        yaxis_title="Count of Movies",
        showlegend=False,  # Hide legend for the bar chart
        width=1100,  
        height=500,
        yaxis=dict(
            autorange="reversed",  # Flip the y-axis to make the bars go downward
        ),
    )
    return fig_bar

def fig_combined_plots(fig_box, fig_bar, title_name, log=False):
    # Create subplots: 2 rows, 1 column (vertical layout)
    fig_combined = make_subplots(
        rows=2, cols=1,
        row_heights=[0.7, 0.3],  # More space for the box plot
        shared_xaxes=True,
        vertical_spacing=0.05,
        subplot_titles=["Class", ""],  # Empty title for second subplot
    )

    # Add all traces from the box plot to the first row
    for trace in fig_box['data']:
        fig_combined.add_trace(trace, row=1, col=1)

    # Add bar chart to the second row
    for trace in fig_bar['data']:
        fig_combined.add_trace(trace, row=2, col=1)

    # Update layout to center the title and maintain consistency in axis titles
    fig_combined.update_layout(
        title={
            "text": f"Distribution of Profitability and {title_name} by Class",
            "x": 0.5,
            "xanchor": "center"
        },
        boxmode="group",  # Group the box plots side-by-side
        yaxis_title=title_name,

        yaxis=dict(
            title=title_name,
            type="log" if log else None,  # Log scale for the first plot if `log` is True
        ),



        showlegend=True,
        xaxis=dict(
            type="category",  # Categorical x-axis
            categoryorder="array",  # Explicitly set order to control spacing
            categoryarray=["Domestic % > 50%", "Foreign % > 50%"],  # Define category sequence
        ),
        yaxis2=dict(
            title="Count",
            autorange="reversed",  # Ensure count axis is reversed for downward bars
        ),

        margin=dict(t=50, b=80),  # Adjust top and bottom margins for proper spacing
        width=1100,
        height=500,
        annotations=[
            dict(
                y=-0.15,  # Position below the x-axis (outside the plot area)
                xref="paper",  # Reference paper (not data)
                yref="paper",
                showarrow=False,
                font=dict(size=14),
                align="center"
            )

        ]
    )
    return fig_combined

