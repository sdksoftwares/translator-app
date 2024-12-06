from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text')
        target_lang = data.get('target_lang')

        if not text or not target_lang:
            return jsonify({'error': 'Invalid input'}), 400

        translated = translator.translate(text, dest=target_lang)
        return jsonify({'translated_text': translated.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
