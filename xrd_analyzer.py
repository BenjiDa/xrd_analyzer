import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool


path = '/path/to/your/data/'
name = 'your_data'
extension = '.xlsx'

df = pd.read_excel(path+name+extension)
df.columns = ['2 theta', 'Intensity']

#df.plot(x='2 theta', y='Intensity')


# Creating figure
output_file(name+".html")

hover = HoverTool(tooltips=[
    ("Intensity", "@y"),
    ("Degrees", "@x"),
])

# create a new plot with a title and axis labels
p = figure(title="XRD data: Sample "+name, x_axis_label='2 theta (degrees)', y_axis_label='Intensity',
           tools=[hover, 'pan', 'wheel_zoom', 'box_zoom', 'crosshair', 'reset'], plot_width=1500, plot_height=500, responsive=True)

# add a line renderer with legend and line thickness
p.line(df['2 theta'], df['Intensity'], legend="", line_width=2)  # , source=df)

# show the results
show(p)
