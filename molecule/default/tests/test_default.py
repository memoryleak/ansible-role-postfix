import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postfix_is_installed(host):
    postfix = host.package("postfix")
    assert postfix.is_installed


def test_postfix_is_running(host):
    postfix = host.service("postfix")
    assert postfix.is_running


def test_sasl_passwd_contains(host):
    postfix = host.file("/etc/postfix/sasl_passwd")
    assert postfix.contains("secret")


def test_virtual_contains(host):
    postfix = host.file("/etc/postfix/virtual")
    assert postfix.contains("hello@example.com")


def test_sasl_passwd_exists(host):
    postfix = host.file("/etc/postfix/sasl_passwd.db")
    assert postfix.exists


def test_virtual_exists(host):
    postfix = host.file("/etc/postfix/virtual.db")
    assert postfix.exists
