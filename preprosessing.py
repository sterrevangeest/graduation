# preprossesing & cleaning the data
import spacy

from spacy import displacy
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
import nl_core_news_lg
nlp = nl_core_news_lg.load()


def preprossesing(df):
    for index, row in df.iterrows():
        # converting ingredients object to an string
        # initialize an empty string
        print("PREPROCESSING")

        ingredients_all = row['ingredients']
        df.at[index, 'ingredients'] = "".join(ingredients_all)

        doc = nlp(df.at[index, 'ingredients'])
        ingredients_list = []

        for token in doc:
            if token.pos_ == "NOUN":
                ingredients_list.append(token.text)
                df.at[index, 'ingredients'] = " ".join(ingredients_list)

        print(row['ingredients'])
    return df
