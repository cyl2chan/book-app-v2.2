#Login Page
from flask import Flask, redirect, request, render_template, url_for#, Response
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required


#app.secret_key = 'supersecretstring123456789'  # Required for authentication
#app.secret_key = 'super secret string'

#Blog page
import json 
import datetime
from flask import Flask, request, jsonify, render_template, redirect
from flask_mongoengine import MongoEngine
import random 

#recommend page
from flask_cors import CORS

app = Flask(__name__, template_folder='template', static_folder = 'static')
CORS(app)
"""
#for local MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'BlogApp',
    'host': 'localhost',
    'port': 27017,
    'host': 'mongodb+srv://cyl2:1PqEMHRcwhiz7lgc@clusterbookapp.xtb2gpk.mongodb.net/?retryWrites=true&w=majority'
}
app.config['SECRET_KEY'] = 'supersecretstring123456789' #'super secret string'
db = MongoEngine()
db.init_app(app)
"""
#for online MongoDB
app.config['MONGODB_HOST'] = "mongodb+srv://user2000:user2000@cluster0.q8mckwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
app.config['SECRET_KEY'] = 'supersecretstring123456789' #'super secret string'
db = MongoEngine(app)

#login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Code from following steps should be added here
# Our mock database.
"""
users = {
    {'student@ryerson.ca': {'password': 'secret'}}, 
    {'demo@gmail.com': {'password': 'demoBook'}}
    }
"""
users = {
    'student@ryerson.ca': 'secret', 
    'tryDemo@gmail.com': 'demoBook'
    }

# User class
class User(UserMixin):
    pass #placeholder for future code

    #comments = db.relationship('Comment', backref='author', lazy='dynamic')

# Login manager loads user by email from mock database
# A user loader tells Flask-Login how to get a specific user object from the ID that is stored in the session cookie
@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user  #get id from session, then retrieve user object from database with peewee query


# Login manager loads user by email from form requesting username and password
#Logging in users without replying on cookies, eg by using header values or an API key passed as a query argument
#Similar to user_loader, except it takes FLask request instead of a user_id
#https://copyprogramming.com/howto/how-is-flask-login-s-request-loader-related-to-user-loader
#
@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

# Login route that is used to access secure routes.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    #if password entered is correct (matched the password in database)
    #if email in users and request.form['password'] == users[email]['password']: 
    if email in users and request.form['password'] == users[email]: 
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))

    return 'Incorrect login'

# Protected route hence user must be logged in to access it. 
@app.route('/protected')
@login_required
def protected():
    return redirect("/library")

# Logout from current session
@app.route('/logout')
#@login_required
def logout():
    logout_user()
    return redirect(url_for('login')) 

# Handle unauthenticated users that access protected routes
@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401
    #flash("You need to login first!")
    #return redirect(url_for('login')) 



#Blog Page
class Entry(db.Document):
    entry_id = db.IntField()
    book_title = db.StringField()
    date = db.StringField()
    content = db.StringField()
    comments = db.ListField(db.ReferenceField('Comment'))
    likes = db.ListField(db.ReferenceField('Like'))
    #comments = db.relationship('Comment', backref='entry', lazy='dynamic')

    meta = {'collection' : 'Entry', 'allow_inheritance' : False}

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    entry_id = random.randint(0, 10000)
    book_title = request.form.get('book_title')
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    content = request.form.get('content')

    new_entry = Entry(entry_id=entry_id, 
        book_title=book_title, date=date, content=content)
    new_entry.save()

    #print(new_entry)
    #print(entry_id, 
        #book_title, date, content)
    return redirect("/blog")


#only for update page
@app.route('/update-modal/<ent_id>', methods=["GET"])
def update_modal(ent_id):
    entries = Entry.objects(entry_id=ent_id)    
    entry = entries.first()

    print("/update-modal/<ent_id>:", entry.entry_id, entry.book_title, entry.content)
    return render_template("modal-update.html", entry=entry) #refer to update page
    #return redirect("/blog", entry.entry_id)
    #return redirect("/blog")
    #return str(entry)

@app.route('/update', methods=['POST'])
def update_entry():
    update_entry_id = request.form.get('entry_id')
    update_book_title = request.form.get('book_title')
    update_date = datetime.datetime.today().strftime("%Y-%m-%d")
    update_content = request.form.get('content')

    entries = Entry.objects(entry_id=update_entry_id)
    entry = entries.first()

    #print(update_entry_id, update_book_title, update_date, update_content)
    #print(entry.to_json())

    if not entry:
        return ("/update: Entry id not found!")
    else: 
        entry.entry_id = update_entry_id
        entry.book_title = update_book_title 
        entry.date = update_date
        entry.content = update_content
        entry.save()

        return redirect("/blog") 


@app.route('/delete/<ent_id>')
def delete_entid(ent_id):
    entries = Entry.objects(entry_id=ent_id)
    entry = entries.first()

    print("/delete/<ent_id>:", ent_id)
    if not entry:
        return ("/delete/<ent_id>: Entry id not found!")
    else: 
        entry.delete()

    return redirect('/blog')

@app.route('/delete', methods=["POST"])
def delete_entry():
    update_entry_id = request.form.get('entry_id')

    entries = Entry.objects(entry_id=update_entry_id)
    entry = entries.first()

    if not entry:
        return ("Entry not found!")
    else:
        entry.delete()    
        return ("Deleted Entry with id:" + update_entry_id)







#comment section
class Comment(db.Document):
    comment_id = db.IntField()
    #author_id = db.IntField()
    entry_id = db.IntField()
    comment_content = db.StringField()
    comment_date = db.StringField()
    
    meta = {'collection' : 'Comment', 'allow_inheritance' : False}


@app.route('/<ent_id>/add-comment', methods=['GET', 'POST'])
@login_required
def add_comment(ent_id):
    entries = Entry.objects(entry_id=ent_id)
    print(ent_id)
    entry = entries.first()

    comt_id = request.form.get('com_id')
    print('comment ID:', comt_id)
    #com_id = random.randint(0, 10000)

    comment_content = request.form['comment_content']
    print("comment content:", comment_content) 
    
    if not comment_content:
        print('Comment cannot be empty.')
    else:
        new_comment = Comment(comment_id=comt_id, entry_id =ent_id, #author_id=author_id
            comment_content=comment_content) #comment_date=comment_date
        new_comment.save()

    return redirect('/blog')
    #return render_template('blog.html', entry_list=list(entries), comment_list=list(comments), entry=entry, comment=comment)


@app.route('/delete-comment/<com_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(com_id):
    comments = Comment.objects(comment_id=com_id)
    comment = comments.first()

    print("/delete-comment/<comment_id>:", com_id)
    if not comment:
        return ("/delete-comment/<comment_id>: Comment id not found!")
    else: 
        comment.delete()

    return redirect('/blog')




#comment section
class Like(db.Document):
    like_id = db.IntField()
    #author_id = db.IntField()
    entry_id = db.IntField()
    
    meta = {'collection' : 'Like', 'allow_inheritance' : False}

@app.route('/<ent_id>/like', methods=['GET', 'POST'])
@login_required
def like(ent_id):
    entries = Entry.objects(entry_id=ent_id)
    print("entry ID of like button: ", ent_id)
    entry = entries.first()

    lik_id = request.form.get('lik_id') #get like ID from ajax
    print('like ID:', lik_id)

    #likes = Like.objects(like_id=lik_id)
    likes = Like.objects(entry_id=ent_id)
    like = likes.first()
    
    if not like: #if there's no like of the same entry ID, generate new like w/ like ID
        new_like = Like(like_id=lik_id, entry_id =ent_id) #author_id=author_id
        new_like.save()
    else: #if entry w/ same entry ID already liked, find the like ID and delete it
        like2 = Like.objects(entry_id=ent_id)
        like2.delete()

    return redirect('/blog')



"""
@app.route('/<ent_id>/list-comment', methods=['GET', 'POST'])
def list_all_comments(ent_id, comment_content):
    entries = Entry.objects(entry_id=ent_id)
    entry = entries.first()
    comments = Comment.objects(entry_id=ent_id, comment_content=comment_content)
    comment= comments.first()

    return render_template("blog.html", entry=entry, comment_list=list(comments)) #, comment=comment)
"""
@app.route('/blog', methods=['GET'])
@login_required
def list_entries():
    entries = Entry.objects()
    entry = entries.first()

    entry_comments = {}
    entry_likes = {}
    
    for entry in entries:
        comments = Comment.objects(entry_id=entry.entry_id)
        entry_comments[entry.entry_id] = comments

        likes = Like.objects(entry_id=entry.entry_id)
        entry_likes[entry.entry_id] = likes


    return render_template('blog.html', entry_list=list(entries), 
        entry_comments=entry_comments, entry_likes=entry_likes, entry=entry) #comment=comment)


#import feedparser
import urllib.request, json 
import requests
@app.route('/get_bookbrowse_blog_feed')
@login_required
def get_bookbrowse_blog_feed():
    """"
    feed_url = "https://www.bookbrowse.com/blogs/editor/rss.cfm"
    data = urllib.request.Request(feed_url)
    with urllib.request.urlopen(data) as response:
        page = response.read()
        return page
    """
    #method #2:
    feed_url = "https://www.bookbrowse.com/blogs/editor/rss.cfm"
    data = requests.get(feed_url)
    return data.content#, data.status_code, {'Content-Type': 'application/rss+xml'}
    

@app.route('/library')
@login_required
def library_page():
    return render_template("library.html")

@app.route('/reading_challenge')
@login_required
def reading_challenge_page():
    return render_template("challenge.html")

@app.route('/recommend')
@login_required
def recommend_page():
    return render_template("recommend.html")


if __name__ == "__main__":
    """
    #for hosting locally
    app.run(host='0.0.0.0', port=5000, debug=True)
    """
    app.run() #for deployment online

