from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/search")
def search():
    return render_template('index.html')

@app.route("/recommend")
def recommend():
    return "Recommendation"

if __name__ == '__main__':
    app.run(debug=False)