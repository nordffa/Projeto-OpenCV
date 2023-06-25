from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/filtro_aplicado', methods=['POST'])
def filtro_aplicado():
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(
        file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    escolha_filtro = request.form['escolha_filtro']
    if escolha_filtro == 'cinza':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif escolha_filtro == 'borrado':
        img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite('static/imagem_filtrada.jpg', img)
    return render_template('filtro.html')


if __name__ == '__main__':
    app.run()
