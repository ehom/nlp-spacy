import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

for token in doc:
    if token.pos_ == "PROPN":
        if token.i + 1 < len(doc) and doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)
