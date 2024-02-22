import streamlit as st
import numpy as np
import pandas as pd

import time


st.title("hello streamlit")



st.header("header")



st.subheader("subheader")



st.text("this the streamlit page and i am learning streamlit for the machine leaning webpage deployment on the strealit")

#using st.markdown to use the tag or to add the emoji or to add the html tag and also to add the bold and italic text

st.markdown("""  # h1 tag 
    ## h2 tag
    ### h3 tag


    :moon: 
    :sunglasses:
            ** bold text **
    __ italic text __
    """,True)



st.latex(r'''   x^2 + y^2 = r^2 ''')



st.write("samant saini streamlit")

# to display the data on the streamlit

a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd =n.reshape((2,4))


dict={
    "name":["samant","sam"],
    "age":[21,42],
    "city":["ghaziabad","noida"]      
          
}

data=pd.read_csv("DigiDB_digimonlist.csv")


st.header("displaying the data from the csv file")
st.dataframe(data)

st.header("displaying the data from the dictionary")
st.dataframe(dict)

st.header("displaying the data from the array")
st.dataframe(a)


st.header("data in the table")
st.table(dict)

st.header("json format")
st.json(dict)

# if a function is run previosly so if run again it will check the cache memory if the precious result of the function is avialabe  if so then print it directly
@st.cache
def set_time():
    time.sleep(5)
    return time.time()


if st.checkbox("1"):
    st.write(set_time())
if st.checkbox("2"):
    st.write(set_time())