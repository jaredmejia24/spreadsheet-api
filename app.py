from flask import Flask, request
import pandas
SHEET_URL = "https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/gviz/tq?tqx=out:csv"

app = Flask(__name__)


def controller_users():

    file = pandas.read_csv(SHEET_URL)

    return {"status": "success", "user_amount": len(file)}


@app.route("/users")
def users():
    res = controller_users()
    return res


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
