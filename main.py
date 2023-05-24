from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Data"



@app.route("/get-user/<user_id>")

def get_user(user_id):
    user = {
        'name': "André",
        'id': user_id
    }

    extra = request.args.get('extra')
    if extra:
        user[extra] = 'data'
    return jsonify(user), 200


if __name__ ==  "__main__":
    app.run(debug=True)