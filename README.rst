eb-prune
########

.. image:: https://travis-ci.org/adarnimrod/eb-prune.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/eb-prune

A CLI tool to prune old versions of Elastic Beanstalk.

Installation
------------

.. code:: shell

    pip install eb-prune

Usage
-----

To keep the last 100 versions available, simply run :code:`eb-prune 100`. The
tool relies on the usual AWS CLI configuration as described `here
<http://docs.aws.amazon.com/cli/latest/topic/config-vars.html>`_, specifically
on access key id, secret access key and region.

.. code:: shell

    $ eb-prune --help
    usage: eb-prune [-h] [-d] versions_to_keep

    positional arguments:
      versions_to_keep  The number of versions to keep.

      optional arguments:
        -h, --help        show this help message and exit
        -d, --dry-run     Dry run, do not delete versions.

License
-------

This software is licnesed under the MIT licese (see the :code:`LICENSE.txt`
file).

Testing
-------

Tests require Python 2.7, Python 3.2 or later and Tox and are run by running
:code:`tox`. Also, Travis CI is used to test on multiple Python versions for
every push.

Release
-------

Releases require Python 2.7 or Python 3.2 or later and Tox. To release a new
version bump the version in the :code:`VERSION` file and run :code:`tox -e
release`.

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.

TODO
----

- Fix Travis CI run on Python 3.2
  (https://travis-ci.org/adarnimrod/eb-prune/jobs/187705346).
- Release to PyPI on tagged commits from Travis CI.
- Add tests using moto.
