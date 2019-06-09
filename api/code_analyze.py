"""Code Analyzer API -code_analyze."""

import json

from flask import current_app
from flask.ext.restful import (
    fields,
    marshal,
    reqparse,
    Resource
)

from pylint import epylint as lint


error_details = {
    'line': fields.String,
    'message_id': fields.String(attribute='message-id'),
    'message': fields.String
}
format_details = {
    'errors': fields.Nested(error_details)
}


parser = reqparse.RequestParser()
parser.add_argument('source_code', required=True, type=unicode,
                    location=['json', 'form'],
                    help='Source code required to run formatting.')


class CodeAnalyze(Resource):
    """Handle requests related to source code formatting."""

    def post(self):
        """
        Save the posted data into a temporary file.

        Check the saved file for errors/formatting issues.
        Return a JSON response with errors if any.
        """
        source_code = parser.parse_args().get('source_code')
        temp_file = '{}/{}'.format(
            current_app.config.get("TEMP_FOLDER"),
            'source_code.py'
        )
        with open(temp_file, 'wb') as _temp:
            _temp.write(source_code)

        (pylint_stdout, pylint_stderr) = lint.py_run(
            temp_file + ' --output-format=json',
            return_std=True,
        )
        error_list = []
        if pylint_stdout.getvalue():
            error_list = json.loads(pylint_stdout.getvalue())
            error_list = sorted(error_list, key=lambda i: i['line'])

        return marshal(
            {'errors': error_list},
            format_details
        ), 200
