from flask import Flask, jsonify, request
from flask_cors import CORS
import pycantonese as pc
import utils

app = Flask(__name__)
CORS(app)


def init():
    global corpus
    corpus = pc.hkcancor()


@app.route("/segment", methods=["POST"])
def segment_text():
    data = request.json
    segmented = pc.segment(data["text"])
    return jsonify(segmented)

@app.route("/stop-words", methods=["GET"])
def stop_words():
    sw = list(pc.stop_words())
    return jsonify(sw)


@app.route("/search", methods=["POST"])
def search():
    data = request.json
    tokens = [
        {
            "word": token.word,
            "pos": token.pos,
            "jyutping": token.jyutping,
        }
        for token in corpus.search(**data)
    ]
    # Remove duplicated token.
    tokens = [dict(t) for t in set(tuple(token.items()) for token in tokens)]
    return jsonify(tokens)


@app.route("/jyutping", methods=["POST"])
def jyutping():
    data = request.json
    jyutping_list = pc.characters_to_jyutping(data["text"])
    return jsonify(jyutping_list)


@app.route("/parse", methods=["POST"])
def parse():
    data = request.json
    result = pc.parse_text(data["text"])
    tokens = [
        {
            "word": token.word,
            "pos": token.pos,
            "jyutping": token.jyutping,
        }
        for r in result.utterances()
        for token in r.tokens
    ]
    return jsonify(tokens)

@app.route("/asr", methods=["POST"])
def asr():
    data = request.files
    resp = utils.sentence_recognition(data["file"])
    return jsonify(resp)

if __name__ == "__main__":
    init()
    app.run(debug=True, port=8090)
