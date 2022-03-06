from flask import Flask, render_template, request

app = Flask(__name__)

class_dict = {
    '1': 'CSPB 1300',
    '2': 'CSPB 2824',
    '3': 'CSPB 2270',
    '4': 'CSPB 3104',
    '5': 'CSPB 2400',
    '6': 'CSPB 3308',
    '7': 'CSPB 3155',
    '8': 'CSPB 3702',
    '9': 'CSPB 3022',
    '10': 'CSPB 4122',
    '11': 'CSPB 4502',
    '12': 'CSPB 2820',
    '13': 'CSPB 3403'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_list = request.form.getlist('mycheckbox')
        remaining_class_key = [new for new in class_dict.keys() if new not in selected_list]
        remaining_class = [class_dict[x] for x in remaining_class_key]
        print("Classes remaining: ")
        print(remaining_class)
        return 'Done'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)