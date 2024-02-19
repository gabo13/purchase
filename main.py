
import sqlite3
import random
from flask import Flask, render_template, g, request, redirect

app = Flask(__name__)

DATABASE = "2024.db"
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods= ['GET', 'POST'])
def index():
    with app.app_context():
        c = get_db().cursor()
        #fill_table(c,256)
        if request.method == 'GET':
            c.execute("SELECT * FROM spend order by month, day;")
            rows = c.fetchall()
            return render_template('index.html', vasarlasok = rows)
        if request.method == 'POST':
            c.execute( '''INSERT INTO spend
                       (month, day, shop,cost, comment)
                       VALUES (?,?,?,?,?);''',
                       (request.form.get('month', type= int),
                        request.form.get('day', type= int),
                        request.form.get('shop'),
                        request.form.get('cost', type= float),
                        request.form.get('comment')
                       )
                     )
            c.connection.commit()
    return redirect('/')
def create_table(c):
    c.execute("DROP TABLE IF EXISTS spend")
    c.execute( '''CREATE TABLE IF NOT EXISTS spend
               (ID INTEGER PRIMARY KEY,
               month INTEGER NOT NULL,
               day INTEGER NOT NULL,
               shop TEXT NOT NULL,
               cost REAL,
               comment TEXT); 
               ''')

def create_record(c, month, day, shop, cost, comment='NULL'):
    c.execute( '''INSERT INTO spend
               (month, day, shop, cost, comment)
               VALUES ( ?, ?, ?, ?, ?);
               ''',(month, day, shop, cost, comment))

def fill_table(c, num_records = 200):
    create_table(c)
    shops = ['TESCO','COOP','ALDI','LIDL','C&A','REAL','MEDIA MARKT']
    cloths = ['nadrág','póló','pulcsi']
    c.execute("BEGIN TRANSACTION")
    for _ in range(num_records):
        pass
        month = random.randint(1,2)
        day = random.randint(1,29)
        shop = random.choice(shops)
        cost = random.randint(1,150)*100
        match shop:
            case 'C&A':
                comment = random.choice(cloths)
            case 'MEDIA MARKT':
                comment = 'kütyü'
            case _:
                comment = ''
        #c.execute("BEGIN TRANSACTION;")
        create_record(c,month,day,shop,cost,comment)
        #print(month,day,shop,cost,comment)
    c.execute("COMMIT")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 8080, debug= True)
