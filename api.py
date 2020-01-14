import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

feedbackList = [
    {
        'id': 0,
        'description': 'Sample feedback 0'
    },
    {
        'id': 1,
        'description': 'Sample feedback 1'
    },
    {
        'id': 2,
        'description': 'Sample feedback 2'
    }
]

@app.route('/api/v1/resources/feedback/all', methods=['GET'])
def api_all():
    return jsonify(feedbackList)

@app.route('/api/v1/resources/feedback', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for feedback in feedbackList:
        if feedback['id'] == id:
            results.append(feedback)

    return jsonify(results)

app.run()