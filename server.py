from mood_model import get_model
from mood_model import get_vect
from mood_model import train_model
from io import StringIO
from bottle import route, Bottle, SimpleTemplate, run, template, request, static_file

@route('/')
def root():
    return SimpleTemplate(name='index.tpl').render(result = "", message = "", text = "")

def make_prediction(thought):
    nb = get_model()
    vect = get_vect()
    return int(nb.predict(vect.transform([thought])))

@route('/think', method='POST')
def think():
    thought = request.forms.get('thought')
    data = make_prediction(thought)
    print(data)
    result = ""
    if data == 1:
        result = "Sad-ish"
    elif data == 3:
        result = "Neutral-ish"
    elif data == 5:
        result = "Happy-ish"
    else:
        result = "Undefined"
    return SimpleTemplate(name='index.tpl').render(result = result, message = '', text = thought)

@route('/vote', method='POST')
def vote():
    should_we_train_model = request.forms.get('vote')
    if should_we_train_model == "true":
        thought = request.forms.get('thought')
        data = make_prediction(thought)
        print(data)
        train_model(thought, data)
    return SimpleTemplate(name='index.tpl').render(result = "", message = "Thx for vote. Let us make machines smarter.", text = "")

run(host='localhost', port=8079, debug=True)
