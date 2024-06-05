import sys

from clint.textui import prompt


class PromptClient(object):
    def __init__(self, validators=None):

        self.validators = validators or []

        return

    def _options(self, question):
        ''' prompt query provides with options '''

        confirm_options = [
            {'selector': '1', 'prompt': 'Yes', 'return': 'Y'},
            {'selector': '2', 'prompt': 'No', 'return': 'N'}
        ]

        _prompt = prompt.options('{}'.format(question), confirm_options)

        if _prompt == 'Y':
            return 'Y'
        elif _prompt == 'N':
            return 'N'
        else:
            sys.stderr()

    def _query(self, question, validators=None):
        ''' prompt options allows for free text '''

        self.validators = validators

        _prompt = prompt.query('{}'.format(question), validators=validators)

        return _prompt
