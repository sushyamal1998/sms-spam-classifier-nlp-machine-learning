from flask import Flask, render_template, request
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


app = Flask(__name__)

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

ps = PorterStemmer()

def text_preprocess(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  L = []
  for i in text:
    if i.isalnum():
      L.append(i)

  text = L[:]
  L.clear()
  for i in text:
    if i not in stopwords.words("english") and i not in string.punctuation:
      L.append(i)

  text = L[:]
  L.clear()

  for i in text:
    L.append(ps.stem(i))
  return " ".join(L)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        input_sms = request.form["message"]

        transformed_sms = text_preprocess(input_sms)

        vector_input = tfidf.transform([transformed_sms])

        prediction = model.predict(vector_input)[0]

        if prediction == 1:
            result = "Spam"
        else:
            result = "Not Spam"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
