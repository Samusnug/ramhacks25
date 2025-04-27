import json
import pandas as pd

with open("phone_pings.json", "r") as r:
    p = r.read()

x = json.loads(p)

df = pd.DataFrame(x)

df.loc[-1] = {
    "device_id": "Theft 1",
    "lat": 40.69308179020694,
    "lon": -73.9194323707594,
    "timestamp": "2025-03-05T02:07:00"
}
import plotly.express as px

size = pd.Series([1 for x in range(185)])

fig = px.scatter_map(df, 
                        lat="lat", 
                        lon="lon", 
                        hover_name="device_id", 
                        hover_data=["device_id", "timestamp"],
                        color="device_id",
                        zoom=8, 
                        size=size,
                        size_max=8,
                        height=1080,
                        width=1920)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()