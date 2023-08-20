from flask import Flask, render_template


app= Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio_page():
    return render_template('portfolio.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)