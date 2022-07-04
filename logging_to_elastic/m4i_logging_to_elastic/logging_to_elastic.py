from elasticsearch import Elasticsearch
from flask import Flask, request
from m4i_atlas_core import ConfigStore
from m4i_backend_core.auth import requires_auth

app = Flask(__name__)

store = ConfigStore.get_instance()


def write_to_elastic(index_name: str, message: dict):
    username, password, url_with_port, elastic_ca_certs_path = store.get_many('elastic_username', 'elastic_password',
                                                                         'elastic_host', 'elastic_ca_certs_path')
    connection = Elasticsearch(
        url_with_port,
        basic_auth=(username, password),
        ca_certs=elastic_ca_certs_path
    )
    response = connection.index(index=index_name, document=message)
    return response


@app.route('/log', methods=['POST'])
@requires_auth(transparent=True)
def logging_to_elastic(access_token=None):
    """
    This is the endpoint /log which is used to push logs to elastic index "atlas-logging".
    For the frontend the path will be /repository/api/log.

    :param message: The message or log to be pushed
    :param access_token: the bearer token of the frontend used to verify where this request is coming from.
    :return: The elastic api response.
    """
    index_name: str = 'atlas-logging'
    message = request.get_json(force=True)
    write_to_elastic(index_name, message)

# END logging_to_elastic
