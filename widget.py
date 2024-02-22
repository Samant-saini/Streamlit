import streamlit as st


st.title("widget")

if st.button("subscribe"):
    st.write("you click the button")



name=st.text_input("name")
st.write(name)

address=st.text_area("enter the address")
st.write(address)


date=st.date_input("enter date")
time=st.time_input("enter time")


if st.checkbox("tick the checkbox"):
    st.write("thank you")


st.radio("radio_colour",("r","y","g"),index=0)


st.selectbox("selectbox_colour",("r","y","g"),index=0)



m=st.multiselect("multi_colour",("r","y","g"))
st.write(m)

st.slider("age",min_value=18,max_value=200,value=30,step=2)



st.number_input("number",min_value=18.0,max_value=200.0,value=30.0,step=2.0)



img=st.file_uploader("upload")
st.image(img)