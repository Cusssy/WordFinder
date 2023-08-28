from flask import Flask, render_template, request, escape
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['whisper_db']
collection = db['whisper_results']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        
        results = collection.find({'resultado_whisper': {'$regex': query}})
        count = collection.count_documents({'resultado_whisper': {'$regex': query}})

        if count > 0:
            return render_template('results.html', query=query, results=results, count=count)
        else:
            return render_template('no_results.html', query=query)

    return render_template('index.html', escape=escape)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
