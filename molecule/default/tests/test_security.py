import os
import requests
from requests import ReadTimeout

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_webserver_connected_via_localhost(host):

    scks = host.socket("tcp://127.0.0.1:80")
    assert scks.is_listening

def test_not_webserver_connected_via_public_network(host):
    try:
        response = requests.get('http://localhost:8888', verify=False, timeout=10)
        # should be never reached
        assert not response.status_code == 200
    except ReadTimeout:
        pass
