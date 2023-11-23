from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

# Base de datos
data_base = pymysql.connect(host='viaduct.proxy.rlwy.net',
                            port=51991,
                            user='root',
                            password='eggh-22cgFb-gBg4aH6DfFAC14edeFC6',
                            db='railway')


@app.route("/")
def index():
    cursor_db = data_base.cursor()
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
