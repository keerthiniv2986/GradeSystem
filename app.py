
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Grade System</title>
    </head>
    <body>
        <h1>Grade System</h1>
        <h2>Roll Number: 24MIS0018</h2>

        <h3>Enter Student Marks</h3>

        <form action="/result" method="POST">

            <label>Mathematics:</label>
            <input type="number" name="maths"
                   min="0" max="100" required><br><br>

            <label>Computer Science:</label>
            <input type="number" name="cs"
                   min="0" max="100" required><br><br>

            <label>Physics:</label>
            <input type="number" name="physics"
                   min="0" max="100" required><br><br>

            <label>English:</label>
            <input type="number" name="english"
                   min="0" max="100" required><br><br>

            <label>Chemistry:</label>
            <input type="number" name="chemistry"
                   min="0" max="100" required><br><br>

            <button type="submit">Submit Marks</button>

        </form>
    </body>
    </html>
    """

@app.route("/result", methods=["POST"])
def result():

    maths = float(request.form["maths"])
    cs = float(request.form["cs"])
    physics = float(request.form["physics"])
    english = float(request.form["english"])
    chemistry = float(request.form["chemistry"])

    marks = [maths, cs, physics, english, chemistry]

    if any(mark < 0 or mark > 100 for mark in marks):
        return "Error: Marks must be between 0 and 100", 400

    return f"""
    <h1>Grade System</h1>
    <h2>Roll Number: 24MIS0018</h2>

    <h3>Marks Submitted Successfully!</h3>

    <p>Mathematics: {maths}</p>
    <p>Computer Science: {cs}</p>
    <p>Physics: {physics}</p>
    <p>English: {english}</p>
    <p>Chemistry: {chemistry}</p>

    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
