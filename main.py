import os
import whisper
import time
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_KEY')
model = whisper.load_model("base")


def transcriber(audio_path):
    audio = whisper.load_audio(audio_path)
    result = model.transcribe(audio)
    results = result["segments"]
    return results


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def format_transcript(results):
    final_transcript = []
    for output in results:
        timestamp = f'[{convert(output["start"])} --> {convert(output["end"])}]'
        transcribed = output["text"]
        section = f"{timestamp}{transcribed}\n"
        final_transcript.append(section)
    return final_transcript


def list_to_string(list_entry):
    string = ""
    for i in list_entry:
        string += str(i)
    return string

final_results = transcriber("path")
clean_transcript = format_transcript()
# convert_transcript_to_txt = list_to_string(final_transcript)


def write_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


# write_to_file(convert_transcript_to_txt, 'tlhaks.txt')


@app.route("/")
def home():
    return render_template("index.html", trans=convert_transcript_to_txt)


if __name__ == "__main__":
    app.run(debug=True)
