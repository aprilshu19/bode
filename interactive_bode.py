from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import math 

#Find a way to automatically populate csv file from MatLab
df = pd.read_csv('https://raw.githubusercontent.com/aprilshu19/bode/main/bode_points%20(1).txt', sep = ",", )

app = Dash(__name__)

fig = px.line(df, x = 'fout', y = 'mag')  

app.layout = html.Div(children=[
    html.H1(children='Bode Plot'),

    html.Div(children='RLC load'),

    ##Show current capacitor and inductor values pulled in from Matlab - 404

    dcc.Graph(
        id='graph-content',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
    
#Only for RLC model----------------------------------------------------------------
#User input specifies resonant frequency - need to pull in range from csv
'''ALLOWED_TYPES = (
    "range", "capacitance"
)
#Note: To add in app.layout
    [
        dcc.Input(
            id="input_{}".format(_),
            type=_,
            placeholder="input type {}".format(_),
        )
        for _ in ALLOWED_TYPES
    ]
    + [html.Div(id="out-all-types")]


@app.callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(_), "value") for _ in ALLOWED_TYPES],
)
def cb_render(*vals):
    w_res = vals[0]
    #Calculate new capacitor value
    L = float(input("Enter current inductance value: ")) #404
    C = (1 / (2* math.pi * w_res * math.sqrt(L))) ** 2
    vals[1] = C
    return " | ".join((str(val) for val in vals if val))'''

#Link to MatLab GUI to estimate new tf with new component value - 404






