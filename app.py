from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta dinámica para clientes
@app.route('/reserva/<cliente>')
def reserva(cliente):
    return f'Bienvenida {cliente}, tu reserva en Tania Guerrero Beauty Trainer ha sido registrada exitosamente.'

# Ruta dinámica para servicios
@app.route('/servicio/<nombre>')
def servicio(nombre):
    return f'Servicio seleccionado: {nombre}. Pronto nos contactaremos contigo.'

if __name__ == '__main__':
    app.run(debug=True)