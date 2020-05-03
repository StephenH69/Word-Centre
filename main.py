from random import randint
from time import strftime
from flask import Flask, render_template, flash, request, Markup, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import re
import defs


DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField('Surname:', validators=[validators.required()])


class ReusableFormLetters(Form):
    phrase = TextField('Phrase:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    return redirect("/wordsinword", code=302)


@app.route("/pig-latin", methods=['GET', 'POST'])
def pig():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            #defs.write_to_disk('Pig Latin', phrase)
            flash('Hello: {}'.format(phrase))
            pig = defs.pig_it(phrase)
            return render_template('pages/pig.html', form=form, translation=pig, entry=phrase)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/pig.html', form=form)


@app.route("/missing-letters", methods=['GET', 'POST'])
def missing():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            #defs.write_to_disk('Missing Letters', phrase)
            flash('Hello: {}'.format(phrase))
            potentialAnswers = defs.missing_letter(phrase)
            return render_template('pages/missing_letters.html', form=form, answers=potentialAnswers, entry=phrase)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/missing_letters.html', form=form)


@app.route("/anagram", methods=['GET', 'POST'])
def anagram_solver():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            #defs.write_to_disk('Anagram Solver', phrase)
            flash('Hello: {}'.format(phrase))
            potentialAnswers = defs.anagram_s(phrase)
            return render_template('pages/anagram.html', form=form, answers=potentialAnswers, entry=phrase)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/anagram.html', form=form)


@app.route("/wordsinword", methods=['GET', 'POST'])
def wordsinword():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            #defs.write_to_disk('Words in a Word', phrase)
            flash('Hello: {}'.format(phrase))
            potentialAnswers = defs.words_in_word(phrase)
            i = len(potentialAnswers)
            returnMessage = defs.results_formating(potentialAnswers)
            return render_template('pages/wordsinword.html', form=form, answers=returnMessage, entry=phrase, totalresults=i)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/wordsinword.html', form=form)


@app.route("/wordsstartingwith", methods=['GET', 'POST'])
def wordsstartingwith():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            flash('Hello: {}'.format(phrase))
            potentialAnswers = defs.words_starting_with(phrase)          
            i = len(potentialAnswers)
            returnMessage = defs.results_formating(potentialAnswers)
            return render_template('pages/wordsstartingwith.html', form=form, answers=returnMessage, entry=phrase, totalresults=i)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/wordsstartingwith.html', form=form)


@app.route("/wordscontaining", methods=['GET', 'POST'])
def wordscontaining():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            flash('Hello: {}'.format(phrase))
            potentialAnswers = defs.words_containing(phrase)          
            i = len(potentialAnswers)
            returnMessage = defs.results_formating(potentialAnswers)
            return render_template('pages/wordscontaining.html', form=form, answers=returnMessage, entry=phrase, totalresults=i)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/wordscontaining.html', form=form)


@app.route("/wordsending", methods=['GET', 'POST'])
def wordsending():
    form = ReusableFormLetters(request.form)
    # print(form.errors)
    if request.method == 'POST':
        phrase = request.form['phrase'].lower()
        if form.validate():
            flash('Hello: {}'.format(phrase))
            potentialAnswers = defs.words_ending(phrase)          
            i = len(potentialAnswers)
            returnMessage = defs.results_formating(potentialAnswers)
            return render_template('pages/wordsending.html', form=form, answers=returnMessage, entry=phrase, totalresults=i)
        else:
            flash('Error: All Fields are Required')
    return render_template('pages/wordsending.html', form=form)


if __name__ == "__main__":
    app.run()
