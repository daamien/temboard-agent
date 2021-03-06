################
 temBoard Agent
################

| |Python| |CircleCI| |PyPI|

temBoard_ is a powerful management tool for PostgreSQL.

temBoard agent is a Python2 service designed to run along PostgreSQL, exposing a
REST API to implement various management tasks on PostgreSQL instance. See
http://temboard.io/ for the big picture.


==========
 Features
==========

- Non intrusive daemon dedicated to one PostgreSQL cluster.
- No extra dependencies.
- Written python2.7, supported by stable distribution releases.
- Secured REST API with SSL and credentials.
- Extensible with plugins.


==============
 Installation
==============

.. code-block::

   pip install temboard-agent
   sudo -u postgres temboard-agent -c /usr/local/share/temboard-agent/quickstart/temboard-agent.conf

See `temBoard full documentation`_ for details on configuration.


.. |CircleCI| image:: https://circleci.com/gh/dalibo/temboard-agent.svg?style=shield
   :target: https://circleci.com/gh/dalibo/temboard-agent
   :alt: CircleCI

.. |PyPI| image:: https://img.shields.io/pypi/v/temboard-agent.svg
   :target: https://pypi.python.org/pypi/temboard-agent
   :alt: Version on PyPI

.. |Python| image:: https://img.shields.io/pypi/pyversions/temboard-agent.svg
   :target: https://www.python.org/
   :alt: Versions of python supported

.. _`temBoard`: http://temboard.io/
.. _`temBoard full documentation`: http://temboard.readthedocs.io/
