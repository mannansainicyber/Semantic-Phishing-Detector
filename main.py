# import sklearn numpy, spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

# load the `en_code_web_md model (of SpaCY?)`
nlp = spacy.load("en_core_web_md")
# define the function
def check_threat_level(word):
    # set the target text
    target = nlp("confirm urgent account to release funds")
    # generate the word token
    token = nlp(word)
    # check similarity between `target` and  `token`
    sim = target.similarity(token)
    return sim

usr_input = input("Enter Text to scan..\n>>>")
words = usr_input.split()
max_score = max([check_threat_level(w) for w in words])
score = check_threat_level(usr_input)

if score > 0.70 or max_score > 0.80:
    print(f"HIGH ALERT!!!!!! (Sentence: {score:.2f}, Max Word: {max_score:.2f})")
elif score > 0.40:
    print("Mehhh, may be phising but idk i dont get paid enough")
else:
    print("This is clear")
