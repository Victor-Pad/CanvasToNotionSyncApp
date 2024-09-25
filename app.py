from flask import Flask, render_template, redirect, url_for
import os


def load_env_file():
    """
    Loads enviroment variable from an .env file.
    """
    if os.path.exists('.env'):
        with open('.env') as f:
            for line in f:
                if line.strip():
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value


load_env_file()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
