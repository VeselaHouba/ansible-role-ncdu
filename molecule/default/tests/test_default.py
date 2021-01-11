import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ncdu(host):
    cmd = host.run("ionice -c idle ncdu -o /opt/ncdu.json /")
    outfile = host.file("/opt/ncdu.json")
    assert cmd.rc == 0
    assert outfile.exists
    assert outfile.size > 1000
