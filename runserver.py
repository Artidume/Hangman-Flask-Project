from flask import Flask, render_template, request, redirect, url_for
from random import randint
import hangman 
app = Flask(__name__)
#fill up the list with the words
with open("WordList.csv","r") as f:
    wordlist=[]
    line = f.readline().strip()
    while line!="":
        wordlist.append(line.upper())
        line=f.readline().strip()


@app.route("/")
def main_page():
    global letters_left
    global lives
    global correct_letters
    global word
    global short_word
    letters_left=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lives=10
    correct_letters = []
    word = wordlist[randint(0,len(wordlist)-1)]
    short_word = []
    for word_letter in word:
        if word_letter in letters_left:
            if word_letter not in short_word:
                short_word.append(word_letter)
    #print(short_word)
    render_output = hangman.render(correct_letters,word)
            
    return render_template("man.html", num=10-lives,letters_left=letters_left, word=word,show=False, render_output=render_output)

@app.route("/main")
def mainer_pager():
    try:
        global letters_left
        global lives
        render_output = hangman.render(correct_letters,word)
        return render_template("man.html", num=10-lives, letters_left=letters_left,word=word, show=False, render_output=render_output)
    except:
        return redirect("/")
@app.route("/data",methods=["POST"])
def deal_with_data():
    try:
        global letters_left
        global lives
        global correct_letters
        global word
        global short_word
        guess = request.form["guess"].upper()
        if guess not in letters_left:
            return render_template("error.html") 
        isInWord = hangman.validate(guess,word)
        letters_left=hangman.remove_letter(guess, letters_left)
        if isInWord:
            correct_letters.append(guess)
            
            if len(correct_letters)==len(short_word):
                return render_template("WIN.html", word=word)
        else:
            lives-=1
        render_output = hangman.render(correct_letters,word)
        return render_template("man.html",num=10-lives, letters_left=letters_left,correct_letters=correct_letters, show=False, render_output=render_output)
    except:
        return redirect("/")



app.run()