""" MadLibs Application Server """

from flask import Flask, request, render_template
from stories import story, Story

app = Flask(__name__)


@app.route("/")
def welcome():
    """ MadLibs Welcome Page """
    """ Welcome page handles the request for the prompts required by the story """

    return render_template("welcome.html", prompts=story.prompts)


@app.route("/story")
def your_story():
    """ story Page

        story page intakes the prompts provided in the welcome page and uses them
        to generate the story.

    """

    # using story prompts, loop through the query string for each value.
    answers = {}
    for prompt in story.prompts:
        # get the value from args for the prompt.
        answers[prompt] = "<strong>" + \
            request.args.get(prompt, "") + "</strong>"

    # Perform some cleanup -- remove the new line (\n) and change all "  " to " ".
    generated_story = story.generate(answers).strip("\n").replace("  ", " ")

    return render_template("story.html", my_story=generated_story)
