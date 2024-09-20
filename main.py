from flask import Flask, render_template, request, redirect, send_file, flash
import os
from werkzeug.utils import secure_filename
from vigenere import vigenere_encrypt, vigenere_decrypt
from playfair import playfair_encrypt, playfair_decrypt
from hill import hill_encrypt, hill_decrypt

app = Flask(__name__)
app.secret_key = 'secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_spaces(text):
    return text.replace(' ', '').replace('\n', '').replace('\r', '')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cipher = request.form.get('cipher')
        operation = request.form.get('operation')
        key = request.form.get('key')

        key = remove_spaces(key)

        if not key or len(key) < 12:
            flash('Kunci harus diisi dan minimal 12 karakter.')
            return redirect(request.url)

        # Mendapatkan input teks atau file
        text = request.form.get('text')
        file = request.files.get('file')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            with open(filepath, 'r') as f:
                input_text = f.read()
            os.remove(filepath)
        elif text:
            input_text = text
        else:
            flash('Silakan masukkan teks atau unggah file txt.')
            return redirect(request.url)
        
        
        input_text = remove_spaces(input_text)

        # Proses enkripsi atau dekripsi
        if cipher == 'vigenere':
            if operation == 'encrypt':
                output_text = vigenere_encrypt(input_text, key)
            else:
                output_text = vigenere_decrypt(input_text, key)
        elif cipher == 'playfair':
            if operation == 'encrypt':
                output_text = playfair_encrypt(input_text, key)
            else:
                output_text = playfair_decrypt(input_text, key)
        elif cipher == 'hill':
            if operation == 'encrypt':
                output_text = hill_encrypt(input_text, key)
            else:
                output_text = hill_decrypt(input_text, key)
        else:
            flash('Cipher tidak dikenali.')
            return redirect(request.url)

        return render_template('index.html', output=output_text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
