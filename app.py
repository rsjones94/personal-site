from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)