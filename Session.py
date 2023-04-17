from flask import Flask, session

app = Flask(__name__)

@app.route("/")

def index():

  # Get the session data

  session_id = session.get("session_id")

  user_id = session.get("user_id")

  # If the session id is not set, redirect to the login page

  if not session_id:

    return redirect("/login")

  # If the user id is not set, redirect to the home page

  if not user_id:

    return redirect("/home")

  # Display the user's name

  return f"Hello, {user_id}"

@app.route("/login")

def login():

  # Get the username and password from the request

  username = request.args.get("username")

  password = request.args.get("password")

  # Check if the username and password are valid

  if username == "admin" and password == "password":

    # Create a new session for the user

    session["session_id"] = os.urandom(16)

    session["user_id"] = "admin"

    # Redirect the user to the home page

    return redirect("/home")

  # Otherwise, redirect the user to the login page

  return redirect("/login?error=Invalid username or password")

@app.route("/logout")

def logout():

  # Delete the session data

  session.pop("session_id")

  session.pop("user_id")
 
