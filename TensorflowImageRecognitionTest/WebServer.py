from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app
@app.route('/')
def hello_world():
    return "Hello_world"

@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website')
    return '''Language given: {}
              The Framework: {}
              The Website: {}'''.format(language, framework, website)

@app.route('/form-example', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '<h1>The language is {}.
                    The framework is {}.
                    </h1>'.format(language, framework, website)

    return '''<form method="POST">
    Language <input type="text" name="language">
    Framework <input type="text" name="framework">
    <input type="submit"
    </form>'''

if __name__ == '__main__':
    print("running server")
    app.run(port=3000) #run app in debug mode on port 5000
