from flask import Flask, render_template, request


app= Flask(__name__)


@app.route('/')

def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio_page():
    return render_template('portfolio.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/submit',methods=['POST'])
def get_form_data():
    if request.method=="POST":
        sender_name= request.form['name']
        sender_email= request.form['email']
        sender_tel= request.form['telephone']
        sender_text= request.form['text']
        return render_template('contact.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)