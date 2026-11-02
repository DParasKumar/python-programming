from flask import Flask

print("Hello, World!")
print("This is my first Python program.")

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask!"


if __name__ == "__main__":
    app.run(debug=True)