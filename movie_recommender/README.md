
Description: We are Building a Book Recommender System and Our task is to Build a Content Based Recommender System which clubs similar movies and recommends it. We are not solving a Collaborative Filtering based Recommender where User Interests are Taken in.

Dataset Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download

We will be Dividing into 6 Steps.

1.Data

2.Pre-Processing

3.Vectorization ( A part of Pre-Processing )

4.Model-Building

5.Convert Into Website

6.Deployment ( I haven't Deployed because Heroku ke Liye I needed to fill my credit card details )

Key-Libraries Used:

1.Numpy

2.Pandas

3.ast

3.1 ast.literal_eval: Converts a String which Contains a List of Dictionaries into a List of Dictionaries
    
4.sklearn

4.1 feature_extraction.text import CountVectorizer: Converts a Document into Vectors using a method called Bag of Words.
4.2 metrics.pairwise import cosine_similarity: To find Similarity between different vectors using angle between 2 vectors

