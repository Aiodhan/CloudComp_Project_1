# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('layout.html')

@app.route("/engage", methods=["GET","POST"])
def engage():
    """Renders the contact page."""
    return render_template("engage.html")

@app.route('/journy',methods=["GET","POST"])
def journy():
    """Renders the about page."""
    return render_template('journy.html'  )

@app.route('/ala',methods=["GET","POST"])
def ala():
    """Renders the about page."""
    return render_template('ala.html')

@app.route('/blog',methods=["GET","POST"])
def blog():
    """Renders the about page."""
    return render_template('blog.html')

@app.route('/contact',methods=["GET","POST"])
def contact():
    """Renders the about page."""
    return render_template('contact.html')

@app.route('/about',methods=["GET","POST"])
def about():
    """Renders the about page."""
    return render_template('about.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
