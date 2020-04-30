import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "openjdk-8-jdk-headless"
    ])
def test_for_openjdk8_package_installed(host, name):
    pkg = host.package(name)

    assert pkg.is_installed
