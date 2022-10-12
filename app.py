from flask import Flask, render_template, jsonify

app = Flask(__name__,template_folder='templates')

JOBS=[
  {
    'Company':'KPMG',
    'title':'Junior Data Analyst',
    'Salary':'7.6LPA',
    'Location': 'Bengaluru, Karnataka'
  },
  {
    'Company':'Walmart',
    'title':'Data Scientist',
    'Salary':'13LPA',
    'Location': 'Delhi, India'
  },
  {
    'Company':'Currenex State Street Trust Company',
    'title':'Data Analyst',
    'Location': 'Bengaluru, Karnataka'
  },
  {
    'Company':'Shell',
    'title':'Data Analyst-MDM',
    'Salary':'4.2LPA',
    'Location': 'Bengaluru, Karnataka'
  }
]
@app.route('/')
def hello():
    return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)