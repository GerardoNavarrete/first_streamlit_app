import streamlit

# Info
streamlit.title("My Parents New Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣OMEGA 3 & Blueberry Oatmeal")
streamlit.text("🥗kale, Spinach & Smoothie")
streamlit.text("🐔Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞Avocado Toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

# Loaded fruit table & added an index
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_shown = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_shown)

# Import the From fruityvice website the watermelon info 
streamlit.header("FruityVice Fruit Advice")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# normalizes the json info we just retrieved from our request 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Displays the normalized data istead of json format
streamlit.dataframe(fruityvice_normalized)

# created an input 
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
