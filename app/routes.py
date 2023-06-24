from flask import Flask, request         # from the flask module import the Flask class
# OOP

app = Flask(__name__)           # Create an instance of Flask into app (now an object)
USERS = []

# variables that belong to a class are called "attributes"
# functions that belong to a class are called "methods"

@app.get("/users/<int:user_id>")       # with url parameter
@app.get("/<int:user_id>")             # we now have access to the object's methods (also a decorator)
def main(user_id):                     # A wrapped function is called a view function in flask.
    me = {}
    not_found = True
    if user_id == 1:
        not_found = False
        me = {
            "first_name": "Rafael",
            "last_name": "GPL",
            "hobbies": "DIY stuff",
            "is_active": True
        }
    if not_found:
        return me, 404          # when we return a python dictionary from a view function,
                                # flask will automatically convert it to JSON
    return me

@app.get("/users/")
def get_users():
    return USERS

@app.post("/users/")
def create_user():
    raw_data = request.json
    USERS.append(raw_data)
    return 201, {"message": "created"}

# REST
# Architectural guide for building network connected APIs
# Representational State Transfer

# Endpoints are named after the resource they manage, but in plural noun form.
# Examples:
# /users
# /pets
# /products

# They help us support CRUD(S) operations
# CREATE  -> POST
# READ    -> GET (intended to retrieve a single resource)
# UPDATE  -> PUT/PATCH
# DELETE  -> DELETE
# (SCAN)  -> GET (intended to retrieve multiple resources)

