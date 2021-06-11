import pandas as pd
import streamlit as st
from preprosessing import preprossesing
import numpy as np
from createRecommendation import recommendations


# load recipes from json file
df = pd.read_csv('recipe-df-2.csv')
print(df['ingredients'][0])


print(df.head(10))

st.header('Add your recipe below')
with st.form(key='my_form'):
    recipe_title = st.text_input(label='Enter the title')
    recipe_ingredients = st.text_input(label='Drop the list of ingredients')
    recipe_dish = st.selectbox(
        'Select the type of dish',
        ('risotto', 'ravioli', 'rijst', 'spaghetti', 'penne', 'quiche', 'pasta', 'pizza', 'stoofpot',
         'curry', 'couscous', 'quinoa', 'groente', 'falafel', 'soep', 'noedels', 'stamppot', 'wrap', 'burrito', 'lasagne'))
    submit_button = st.form_submit_button(label='Find recommendations')

if submit_button:
    st.subheader(f'Recommendations for {recipe_title}:')

    new_row = pd.DataFrame()
    add = [{"link": 0, "category": 0, 'title': recipe_title, 'total_time': 0, "yields": 0,
            'ingredients': recipe_ingredients, 'instructions': 0, "image": 0, "nutrients": 0, 'author': "user", "dish": recipe_dish}]
    new_row = new_row.append(add, ignore_index=True)

    new_row = preprossesing(new_row)
    df = df.append(new_row)
    df_set = df[df['dish'] == recipe_dish].reset_index()

    recommendations = recommendations(df_set, recipe_title)

    # st.dataframe(recommendations)

    for index, row in recommendations.iterrows():
        st.subheader(f'{row["title"]}:')
        st.write(f'Ingredients: {row["ingredients"]}')
        st.write(f'Link to recipe: {row["link"]}')
        st.write(f'Tag: {row["category"]}')
        st.write(f'Smiliraty score: {row["score"][1]}')
        st.write()
