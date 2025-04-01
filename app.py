from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    
    if request.method == 'POST':
        movie_name = request.form.get("movie_name", "").strip()
        if movie_name:
            recommendations = [
                f"{movie_name} - Part 2",
                f"Similar to {movie_name}",
                "Another Great Movie",
                "Top Trending Movie"
            ]
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
