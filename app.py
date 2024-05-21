from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar-script', methods=['POST'])
def ejecutar_script():
    try:
        print("Ejecutando el script...")
        result = subprocess.run(['python', 'prueba.py'], capture_output=True, text=True)
        output = result.stdout
        print("Script ejecutado, salida:", output)
        return jsonify({'status': 'success', 'output': output})
    except Exception as e:
        print("Error al ejecutar el script:", str(e))
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

