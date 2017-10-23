Example Repo for Setuptools issue
=================================

These two repos have intentional version conflict to make issue stand out more.
`pip` silently ignores the conflic according to its standard rules (top level wins).

STR
---
.. code-block:: sh

    mkvirtualenv test
    git clone git@github.com:vartec/example_repo_setuptools_issue.git
    cd example_repo_setuptools_issue
    pip install -e .[testing] --process-dependency-links
    python setup.py test


ER
--
``python setup.py test`` not attempting to install anything, just running the tests

AR
--
``python setup.py test`` attempts to reinstall submodule dependencies, resulting in `VersionConflict`


What I'd like to achieve
------------------------

A way of preventing `python setup.py test` from attempting to install anything, given that everything is already installed in previous step using `pip`