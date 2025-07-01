from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    with open("home.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    message = request.form['message']
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Thank You</title>
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        <div class="thank-you">
            <h2>Thank You, {name}!</h2>
            <p>Your message has been received:</p>
            <blockquote>{message}</blockquote>
            <a href="/" class="back-button">← Back to Home</a>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
