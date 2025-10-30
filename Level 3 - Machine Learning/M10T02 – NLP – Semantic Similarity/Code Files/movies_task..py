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

# --- Run and print result ---
if __name__ == "__main__":
    recommended_movie, similarity_score = most_similar_movie(planet_hulk_desc, movies)
    print(f"Recommended movie: {recommended_movie}")
    print(f"Similarity score: {similarity_score:.3f}")

# =====================================================
# Notes 
# =====================================================
"""
SpaCy’s medium model (en_core_web_md) uses word vectors and looks for semantic content.

Even though the movie plot is very different (WWII story vs. Planet Hulk), SpaCy is likely picking up on:

Words associated with action, conflict, danger, or survival (“soldier fighting for survival”, “monstrous identity”, etc.)

Certain common terms like “soldier”, “monstrous”, or “dangerous” may have high vector similarity to “Hulk”, “gladiator”, “planet”, “dangerous”, etc.

SpaCy is not reading plot logic, only semantic closeness of words.

SpaCy’s model captures general similarity of words and concepts, but it doesn’t understand context like humans do.
"""
