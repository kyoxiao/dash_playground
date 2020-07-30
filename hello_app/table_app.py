# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import redis

u_redis = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

data=[]

for key in u_redis.scan_iter("*"):
    obj = u_redis.hgetall(key)
    data.append(obj)

df = pd.DataFrame(data)

print(df.to_dict('records'))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dash_table.DataTable(
    id='table1',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)

