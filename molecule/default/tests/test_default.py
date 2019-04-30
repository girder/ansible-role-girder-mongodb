import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mongodb_install(host):
    mongodb_package = host.package('mongodb-org-server')
    assert mongodb_package.is_installed
    assert mongodb_package.version.startswith('4.0')


def test_mongodb_user(host):
    mongodb_user = host.user('mongodb')
    assert mongodb_user.exists


def test_mongodb_group(host):
    mongodb_group = host.user('mongodb')
    assert mongodb_group.exists


def test_mongodb_data_dir(host):
    mongodb_dir = host.file('/var/lib/mongodb')
    assert mongodb_dir.is_directory
    assert mongodb_dir.user == 'mongodb'
    assert mongodb_dir.group == 'mongodb'


def test_mongodb_data_file(host):
    mongodb_file = host.file(os.path.join('/var/lib/mongodb', 'mongod.lock'))
    assert mongodb_file.is_file
    assert mongodb_file.user == 'mongodb'
    assert mongodb_file.group == 'mongodb'


def test_mongodb_service(host):
    mongodb_service = host.service('mongod')
    assert mongodb_service.is_running
    assert mongodb_service.is_enabled


def test_mongodb_socket_private(host):
    mongodb_socket = host.socket("tcp://127.0.0.1:27017")
    assert mongodb_socket.is_listening


def test_mongodb_socket_public(host):
    mongodb_socket = host.socket("tcp://0.0.0.0:27017")
    assert not mongodb_socket.is_listening
