from nltk import wordnet as wn 
import numpy as np
import random

def col_synonyms_wn(input_text):
    """
    Get synonyms using wordnet
    """
    sample_texts = wn.synonyms(input_text)
    closest_relation = sample_texts[0]
    if len(closest_relation) > 1:
        output_text = np.random.choice(closest_relation, size=1)
    elif len(closest_relation) == 1 :
        output_text = closest_relation[0]

    return closest_relation


def col_synonyms_slm(input_text):
    """
    Using OLLAMA
    """
    raise Exception("Not implemented")