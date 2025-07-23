from flask import Flask, request, jsonify, render_template
import sys
from io import StringIO

from interpreter import run_varlang, variables, functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("playground.html")

@app.route('/run', methods=['POST'])
def run_code():
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        data = request.get_json()
        code = data.get('code', '')

        # Clear interpreter state
        variables.clear()
        functions.clear()

        # Run the code
        run_varlang(code)

        output = captured_output.getvalue()
        sys.stdout = old_stdout
        return jsonify({'success': True, 'output': output})
    except Exception as e:
        sys.stdout = old_stdout
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)