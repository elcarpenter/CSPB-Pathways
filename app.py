# test
from flask import Flask, render_template, request
import json

from basicGen import basicAlg
from reviews import *

# class_dict = {
#     '1': 'CSPB 1300',
#     '2': 'CSPB 2824',
#     '3': 'CSPB 2270',
#     '4': 'CSPB 3104',
#     '5': 'CSPB 2400',
#     '6': 'CSPB 3308',
#     '7': 'CSPB 3155',
#     '8': 'CSPB 3702',
#     '9': 'CSPB 3022',
#     '10': 'CSPB 4122',
#     '11': 'CSPB 4502',
#     '12': 'CSPB 2820',
#     '13': 'CSPB 3403'
# }

app = Flask(__name__)


class_dict = {
    '1': 1300,
    '2': 2824,
    '3': 2270,
    '4': 3104,
    '5': 2400,
    '6': 3308,
    '7': 3155,
    '8': 3702,
    '9': 3022,
    '10': 4122,
    '11': 4502,
    '12': 2820,
    '13': 3403
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_list = request.form.getlist('mycheckbox')
        selected_class = [class_dict[x] for x in selected_list]
        # remaining_class_key = [new for new in class_dict.keys() if new not in selected_list]
        # remaining_class = [class_dict[x] for x in remaining_class_key]
        to_take = basicAlg(selected_class)
        return {"class to take next semester:": json.dumps(selected_list)}

    return render_template('index.html')

@app.route('/reviews', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        selected_list = request.form.getlist('mycheckbox')
        reviews = review_printer(selected_list)
        return reviews
    else:
        return render_template('reviews.html')


if __name__ == "__main__":
    app.run(debug = True)
