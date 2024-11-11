import streamlit as st
import pandas as pd
from recipee import Recipee

# Page title and app description
st.title("Las recetas de la abuela (Grandma recipees) - Version 3")
st.write("We have a database (20K) of recipees in Spanish.")
st.write("Here you can write an ingredient name, and how many recipees containing it you want to see.")
st.write("You can also check the entire database, to help you get examples of ingredients to look for.")

# Data preparation
recipees_df = pd.read_csv('recetasdelaabuela.csv')

# Interface preparation
ingredient = st.text_input("Enter an ingredient: ")

# New recipee object 
recipee = Recipee(ingredient)

# Search recipees
recipees, amount_of_recipees = recipee.search()

# Based in the amount of recipes, show 1 recipee, show an error or make the user
# choose how many recippes to show

if amount_of_recipees > 0:
    if amount_of_recipees > 1:
        st.write(f"We found {amount_of_recipees} recipees with ingredient {ingredient}.")
        amount = st.slider("Select the amount of recipees", min_value=1, max_value=amount_of_recipees)
    if st.button("Show recipees"):
        st.write("These are the recipees with the chosen ingredient:")
        st.write(recipees.head(amount))
else:
    st.write(f"No recipee found for ingredient {ingredient}")



# Side bar
st.sidebar.title("Advanced options")

st.sidebar.write("If unsure of what ingredients to look for, check the box below to show the data!")

if st.sidebar.checkbox("Show data"):
    st.markdown("---")
    st.write("This is the original data")
    st.write(recipees_df)



