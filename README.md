girder.mongodb
==============
[![Apache 2.0](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/girder/ansible-role-girder-mongodb/master/LICENSE)
[![Tests](https://circleci.com/gh/girder/ansible-role-girder-mongodb.svg?style=svg)](https://circleci.com/gh/girder/ansible-role-girder-mongodb)

An Ansible role to install [MongoDB server](https://www.mongodb.com/download-center/community).

Requirements
------------

Ubuntu 16.04+.

Role Variables
--------------

| parameter           | required | default          | comments                                                                |
| --------------------| -------- | ---------------- | ----------------------------------------------------------------------- |
| mongodb_version     | no       | 4.0              | The major.minor version of MongoDB to install.                          |
| mongodb_data_path   | no       | /var/lib/mongodb | The filesystem path where data files will be persisted.                 |
| mongodb_bind_public | no       | false            | Whether to bind to all network interfaces. **This is a security risk.** |
