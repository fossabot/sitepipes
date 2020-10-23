from flask import Blueprint, request

from sitepipes import

workflows = Blueprint('workflows', __name__)


@workflows.route('/api/run_')
def run_():
