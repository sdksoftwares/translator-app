import os
from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

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

        # Use deep-translator for translation
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
