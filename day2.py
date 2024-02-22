import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
data=pd.DataFrame(
    np.random.randn(100,3),
    columns=["a","b","c"]
)

chart=alt.Chart(data).mark_circle().encode(
    x='a',y="b",tooltip=['a','b']
)

st.header("show the map")
st.map()



st.header("flow chart")
st.graphviz_chart("""
digraph{
watch->like
like->share
like->subscribe
}




""")

st.set_option('deprecation.showPyplotGlobalUse', False)


st.header("scatterplot using the matplotlib")
plt.scatter(data['a'],data['b'])
plt.title("scatter plot")
st.pyplot()

st.header("line chart")
st.line_chart(data)

st.header("area chart")
st.area_chart(data)

st.header("bar chart")

st.bar_chart(data)




#to display images

st.header("display images")
st.image("streamlit.png")


#adding the audio
st.header("adding the audio")
st.audio("audio.m4a")

# adding the video
st.header("adding the video")
st.video("assignment.mkv")


#adding the video link
st.header("using the link to add video")
st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=4")