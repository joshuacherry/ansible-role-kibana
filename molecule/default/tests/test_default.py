"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kibana_is_installed(host):
    """
    Tests that kibana is installed
    """
    kibana_package = "kibana"

    kibana = host.package(kibana_package)
    assert kibana.is_installed


def test_kibana_running_and_enabled(host):
    """
    Tests that kibana is running and enabled
    """
    kibana = host.service("kibana")
    assert kibana.is_running
    assert kibana.is_enabled
