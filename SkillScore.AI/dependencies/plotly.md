# 📦 `plotly`

## ✅ What is plotly?

**plotly** is a powerful Python library used to create **interactive, web-based visualizations**. Unlike static plots from matplotlib, plotly charts respond to user actions like zooming, hovering, and clicking.

It is ideal for creating dynamic dashboards, data exploration tools, and visual presentations. plotly can be used both in Jupyter notebooks and full-scale web apps, and it supports a wide range of chart types from line and bar graphs to 3D plots and maps.

---

## ✨ Key Features

- Fully interactive plots (hover tooltips, zoom, pan, select)
- Supports complex chart types: 3D scatter plots, heatmaps, choropleth maps, etc.
- Works seamlessly with pandas DataFrames
- Outputs as HTML, which can be embedded in web apps or shared online
- Integrates with frameworks like Dash, Streamlit, and Flask

---

## 📘 Example: plotly in Action

Suppose you want to make an interactive bar chart of student scores.

1. Import plotly: `import plotly.express as px`
2. Prepare your data:  
   `data = {"Name": ["Amit", "Neha", "Rahul", "Priya"], "Score": [75, 88, 92, 85]}`
3. Create a DataFrame: `import pandas as pd` and `df = pd.DataFrame(data)`
4. Build the chart: `fig = px.bar(df, x="Name", y="Score", title="Student Scores")`
5. Show the chart: `fig.show()`

The result is a bar chart that you can hover over to see exact values and even zoom or save as an image.

---

## 🚀 How to Use This in Practice

To use plotly in your project:

- Install it using `pip install plotly`
- Import it using `import plotly.express as px`
- Create a DataFrame or pass in data as lists or dictionaries
- Call a plot function like `px.bar()`, `px.line()`, `px.scatter()`, or `px.pie()`
- Display the plot using `fig.show()`

You can also export the plot to HTML using:  
`fig.write_html("plot.html")` — which you can open in any browser.

---

## 📊 What Kind of Results Can It Produce?

plotly can generate a wide variety of interactive charts:

- Bar and line graphs
- Pie charts and donut charts
- Scatter and bubble plots
- Heatmaps and contour plots
- 3D surface charts and geographical maps

For example, you can visualize monthly sales with tooltips on hover, create animated charts over time, or display geospatial data using interactive maps — all in just a few lines of Python.

---

## 🧠 Summary

plotly is the go-to library when you need **interactive and modern** data visualizations. It’s especially useful for dashboards, exploratory data analysis, and web integration.

If you want your audience to **interact** with your charts — zoom, filter, hover, or animate them — plotly offers a clean and powerful way to do it using only Python.
