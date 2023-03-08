import plotly.express as px
import json
import pandas as pd

json_file = ""
x_val = ""
y_val = ""

if not (json_file or x_val or y_val):
    json_file = input("Filename: ")
    x_val = input("X value: ")
    y_val = input("Y value: ")

f = open(f"json/{json_file}.json", "r")
data = json.load(f)

compress = "y"

data = {key: val for key, val in data.items() if val > 4}

data_dict = {
    x_val: data.keys(),
    y_val: data.values(),
}


fig = px.bar(data_dict, x=x_val, y=y_val, template="plotly_dark")
fig.show()
