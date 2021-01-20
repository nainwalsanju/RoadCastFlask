from flask import Flask,render_template,request
from flask_migrate import Migrate
from models import db, InfoModel, AuthorModel
from flask import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pass@localhost:5432/flask"
app.config['SQLALCHEMY_BINDS']={
    'db2': 'mysql://root:pass@localhost:3306/flask'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
 
@app.route('/')
def form():
    books = InfoModel.query.all()
    authors= AuthorModel.query.all()
    return render_template("form.html", books=books, authors=authors)
 
 
@app.route('/addBook', methods = ['POST', 'GET'])
def addBook():
    if request.method == 'GET':
        books = InfoModel.query.all()
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        author=request.form['author']
        price=request.form['price']
        new_book = InfoModel(name=name, year=year,author=author,price=price)
        db.session.add(new_book)
        db.session.commit()
        return redirect("/")

@app.route('/addAuthor', methods = ['POST', 'GET'])
def addAuthor():
    if request.method == 'GET':
        books = InfoModel.query.all()
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_author = AuthorModel(name=name, age=age)
        db.session.add(new_author)
        db.session.commit()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)