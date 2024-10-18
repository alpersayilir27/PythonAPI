from flask import Flask, request, jsonify

app = Flask(__name__)

# GET method route
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Alper Sayilir",
        "email": "alper@example.com"
    }

    # Check for 'extra' query parameter
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# POST method route
@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
