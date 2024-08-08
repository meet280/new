import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt



st.title("Lets Play with data")
penduins_df=pd.read_csv("penguin.csv")
st.write(penduins_df.head())
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

penduins_df = penduins_df[penduins_df['species']==selected_species]

alt_chart = (alt.Chart(penduins_df).mark_circle().encode(x=selected_x_var,y=selected_y_var,))

st.altair_chart(alt_chart)
