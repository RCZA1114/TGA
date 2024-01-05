import streamlit as st   ##This is to deploy the app
import plotly.express as px   ##This is to chart the file
import pandas as pd     ##Read the CSV File


st.set_page_config(
    page_title="TGA Dashboard",    #Give the tab a name
)




st.title("TGA Analysis")    #Put a title in the page


@st.cache_data   #This is so the data only reloaded once.
def load_data():
    data = pd.read_csv("ALLDATA.csv")  #This is to read the csv file
   


    return data



data = pd.read_csv("ALLDATA.csv") #Call the function

data[['Batch Group', 'Batch Group Number']] = data['Batch'].str.split('-', expand=True) #Split the 'Batch' Column into two columns.

batches = data['Batch Group'].unique() #This creates a list of different values.
selected_batch = st.selectbox('Select Batch', batches) #This makes you select between CNM01, CNM02 and CNM03.

filtered_data = data[data['Batch Group'] == selected_batch]

x_axis = st.selectbox('Select X axis', ('Time (min)', 'Temp (Cel)'))   #Select the X Axis


y_axis = st.selectbox('Select Y axis', ('DSC (mW)', 'TG (ug)', 'DTG'))  #Select the Y Axis




fig = px.scatter(filtered_data, x=x_axis, y=y_axis , title="Chart of the Data",) #Chart the Graph


st.plotly_chart(fig, use_container_width=True)   #Show the graph in the app and make it interactive.
