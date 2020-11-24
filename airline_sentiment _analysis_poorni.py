##packages to convert python code to API 

from flask import Flask, jsonify,request

##for loading the Prediction model 
from sklearn.externals import joblib



#Functions apart from the python pipeline code
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
from nltk.stem.wordnet import WordNetLemmatizer
lemma = WordNetLemmatizer()

def split_into_lemmas(message):
    message=message.lower()
    words = word_tokenize(message)
    words_sans_stop=[]
    for word in words :
        if word in stop:continue
        words_sans_stop.append(word)
    return [lemma.lemmatize(word) for word in words_sans_stop]



##Creating an API :
app = Flask(__name__)


#curl request is used to call the server


@app.route('/',methods=['POST'])
def home():
    return 'Hello ,use predict after blackslash '

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.get_json(silent=True)
    message=json_.get('message')
    mydf = pd.DataFrame({'message':message})
    print(mydf)
    prediction = clf.predict(mydf['message'])
    print(prediction)
    return jsonify({'prediction': prediction.tolist()})
 

if __name__ == '__main__':
    clf = joblib.load('/Users/anamika/Downloads/analysis_1_by_poornima.pkl')
    app.run(port=5000)
    