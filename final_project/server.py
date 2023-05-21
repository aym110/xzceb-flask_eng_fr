import machinetranslation
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french():
    english_text = request.form.get('text')
    french_text = machinetranslation.english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    french_text = request.form.get('text')
    english_text = machinetranslation.french_to_english(french_text)
    return english_text

if __name__ == '__main__':
    app.run()
