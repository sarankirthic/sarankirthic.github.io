from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
# from config import Config

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/art')
def art():
    return render_template('art.html', title='Art')


@app.route('/projects')
def projects():
    return render_template('project.html', title='Projects')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


# mail = Mail(app)
#
# @app.route('/contact')
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#
#         msg = Message(subject="New Contact Form Message",
#                       sender=Config.MAIL_USERNAME,
#                       recipients=["sarankirthic@gmail.com", "spskartist@gmail.com"])
#         msg.body = f"From: {name} <{email}>\n\n{message}"
#
#         try:
#             mail.send(msg)
#             flash('Email send Successfully', 'success')
#         except Exception as e:
#             flash(f'Failed to send Email: {str(e)}', 'danger')
#
#         return redirect(url_for('contact'))
#
#     return render_template('contact.html', title='Contact')


@app.route('/secret')
def secret():
    return render_template('secret.html', title='Secret')


@app.route('/helloworld')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
