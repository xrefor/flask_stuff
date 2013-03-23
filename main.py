from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.secret_key='baconaaakka'

@app.route('/')
def get():
  return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def post():
  if request.method == 'POST':
    return 'you have written %s' % request.form['command']
  else:
    return 'no'

if __name__ == '__main__':
  app.run(debug=True)
