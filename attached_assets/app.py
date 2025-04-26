from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods = ["POST"])
def ask():
data = request.get_json()
question = data.get("question", "")
response = f"Tu as demandé : {
	question
}" # Logique IA simple (à remplacer)
return jsonify({
	"response": response
})

if __name__ == "__main__":
app.run(debug = True)