from flask import Flask, render_template
from waitress import serve
from utils.icons import render_icon

from resources import about, projects, experience, skills, education, certifications

app = Flask(__name__)
app.jinja_env.globals.update(render_icon=render_icon)


@app.route('/')
def testing():
    return render_template(
        'base.html',
        title='Home',
        about=about.ABOUT,
        projects=projects.PROJECTS,
        experience=experience.EXPERIENCE,
        skills=skills.SKILLS,
        education=education.EDUCATION,
        certifications=certifications.CERTIFICATIONS
    )


@app.route('/secret')
def secret():
    return render_template('secret.html', title='Secret')


@app.route('/helloworld')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
