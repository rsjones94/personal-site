from flask import Flask, render_template, url_for, request

from flask_mail import Message, Mail

from forms import ContactForm


app = Flask(__name__)

app.secret_key = '10doublecross2016DEV'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'
 
Mail.init_app(app)

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
      return 'Form posted.'
 
  elif request.method == 'GET':
      return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', title='Whoops! 404'), 404

if __name__ == '__main__':
    app.run(debug=True)
