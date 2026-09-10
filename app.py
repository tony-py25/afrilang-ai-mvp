from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

datasets = [
    {
        "id": 1,
        "name": "Kiswahili Conversational Speech Dataset",
        "language": "Kiswahili",
        "type": "Speech",
        "country": "Kenya",
        "description": "High-quality Kiswahili conversational speech data for AI speech recognition and voice applications.",
        "price": 500
    },
    {
        "id": 2,
        "name": "Kikuyu Text Dataset",
        "language": "Kikuyu",
        "type": "Text",
        "country": "Kenya",
        "description": "Kikuyu language text samples suitable for language-model research and NLP applications.",
        "price": 300
    },
    {
        "id": 3,
        "name": "Dholuo Translation Dataset",
        "language": "Dholuo",
        "type": "Translation",
        "country": "Kenya",
        "description": "Dholuo-English translated sentences for machine translation and language AI.",
        "price": 400
    },
    {
        "id": 4,
        "name": "Hausa Conversational Dataset",
        "language": "Hausa",
        "type": "Speech",
        "country": "Nigeria",
        "description": "Hausa conversational language data for speech and conversational AI research.",
        "price": 450
    },
    {
        "id": 5,
        "name": "Amharic NLP Dataset",
        "language": "Amharic",
        "type": "Text",
        "country": "Ethiopia",
        "description": "Amharic text data for natural-language-processing applications.",
        "price": 350
    }
]


@app.route("/")
def home():
    return render_template("home.html", datasets=datasets)


@app.route("/datasets")
def dataset_list():
    query = request.args.get("q", "").lower()
    language = request.args.get("language", "")
    data_type = request.args.get("type", "")

    filtered = datasets

    if query:
        filtered = [
            d for d in filtered
            if query in d["name"].lower()
            or query in d["language"].lower()
            or query in d["description"].lower()
        ]

    if language:
        filtered = [d for d in filtered if d["language"] == language]

    if data_type:
        filtered = [d for d in filtered if d["type"] == data_type]

    languages = sorted(set(d["language"] for d in datasets))
    types = sorted(set(d["type"] for d in datasets))

    return render_template(
        "datasets.html",
        datasets=filtered,
        languages=languages,
        types=types
    )


@app.route("/dataset/<int:dataset_id>")
def dataset_detail(dataset_id):
    dataset = next(
        (d for d in datasets if d["id"] == dataset_id),
        None
    )

    if dataset is None:
        return "Dataset not found", 404

    return render_template("detail.html", dataset=dataset)


@app.route("/request-license/<int:dataset_id>", methods=["GET", "POST"])
def request_license(dataset_id):
    dataset = next(
        (d for d in datasets if d["id"] == dataset_id),
        None
    )

    if dataset is None:
        return "Dataset not found", 404

    if request.method == "POST":
        return render_template(
            "checkout.html",
            dataset=dataset,
            submitted=True
        )

    return render_template(
        "checkout.html",
        dataset=dataset,
        submitted=False
    )


@app.route("/contributor")
def contributor():
    return render_template("contributor.html")


@app.route("/buyer")
def buyer():
    return render_template("buyer.html")


if __name__ == "__main__":
    app.run(debug=True)
