from flask import Flask

app = Flask(__name__)


@app.route('/cube_summation', methods=['GET', 'POST'])
def cube_summation():
    # TODO: add logic to call cube summation
    return ''


if __name__ == 'main':
    app.run()


    

