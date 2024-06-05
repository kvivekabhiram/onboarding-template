# engent endpoints for onboarding

import os, getpass, ast

from flask import Flask, jsonify, abort, request

APP = Flask(__name__)

NAME = os.environ.get('NAME', 'Twilion!')


@APP.route('/')
def welcome():
    """
    default endpoint
    """
    # generic welcome page
    # should be better

    return "Welcome to Twilio Engineering, {}".format(NAME)


@APP.route('/funfacts/', methods=['GET'])
def list_users():
    """
    lists all fun facts to date
    """
    # list all users
    users = os.listdir('funfacts')

    return jsonify({'users': users})


@APP.route('/funfacts/', methods=['POST'])
def add_fact():
    """
    post new fun fact
    """

    # abort is no json is sent
    if not request.json:
        abort(400)

    # expected json
    fun_fact = {
        'name' : request.json['name'],
        'uid' : getpass.getuser(),
        'title': request.json['title'],
        'team' : request.json['team'],
        'fun_fact': request.json['fun_fact'],
    }



    # create file with username
    name = str(fun_fact['name'])
    current_path = os.getcwd()
    file = current_path + '/funfacts/' + name

    # write data to file
    f = open(file, 'w+')
    f.write(str(fun_fact))
    f.close()

    return get_funfact(username=name), 201


@APP.route('/funfacts/<username>')
def get_funfact(username):
    """
    displays funfact of specified username
    """
    # get current directory
    current_dir = os.getcwd()
    if not current_dir.endswith('/'):
        current_dir += '/'

    filepath = current_dir + 'funfacts/{}'.format(username)

    # if file exists, display
    if os.path.exists(filepath):
        # return open(filepath, 'r').read() + '\n'
        content = open(filepath, 'r').read()
        # convert to json
        return ast.literal_eval(content)
    else:
        abort(404)


@APP.route('/pics')
def pics():
    """
    picture endpoint
    """

    return "let's see some media"


@APP.route('/battlestar')
def battlestar():
    """
    battlestar endpoint
    """

    return "Let's explore Juno"


@APP.route('/transmogrify')
def transmogrify():
    """
    string translation endpoint
    """

    return "Let's translate a string"


@APP.route('/message')
def message():
    """
    text message endpoint
    """

    return "Let's send a text"

@APP.route('/secret')
def secret():
    """
    secrets endpoint
    """

    return "Tell me a secret"


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
