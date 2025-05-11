import pandas as pd
from preswald import connect, get_df
from preswald import query, table, text, plotly 
import plotly.express as px



connect()  # Initialize connection to preswald.toml data sources
df = pd.read_csv("data/International_Education_Costs.csv")  # Load data
sql = "SELECT * FROM 1 WHERE value > 50"
filtered_df = query(sql, "my_dataset")
text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")
fig = px.scatter(df, x="column1", y="column2", color="category", title="")
plotly(fig)


