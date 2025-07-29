from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(dob, favorite, digits=4, total_length=10):
    dob_digits = ''.join(filter(str.isdigit, dob))
    selected_digits = dob_digits[:digits]

    symbols = "!@#$%&*"
    random_chars = ''.join(random.choices(string.ascii_letters + symbols, k=total_length - len(selected_digits)))

    password = selected_digits + favorite[:2].capitalize() + random_chars
    return ''.join(random.sample(password, len(password)))

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    if request.method == 'POST':
        dob = request.form.get('dob')
        favorite = request.form.get('favorite')
        password = generate_password(dob, favorite)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

