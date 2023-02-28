import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string

def preprocess(text):
    # remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word.lower() not in stop_words]

    # remove punctuation and convert to lowercase
    text = ''.join([word.lower() for word in words if word not in string.punctuation])
    return text
def jaccard_similarity(text1, text2):
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
text1 = "This is the first text."
text2 = "This is the second text."

text1 = preprocess(text1)
text2 = preprocess(text2)

similarity = jaccard_similarity(text1, text2)
print("Similarity:", similarity)
