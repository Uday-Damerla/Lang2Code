from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from Lang2Code import Lang2Code

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

PORT = 9000
Lang2Code = Lang2Code()
print("Intent Classification and Entity Recognition Model Successfully Loaded....")


@cross_origin()
@app.route('/Lang2Code', methods=['POST'])
def Lang2Code_request():
    data = request.get_json()
    text = data.get('text')
    response = Lang2Code.Lang2Code_engine(text)
    print("\n\n")
    print(response)
    print("\n\n")
    return response

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Lang2Code Server!"

if __name__ == '__main__':
    examples = [
        "insert median values replacing with the null values",
        "Split dataset into training and test set",
        "Duplicate rows in this dataset",
        "Construct a bar plot",
        "Perform Random Forest Regression",
        "Code for all Regression models"
    ]
    print(f"Server running on http://127.0.0.1:{PORT}/")
    app.run(host="127.0.0.1", port=PORT)