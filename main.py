from flask import Flask,render_template,redirect,request,url_for
from configs.base_config  import Development,Staging,Production
import psycopg2


# Connect to an existing database
conn = psycopg2.connect(dbname="test254", user="postgres", password="nelsonkimathi123")


# Open a cursor to perform database operations
cur = conn.cursor()


# Execute a command: this creates a new table
cur.execute("CREATE TABLE IF NOT EXISTS users(fname varchar,lname varchar, email varchar);")

app = Flask(__name__)
app.config.from_object(Development)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form['last_name']
        email = request.form['email_address']
        cur.execute("INSERT INTO users(fname,lname,email) VALUES (%s, %s, %s)",(fname,lname,email))
       
        conn.commit()
        return redirect(url_for("register"))
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print(rows)
    return render_template("sample.html", details = rows)


if __name__== "__main__":
    app.run(debug=True)