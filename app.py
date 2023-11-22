from flask import Flask, render_template, request
from textSummarizer import summarizer
from getDataFromURL import getData

app = Flask(__name__)


@app.route('/')
@app.route('/res', methods=['GET', 'POST'])
def index():

    textarea_data = ""
    output_data = ""
    if request.method == 'POST':
        url = request.form['url']
        if url != "":
            textarea_data = getData(url)
        else:
            textarea_data = request.form['input']
        output_data = summarizer(textarea_data)

    return render_template("index.html", input_data=textarea_data, output_data=output_data)
