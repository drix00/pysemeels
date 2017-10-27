.. highlight:: shell

============
Installation
============


Stable release
--------------

To install pySEM-EELS, run this command in your terminal:

.. code-block:: console

    $ pip install pysemeels

This is the preferred method to install pySEM-EELS, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for pySEM-EELS can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/drix00/pysemeels

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/drix00/pysemeels/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

Build the docs
--------------

To build the documentation:

.. code-block:: console

    $ cd docs
    $ make html

To generate or update the API documentation:

.. code-block:: console

    $ cd docs
    $ sphinx-apidoc -o api -T ../pysemeels
    $ make html

.. _Github repo: https://github.com/drix00/pysemeels
.. _tarball: https://github.com/drix00/pysemeels/tarball/master
