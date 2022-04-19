"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
import json
from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file, redirect, flash, session, abort, send_from_directory, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
import os
from .models import *
from .forms import *
from sqlalchemy import or_, and_
from flask_wtf.csrf import generate_csrf

def get_uploaded_images():
    image_types = ['jpg', 'png', 'jpeg', 'gif', 'svg', 'webp']
    
    upload_dir = app.config.get('UPLOAD_FOLDER')
    uploads = sorted(os.listdir(upload_dir))

    #this is done to only show file types in image_types list
    cleaned = [img for img in uploads if any(sub in img for sub in image_types)]
    return cleaned

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route('/api/uploads/<filename>')
def get_image(filename):
    upload_dir =  os.path.join(os.getcwd(), app.config.get('UPLOAD_FOLDER'))
    return send_from_directory(upload_dir, filename,)

@app.route("/api/register", methods=["GET", "POST"])
def register():

    form = UserForm()

    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            name = form.name.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            photo = form.photo.data
            
            photoname = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photoname))
            #photo.save(app.config.get('UPLOAD_FOLDER'))

            user = Users(username=username, password=password, name=name, email=email, location=location, biography=biography, photo=photoname)
            db.session.add(user)
            db.session.commit()
            return jsonify({'status': 200})

        else:
            err = {
                "errors": form_errors(form),
                'type': 'bad'
            }

            return jsonify(err)

@app.route("/api/cars", methods=["GET", "POST"])
def cars():

    form = CarForm()

    if request.method == "POST":
        if form.validate_on_submit():
            description = form.description.data
            make = form.make.data
            model = form.model.data
            colour = form.colour.data
            year = form.year.data
            transmission = form.transmission.data
            car_type = form.car_type.data
            price = form.price.data
            user_id = form.user_id.data
            photo = form.photo.data
            
            names = []
            for p in photo:
                photoname = secure_filename(p.filename)
                names.append(photoname)
                p.save(os.path.join(app.config['UPLOAD_FOLDER'], photoname))
                #photo.save(app.config.get('UPLOAD_FOLDER'))

            names = '/t'.join(x for x in names)

            

            car = Cars(description=description,_make=make, model=model, colour=colour, year=year, transmission=transmission, car_type=car_type, price=price, user_id=user_id, photo=names)
            db.session.add(car)
            db.session.commit()
            return jsonify({'status': 200})
        else:
            err = {
                "errors": form_errors(form),
                'type': 'bad'
            }

            return jsonify(err)

    carfiles = Cars.query.all()
    
    return jsonify(carfiles)


@app.route("/api/cars/<car_id>", methods=["GET"])
def getcar(car_id):
    file = Cars.query.filter_by(id=car_id).first()
    return jsonify(file)

@app.route("/api/cars/<car_id>/favourite", methods=["POST"])
def favcar(car_id):
    if request.method == 'POST':
        fav = Favourites(car_id=car_id, user_id=int(current_user.get_id()))
        db.session.add(fav)
        db.session.commit()
        return jsonify({'status': 200})

#-----------------------This should be a GET method-------------------------------->>>
@app.route("/api/search", methods=["GET", 'POST'])
def search():

    if request.method == "POST":
        make = request['make']
        model = request['model']
        files = db.session.query(Cars).filter(or_(Cars.make.like(make), Cars.model.like(model)))
        #files = db.session.query(Cars).filter(or_(Cars.make == make, Cars.model == model))
        return jsonify(files)

@app.route('/api/users/<user_id>', methods=["GET"])
def getUser(user_id):
    user = Users.query.filter_by(id=user_id).first()
    return jsonify(user)


@app.route('/api/users/<user_id>/favourites', methods=["GET"])
def getFavs(user_id):
    favs = Favourites.query.filter_by(user_id=user_id)
    return jsonify(favs)




@app.route("/api/auth/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return jsonify({'status':200})

    form = LoginForm()

    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit():
            # Get the username and password values from the form.
            username = form.username.data
            password = form.password.data

            # using your model, query database for a user based on the username
            # and password submitted. Remember you need to compare the password hash.
            # You will need to import the appropriate function to do so.
            # Then store the result of that query to a `user` variable so it can be
            # passed to the login_user() method below.
            user = Users.query.filter_by(username=username).first()

            if user != None and check_password_hash(user.password, password):
                # get user id, load into session
                login_user(user)

                return jsonify({'status':200})
            else:
                return jsonify({'status':400})
        else:
            err = {
                "errors": form_errors(form),
                'type': 'bad'
            }

            return jsonify(err)


@app.route("/api/auth/logout")
@login_required
def logout():
    logout_user()
    flash('Logout Successful', 'success')
    return jsonify({'status':200})


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))



###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")