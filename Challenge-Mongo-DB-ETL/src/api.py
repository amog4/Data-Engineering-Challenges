import flask 
from flask import request, jsonify
import random
from datetime import date, time, datetime, timedelta

# create app variable (Initialize flask)

app = flask.Flask(__name__)






# create randomly generated data 
id = random.sample(range(101 ,40001),200)
user_id = random.sample(range(10001,30001),200)
field = [random.randint(1,4) for r in range(0,200)]
option1 =[random.randint(1,2) for r in range(0,200)]
option2 = [random.randint(1,2) for r in range(0,70)]
option3 = [random.randint(1,2) for r in range(0,150)]
option4 = [random.randint(1,2) for r in range(0,10)]
option5 = [random.randint(1,2) for r in range(0,100)]
dtime = []
for dt in range(0,200):
    d = date.today() - timedelta(days=random.randint(1, 60))
    t = time(8, 0, 0)
    dtime.append(datetime.combine(d, t) + timedelta(seconds=random.randint(1, 25200))) 

dataset = []
for  d in range(0,200):
    data = {}
    value = {}
    data['id'] = id[d]
    data['user_id'] = user_id[d]
    data['field'] = field[d]
    options = {}
    if d < len(option1):
        options['option1'] = option1[d]
    if d < len(option2):
        options['option2'] = option2[d]
    if d < len(option3):     
        options['option3'] = option3[d]
    if d < len(option4):
        options['option4'] = option4[d]
    if d < len(option5):
        options['option5'] = option5[d]
    data['options'] = options
    data['timestamp'] = dtime[d]
    dataset.append(data)



# create router

@app.route('/', methods=['GET'])
def api_all():
    return jsonify(dataset)


app.run(debug=True)