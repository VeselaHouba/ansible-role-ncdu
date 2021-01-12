import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ncdu(host):
    cmd = host.run("ionice -c idle ncdu -q -o /opt/ncdu.json /")
    outfile = host.file("/opt/ncdu.json")
    assert cmd.rc == 0
    assert outfile.exists
    assert outfile.size > 1000


def test_ncdu_cron(host):
    cronfile = host.file("/etc/cron.d/ncdu")
    assert cronfile.exists
    assert cronfile.contains('ionice -c idle ncdu')
