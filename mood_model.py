import pandas as pd
import os.path
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

files = ['./data/yelp.csv', './data/amazon-fine-foods.csv']
model_file_name = 'model.pkl'
vect_file_name = 'vector.pkl'

def get_model():
    if os.path.isfile(model_file_name):
        print("read model")
        nb = joblib.load(model_file_name)
    else:
        print("init model")
        nb = MultinomialNB()
    print("getting model")
    return nb

def get_vect():
    if os.path.isfile(vect_file_name):
        print("read vect")
        vect = joblib.load(vect_file_name)
    else:
        print("init vect")
        vect = CountVectorizer(max_df=0.7)
    print("getting vect")
    return vect


def get_results(text):
    vect = get_vect()
    nb = get_model()
    return nb.predict(vect.transform(text))

def train_model(X, y):
    model = get_model()
    vect = CountVectorizer(max_df=0.7)
    model.fit(vect.fit_transform(X), y)
    print("model trained")

def init_model():
    for file_path in files:
        data = pd.read_csv(file_path)
        good_neutral_bad = data[(data.Score==5) | (data.Score==3) | (data.Score==1)]
        X = good_neutral_bad.Text
        y = good_neutral_bad.Score
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

        vect = get_vect()
        X_train_dtm = vect.fit_transform(X_train)
        X_test_dtm = vect.transform(X_test)

        nb = get_model()
        nb.fit(X_train_dtm, y_train)
        y_pred_class = nb.predict(X_test_dtm)

        print("Acccuracy for "+file_path+": ")
        print(metrics.accuracy_score(y_test, y_pred_class))

        nb.fit(X_test_dtm, y_test)
        joblib.dump(nb, model_file_name)
        joblib.dump(vect, vect_file_name)
    print("model init finished")
