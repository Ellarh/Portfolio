from flask import Flask, render_template, request, url_for, redirect
import os
import datetime
import smtplib
app = Flask(__name__)

EMAIL = os.environ.get("DETAILS_EMAIL")
PASSWORD = os.environ.get("DETAILS_P")
@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", current_year=year)


@app.route("/random-things")
def random_things():
    return render_template("random.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name'),
        email = request.form.get('email'),
        subject = request.form.get('subject'),
        message = request.form.get('message')

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=f"{email}",
                                to_addrs=EMAIL,
                                msg=f"Subject: {subject}\n\n My name is: {name} \n {message}")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)