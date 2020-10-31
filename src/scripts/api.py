from flask import Flask, request

app = Flask("composia")


@app.route("/", methods=["GET"])
def helloWorld():
    return{"Hello": "World"}


@app.route("/test", methods=["POST"])
def test():

    body = request.get_json()
    print(body)

    return body


app.run()
