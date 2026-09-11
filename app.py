from flask import Flask, render_template_string
import json

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>African Language AI Data Marketplace</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f5f7fa;
            color: #222;
        }
        header {
            background: #173f5f;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        header h1 {
            margin: 0 0 10px;
        }
        .container {
            max-width: 900px;
            margin: 30px auto;
            padding: 0 20px;
        }
        .dataset {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .button {
            display: inline-block;
            background: #f4a261;
            color: white;
            padding: 12px 20px;
            border-radius: 6px;
            text-decoration: none;
            margin-top: 10px;
        }
        footer {
            text-align: center;
            padding: 30px;
            color: #666;
        }
    </style>
</head>
<body>

<header>
    <h1>African Language AI Data Marketplace</h1>
    <p>High-quality African-language datasets for the next generation of AI.</p>
</header>

<div class="container">
    <h2>Available Datasets</h2>

    {% for dataset in datasets %}
    <div class="dataset">
        <h3>{{ dataset["language"] }} Dataset</h3>
        <p><strong>Type:</strong> {{ dataset["type"] }}</p>
        <p>{{ dataset["description"] }}</p>
        <p><strong>Status:</strong> {{ dataset["status"] }}</p>
        <p><strong>License:</strong> {{ dataset["license"] }}</p>
        <a class="button" href="#">View Dataset</a>
    </div>
    {% endfor %}
</div>

<footer>
    African Language AI Data Marketplace — MVP
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    with open("datasets.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return render_template_string(
        HTML,
        datasets=data["datasets"]
    )

if __name__ == "__main__":
    app.run(debug=True)
