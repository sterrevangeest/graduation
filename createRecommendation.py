import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel


def recommendations(df, title):
    # TFIDF Vectorizer
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['ingredients'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    cosine_sim.shape
    indices = pd.Series(df.index, index=df['title'])

    def get_recommendations(title, cosine_sim=cosine_sim):
        # Get the index of the recipe that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all recipes with that recipe
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the recipe based on the similarity scores
        sim_scores_all = sorted(
            sim_scores, key=lambda x: x[1], reverse=True)
        # Get the scores of the 10 most similar recipes
        sim_scores = sim_scores_all[1:5]

        # Get the movie indices
        recipe_indices = [i[0] for i in sim_scores]

        new_df = pd.DataFrame()
        # new_df['scores'] = sim_scores_all
        new_df['ingredients'] = df['ingredients'].iloc[recipe_indices]
        new_df['title'] = df['title'].iloc[recipe_indices]
        new_df['link'] = df['link'].iloc[recipe_indices]
        new_df['score'] = sim_scores
        new_df['category'] = df['category'].iloc[recipe_indices]

        return new_df
    get_df = get_recommendations(title)
    return get_df
