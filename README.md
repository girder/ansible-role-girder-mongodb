girder.mongodb
==============
[![Apache 2.0](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/girder/ansible-role-girder-mongodb/master/LICENSE)

An Ansible role to install [MongoDB server](https://www.mongodb.com/download-center/community).

Requirements
------------

Ubuntu 16.04+.

Role Variables
--------------

| parameter         | required | default | comments                                                         |
| ------------------| -------- | ------- | -----------------------------------------------------------------|
| mongodb_version   | no       | 4.0              | The major.minor version of MongoDB to install.          |
| mongodb_data_path | no       | /var/lib/mongodb | The filesystem path where data files will be persisted. |
