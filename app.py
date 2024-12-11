from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Parsing parameter from POST request
    input_value = request.form.get('inputField')
    return f"Halo sang majikan dari {input_value}"

if __name__ == '__main__':
    app.run(debug=True)