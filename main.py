from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin
import pickle
import numpy as np

app = Flask(__name__, template_folder= 'templates')
model = pickle.load(open('rfc.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction == 0:
        output = 'Normal'
    elif prediction == 1:
        output = 'DOS'
    elif prediction == 2:
        output = 'PROBE'
    elif prediction == 3:
        output = 'R2L'
    else:
        output = 'U2R'

    return render_template('index.html', output=output)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    if prediction == 0:
        output = 'Normal'
    elif prediction == 1:
        output = 'DOS'
    elif prediction == 2:
        output = 'PROBE'
    elif prediction == 3:
        output = 'R2L'
    else:
        output = 'U2R'

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)