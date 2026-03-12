
from flask import Flask, render_template, request

app = Flask("Newsletter")

anmeldungen = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/anmelden", methods=["POST"])
def anmelden():
    name = request.form['name']
    email = request.form['email']
    geburtsjahr = request.form['geburtsjahr']
    
    anmeldungen.append({"name": name, "email": email, "geburtsjahr": geburtsjahr})
    return render_template("feedback.html", name=name)

@app.route("/anmeldungen")
def anmledungen_liste():
    return render_template("anmeldungen.html", anmeldungen=anmeldungen)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
