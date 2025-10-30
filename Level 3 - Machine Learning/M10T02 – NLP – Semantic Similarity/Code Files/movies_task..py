# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:18:15 2025
@author: juleigar

semantic.py
------------
Movie similarity finder using spaCy.

This version works on both local machines and Google Colab.
It compares a given movie description ("Planet Hulk") to a list of movie descriptions
and finds the most semantically similar one using SpaCy’s word vectors.
"""

import spacy
import os

# --- Install the model only if it's missing ---
# Instead of automatically running pip commands (which can break portability),
# check for the model and download it only if not already installed.
try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    print("Downloading 'en_core_web_md' model...")
    from spacy.cli import download
    download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")

# --- Read movie descriptions from file ---
# Expecting a 'movies.txt' file in the same directory.
file_path = "movies.txt"

if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"❌ Could not find '{file_path}'. Please place your movies.txt file "
        f"in the same folder as this script."
    )

with open(file_path, "r", encoding="utf-8") as f:
    movies = [line.strip() for line in f.readlines() if line.strip()]

# --- Planet Hulk description ---
planet_hulk_desc = (
    "Will he save their world or destroy it? "
    "When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle "
    "and launch him into space to a planet where the Hulk can live in peace. "
    "Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
)

# --- Function to find the most similar movie ---
def most_similar_movie(description, movie_list):
    """
    Returns the movie with the description most similar to the input.

    Parameters:
        description (str): The reference movie description.
        movie_list (list): A list of other movie descriptions to compare against.

    Returns:
        tuple: (most similar movie description, similarity score)
    """
    desc_doc = nlp(description)
    best_movie = None
    max_similarity = -1

    for movie in movie_list:
        movie_doc = nlp(movie)
        similarity = desc_doc.similarity(movie_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            best_movie = movie

    return best_movie, max_similarity

# --- 5️⃣ Run and print result ---
if __name__ == "__main__":
    recommended_movie, similarity_score = most_similar_movie(planet_hulk_desc, movies)
    print(f"Recommended movie: {recommended_movie}")
    print(f"Similarity score: {similarity_score:.3f}")

# =====================================================
# Notes and Explanation (Juleiga Regal)
# =====================================================
"""
SpaCy’s medium model (en_core_web_md) uses word vectors to identify semantic
similarity between texts. It compares the meaning of words rather than just
their literal text.

Even though the movie plots might differ (for example, a WWII story vs. Planet Hulk),
SpaCy finds similarity through shared **themes and vocabulary** — such as:
    - action
    - conflict
    - danger
    - survival

Terms like “soldier”, “fighting”, “monstrous”, or “dangerous” are semantically
related to words in the Hulk description like “gladiator”, “planet”, or “dangerous”.

✅ Key Insight:
SpaCy does **not** understand story logic or plot structure.
It only measures how close the meanings of words and phrases are in a
multi-dimensional vector space.

Therefore, the recommendation may appear logical in terms of word similarity,
even if the movie stories are unrelated from a human perspective.
"""
