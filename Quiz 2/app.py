from flask import Flask, request, render_template
import requests
from pprint import PrettyPrinter

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template('swapi_form.html')

SWAPI_URL = "https://swapi.py4e.com/api/people"
pp = PrettyPrinter(indent=4)

@app.route('/swapi', methods=['GET', 'POST'])
def swapi():
    if request.method == 'POST':
        character_id = request.form.get('character_id')

        response = requests.get(f'{SWAPI_URL}/{character_id}/')

        record = response.json()

        context = {
        'record': record,
        }
        print(record)
        return render_template('swapi_results.html', **context)
    else:
        context = {
            'error': 'Character cannot be located'
            }
        return render_template('swapi_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
