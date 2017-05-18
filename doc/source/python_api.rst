The :mod:`almanachclient` Python API
====================================

.. module:: almanachclient
:synopsis: A python client for the Almanach API.

Usage
-----

First, create an Almanach Client instance with your credentials::

    >>> from almanachclient.v1.client import Client
    >>> almanach = Client(URL, AUTH_TOKEN)

Here ``URL`` will be a string that represents the url of your API.
``AUTH_TOKEN`` will be the authorization token you use to acces the API.


Examples
--------
    >>> almanach = Client('http://api.region.example.org',  'myApiAuthorizationToken')
    >>> almanach.get_info()

    >>> almanach.get_volume_types()
    >>> almanach.get_volume_type('f1c2db7b-946e-47a4-b443-914a669a6673')
    >>> almanach.create_volume_type('f1c2db7b-946e-47a4-b443-914a669a5555', 'VolumeTypeName')
    >>> almanach.delete_volume_type('f1c2db7b-946e-47a4-b443-914a669a5555')

    >>> almanach.get_tenant_entities('my-tenant-uuid', '2017-01-17 00:00:00.00', '2017-05-17 00:00:00.00')

    >>> almanach.delete_instance('f1c2db7b-946e-47a4-b443-914a669a3333')
    >>> almannach.update_instance_entity(instance_id='f1c2db7b-946e-47a4-b443-914a669a2222', start='2017-02-17 00:00:00.00', end='2017-03-17 00:00:00.00')
