from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'   # A db in this current project folder
db = SQLAlchemy(app)    # Initialize the database

# Create the model for tb
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # call the below function for every new task created.
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    # Handling specific routes
    if request.method == 'POST':
        task_name = request.form['task_name']   # Get the task_name from the form
        new_task = Todo(taskname=task_name)     # Insert a new task in the db

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'An error occoured in adding a new task'
    else:
        # Get all the tasks stored in the database to display to the user
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>') # using id as the unique identifier, it becomes variable like in expressjs
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'An error occured in deleting the task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    if request.method=='POST':
        task_to_update.taskname = request.form['task_name']
        print(request.form['task_name'])
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'An error occured in updating the task '
    else:
        return render_template('update.html', task=task_to_update)

if __name__ == '__main__':
    app.run(debug=True)