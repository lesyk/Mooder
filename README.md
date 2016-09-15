## Mooder
Machine Learning Sentiment Analysis of text based on data from Amazon fine foods reviews (65 535 samples) and Yelp reviews (10 001 samples). Uses Naive Bayes classifier for multinomial models together with tokenization of text to a matrix of counts. Model is based on [scikit-learn](http://scikit-learn.org/), [bottlepy](http://bottlepy.org/docs/dev/index.html), and [pandas](http://pandas.pydata.org)

To build a model:
```
python -c 'from mood_model import *; init_model()'
```
To start a server:
```
python server.py
```
