from dash import Dash, dcc, html
import plotly.express as px
from base64 import b64encode
import io


buffer = io.StringIO()

df = px.data.iris() # replace with your own data source

#print(set(df["species"])) #{'setosa', 'virginica', 'versicolor'}
#print(df.head(10))
#specific_data=df[["Id","Species"]]

#df.iloc[5]
print(df.loc[df["species"] == "versicolor"])







