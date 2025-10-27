# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:46:23 2025

@author: juleigar
"""

# garden.py
import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

# List of garden path sentences
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The old man the boat.",
    "The horse raced past the barn fell."
]

# Process each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nSentence: {sentence}")
    
    # Tokenisation and Part-of-Speech tagging
    print("Tokens and POS tags:")
    for token in doc:
        print(f"{token.text} - {token.pos_}")
    
    # Named Entity Recognition
    print("Named Entities:")
    if doc.ents:
        for ent in doc.ents:
            print(f"{ent.text} - {ent.label_} ({spacy.explain(ent.label_)})")
    else:
        print("No named entities detected.")
# Comments on two entities that were looked up:

# 1. Entity: 'Mississippi'
#    Explanation: GPE (Countries, cities, states)
#    Did it make sense? Yes, it makes sense because 'Mississippi' is a U.S. state, 
#    and spaCy correctly recognized it as a geopolitical entity.

# 2. Entity: 'Mary'
#    Explanation: PERSON (People, including fictional)
#    Did it make sense? Yes, it makes sense because 'Mary' is a person's name, 
#    so spaCy correctly classified it as a person.
