import streamlit
import pandas


streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruituvice Fruit Advice')
import requests
fruit_choice=streamlit.text_input('what fruit would you like information about?','kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx=snowflake.connector.connect(**streamlit.secrets["snoflake"])
my_cur=my_cnx.cursor()
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
my_data_row=my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
add_my_fruit=streamlit.text_input('what fruit would you like to add?','jackfruit')
streamlit.text('Thanks for adding jackfruit')

