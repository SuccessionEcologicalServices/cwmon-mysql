========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/cwmon-mysql/badge/?style=flat
    :target: https://readthedocs.org/projects/cwmon-mysql
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/RescueTime/cwmon-mysql.svg?branch=develop
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/RescueTime/cwmon-mysql

.. |requires| image:: https://requires.io/github/RescueTime/cwmon-mysql/requirements.svg?branch=develop
    :alt: Requirements Status
    :target: https://requires.io/github/RescueTime/cwmon-mysql/requirements/?branch=develop

.. |coveralls| image:: https://coveralls.io/repos/github/RescueTime/cwmon-mysql/badge.svg?branch=develop
    :target: https://coveralls.io/github/RescueTime/cwmon-mysql?branch=develop
    :alt: Coverage Status

.. |version| image:: https://img.shields.io/pypi/v/cwmon-mysql.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/cwmon-mysql

.. |downloads| image:: https://img.shields.io/pypi/dm/cwmon-mysql.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/cwmon-mysql

.. |wheel| image:: https://img.shields.io/pypi/wheel/cwmon-mysql.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/cwmon-mysql

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cwmon-mysql.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/cwmon-mysql

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cwmon-mysql.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/cwmon-mysql


.. end-badges

A cwmon_ plugin for monitoring MySQL.

.. _cwmon: https://github.com/RescueTime/cwmon

* Free software: BSD license

Installation
============

::

    pip install cwmon-mysql

Documentation
=============

https://cwmon-mysql.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
