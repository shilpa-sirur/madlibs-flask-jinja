from random import choice

from flask import Flask, render_template, request



# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    answer = request.args.get("play")

    if answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html") 

@app.route('/madlib', methods=["POST"])
def show_madlib():

    peep = request.form.get("person")
    colors = request.form.get("color")
    nouns = request.form.get("noun")
    adjectives = request.form.get("adjective")
    verbs= request.form.get("verb")
    bodyparts= request.form.getlist("bodypart[]")
    


    return render_template("game.html", person=peep, color=colors, noun=nouns, adjective=adjectives, verb=verbs, bodyparts=bodyparts)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
