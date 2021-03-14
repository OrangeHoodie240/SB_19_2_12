from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story')
def get_story():
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    plural_noun = request.args.get('pluralNoun')
    answers = {'place': place, 'noun': noun, 'verb': verb, 'adjective': adjective, 'plural_noun': plural_noun}
    return render_template('displayStory.html', story=story.generate(answers))
