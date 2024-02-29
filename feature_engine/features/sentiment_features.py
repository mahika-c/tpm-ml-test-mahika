# imports
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# TODO - DEFINE YOUR FEATURE EXTRACTOR HERE
# SOURCE: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest?text=newLion+Great+point.++Maybe+they+can+educate+her+mom.
def get_sentiment(text):
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    sentiment = {}
    for i in range(scores.shape[0]):
        l = config.id2label[i]
        sentiment[l] = float(scores[i])

    return sentiment

    # sample output format
    # return({'positive': 0.0, 'negative': 0.0, 'neutral': 0.0})
