from flask import Flask, request
import os

app = Flask(__name__)

# Pasta onde os arquivos recebidos serão salvos
UPLOAD_FOLDER = 'logs_recebidos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return 'Arquivo recebido com sucesso'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
