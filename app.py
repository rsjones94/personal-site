import os

from flask import Flask, render_template, url_for, request
from flask_mail import Message, Mail

from forms import ContactForm


app = Flask(__name__)

app.secret_key = '10doublecross2016DEV'

"""
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_APP_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)
"""

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/pyfluv")
def pyfluv():
    return render_template('pyfluv.html', title='pyfluv')

@app.route("/ecotrajectory")
def ecotrajectory():
    return render_template('ecotrajectory.html', title='ecotrajectory')

@app.route("/newman")
def molec_strain():
    return render_template('molec-strain.html', title='Newman Projection')

@app.route("/geoengine")
def geoengine():
    return render_template('geoengine.html', title='KCI Geoengine')

@app.route("/fuzzypeach")
def fuzzypeach():
    return render_template('fuzzypeach.html', title='fuzzyPeach')

@app.route("/more-projects")
def more_projects():
    return render_template('more-projects.html', title='More Projects')

@app.route("/pet-therapy")
def pet_therapy():
    return render_template('pet-therapy.html', title='Pet Therapy')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if request.method == 'POST':
        
        try:
            the_body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
              
            with app.app_context():
                msg = Message(subject=form.subject.data+' - (skyjonesdev contact form)',
                              sender=app.config.get("MAIL_USERNAME"),
                              recipients=["rsajones94@gmail.com"],
                              body=the_body)
                mail.send(msg)
             
            return render_template('contact.html', success=True)
        except:
            return "Contact forms are down right now. We're working on it!"
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', title='Whoops! 404'), 404

if __name__ == '__main__':
    app.run(debug=True)
