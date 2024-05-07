import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Menampilkan teks 
st.subheader("VISUALISASI DATA")
st.write("Paulina April R Pakpahan (21082010241)")

st.subheader("")
st.subheader("Scatter Plot")
# 1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/Paulinapakpahan/DataVis-2024/blob/main/tips.csv")

# Scatter plot with day against tip
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'])

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# showing the plot
st.pyplot(fig)

st.subheader("")
st.subheader("Line Plot")
# 2
# draw lineplot
fig, ax = plt.subplots() 
sns.lineplot(x="sex", y="total_bill", data=data, ax=ax)

# showing the plot
st.pyplot(fig)

st.subheader("")
st.subheader("Line Chart")
# 3
# plotting the scatter chart
fig = px.line(data, y='tip', color='sex')

# showing the plot
st.plotly_chart(fig)

st.subheader("")
st.subheader("Histogram")
# 4
# draw histogram
fig, ax = plt.subplots()
sns.histplot(data['total_bill'], bins=20, kde=True, ax=ax)

# Setting the X and Y labels
plt.xlabel('Total Bill')
plt.ylabel('Frequency')

# showing the plot
st.pyplot(fig)
