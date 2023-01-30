import turtle_graphics
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def main():
    turtle_graphics.write_file(turtle_graphics.rectangle, "rectangle.svg", 500, 500, 100)
    return send_file("rectangle.svg")

if __name__ == "__main__":
    app.run(host="172.17.0.4", port=8030)
