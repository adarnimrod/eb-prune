eb-prune
########

.. image:: https://git.shore.co.il/nimrod/eb-prune/badges/master/pipeline.svg
    :target: https://git.shore.co.il/nimrod/eb-prune/-/commits/master
    :alt: pipeline status

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

Various linters are configured with `pre-commit <https://pre-commit.com/>`_.
Those are run in CI in `GitLab
<https://git.shore.co.il/nimrod/eb-prune/-/pipelines>`_. To run locally, install
pre-commit and run it.

Release
-------

Update the version in :code:`VERSION`, commit, tag and push. GitLab will do the
rest.

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/explore.
