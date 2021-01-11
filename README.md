# Ansible veselahouba.ncdu role

[![Build Status](https://drone.m-cloud.cz/api/badges/VeselaHouba/ansible-role-ncdu/status.svg)](https://drone.m-cloud.cz/VeselaHouba/ansible-role-ncdu)

`veselahouba.ncdu` is an [Ansible](http://www.ansible.com) role which:
* installs ncdu
* Sets cron to create ncdu output file, so you can load it anytime.

## Installation

Using `ansible-galaxy`:

```shell
$ ansible-galaxy install veselahouba.ncdu
```

Using `requirements.yml`:

```yaml
- name: veselahouba.ncdu
```

Using `git`:

```shell
$ git clone https://github.com/veselahouba/ansible-role-ncdu.git veselahouba.ncdu
```

## Dependencies

* Ansible >= 2.8

## Variables

Please consult `defaults/main.yml`.
