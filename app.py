from flask import Flask, request, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "<h1>Bienvenue sur FileShareSphere</h1>"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return f"Fichier {file.filename} téléchargé avec succès."

@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "Fichier non trouvé", 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)