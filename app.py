from flask import Flask, render_template, request, redirect, url_for, flash
from waitress import serve
from flask_mail import Mail, Message
from forms import ContactForm
from config import Config
from dotenv import load_dotenv


app = Flask(__name__)
app.config.from_object(Config)

load_dotenv()

app.secret_key = Config.SECRET_KEY

app.config['RECAPTCHA_PUBLIC_KEY'] = Config.RECAPTCHA_SITE_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = Config.RECAPTCHA_SITE_SECRET

app.config['MAIL_SERVER'] = Config.MAIL_SERVER
app.config['MAIL_PORT'] = Config.MAIL_PORT
app.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = Config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = Config.MAIL_USE_SSL


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


mail = Mail(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        if not name or not email or not subject or not message:
            flash('All fields are required!')
            return redirect(url_for('contact'))

        mail_message = Message(subject='Contact Form Submission',
                               sender=email,
                               recipients=['sarankirthic@gmail.com'],
                               body=f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}")

        mail.send(mail_message)
        flash('Thank you for submitting your message!')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


@app.route('/secret')
def secret():
    return render_template('secret.html', title='Secret')


@app.route('/helloworld')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
