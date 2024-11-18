from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def promedionotas():
    promedio = None
    asistencia = None
    estado = None
    error_message = None
    if request.method == 'POST':
        try:
            nota1 = request.form['nota1']
            nota2 = request.form['nota2']
            nota3 = request.form['nota3']
            asistencia = request.form['asistencia']

            # Verifica si todos los campos están llenos
            if not nota1 or not nota2 or not nota3 or not asistencia:
                error_message = "Todos los campos deben estar llenos"
            else:
                nota1 = int(nota1)
                nota2 = int(nota2)
                nota3 = int(nota3)
                asistencia = int(asistencia)

                if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                    error_message = "Las notas deben estar entre 10 y 70"
                elif not (0 <= asistencia <= 100):
                    error_message = "La asistencia debe estar entre 0 y 100"
                else:
                    promedio = (nota1 + nota2 + nota3) / 3
                    if promedio >= 40 and asistencia >= 75:
                        estado = 'aprobado'
                    else:
                        estado = 'reprobado'

        except ValueError:
            error_message = "Por favor, ingresa valores numéricos válidos para las notas y la asistencia."

    return render_template('ejercicio1.html', promedio=promedio, asistencia=asistencia, estado=estado, error_message=error_message)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def calcularMayor():
    resultado = None
    cantidadletras = None
    error_message = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Verifica si todos los campos están llenos
        if not nombre1 or not nombre2 or not nombre3:
            error_message = "Todos los campos deben estar llenos"
        else:
            lista = [nombre1, nombre2, nombre3]
            resultado = max(lista, key=len)
            cantidadletras = len(resultado)

    return render_template('ejercicio2.html', resultado=resultado, cantidadletras=cantidadletras, error_message=error_message)

if __name__ == '__main__':
    app.run()