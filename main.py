from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()
import os
import smtplib
email= os.getenv('EMAIL')
email_password= os.getenv('EMAIL_PASSWORD')
receiver= os.getenv('RECEIVER_EMAIL')
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
        sender_mail= request.form['email']
        sender_tel= request.form['telephone']
        sender_text= request.form['text']
        send_email(name=sender_name,sender_email=sender_mail,tel=sender_tel,text=sender_text)
        return render_template('contact.html')

    return render_template('index.html')

def send_email(name,sender_email,tel,text):
    email_message= f"Subject: New Message\n\n Name: {name}\n Email: {sender_email}\n Telephone: {tel}\n Message: {text}"
    with smtplib.SMTP('smtp.gmail.com','587') as connection:
        my_email=email
        my_password = email_password
        to_address= receiver
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(my_email,to_address,msg=email_message)


if __name__ == '__main__':
    app.run(debug=True)