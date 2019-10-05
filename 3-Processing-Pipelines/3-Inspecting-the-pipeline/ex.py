import spacy
import pprint

nlp = spacy.load('en_core_web_sm')


# Print the names of the pipeline components
print(nlp.pipe_names)

# Print the full pipeline of (name, component) tuples
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(nlp.pipeline)
