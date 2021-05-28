from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import pandas as pd
import csv
import os
import json
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast
import dateutil.parser

app = Flask(__name__)
DIR_PATH = os.path.join(os.path.dirname(__file__))


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':    
    app.run(debug=True, use_reloader=True)