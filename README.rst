MongoCapsule
============

|Build Status|

|Code Climate|

|Test Coverage|

|PyPI|

|PyPI|

Overview
--------

MongoCapsule is a very thin wrapper around MongoEngine built for your
happiness. It encapsulates MongoEngine attributes under a single
namespace and hence allows explicit declaration without context
switches.

In addition to that, MongoCapsule adds pagination support to all the
query results.

MongoEngine is a great ORM for using MongoDB in any Python project.
However, since MongoEngine works in “contexts”, using multiple databases
requires trickery such as ``db_alias`` and ``switch_db``. MongoCapsule
solves this by attaching references to MongoEngine attributes to itself.

Quickstart
----------

If you are familiar with MongoEngine, you can use MongoCapsule already!
Create the database object and use it to define your document and
fields.

.. code:: python

    from mongocapsule import MongoCapsule

    db = MongoCapsule('test_db')

    class Fruits(db.Document):
        name = db.StringField()

Refer to `MongoEngine Docs`_ for details.

Installation
------------

To install use pip:

.. code:: bash

        pip install mongocapsule

Or clone the repo:

.. code:: bash

        git clone https://github.com/prashnts/mongocapsule.git
        python setup.py install

Additional API
--------------

MongoCapsule adds Pagination support to the MongoEngine ``QuerySet``
object. It returns 10 objects per page, however, this can be changed.

.. code:: python


    # Obtain nth Page of any arbitrary query:

    query_results = Document.objects(...).sort(...)

    result_page = query_results.page(2)     # Obtain second page

    total_pages = query_results.page_count

    # Update number of items returned per page:

    db.QuerySet.set_page_limit(20)

Contributing
------------

Code Patches, suggestions and bug reports welcome! Please use GitHub
issues for the same.

Rant
----

I wrote this module because the examples in official MongoEngine
documentation encourages using ``from mongoengine import *`` which not
only pollutes the local namespace, but makes class definitions implicit.
Of course, cherrypicked imports are possible, however that requires a
lot of extra imports in each files.

The biggest problem, however, comes when you’re using multiple databases
or hosts – in those cases, you need to use context switches or ugly
``meta`` attributes in the declaration.

.. _MongoEngine Docs: http://docs.mongoengine.org/index.html

.. |Build Status| image:: https://img.shields.io/travis/prashnts/mongocapsule/master.svg
   :target: https://travis-ci.org/prashnts/mongocapsule
.. |Code Climate| image:: https://img.shields.io/codeclimate/github/prashnts/mongocapsule.svg
   :target: https://codeclimate.com/github/prashnts/mongocapsule
.. |Test Coverage| image:: https://img.shields.io/codeclimate/coverage/github/prashnts/mongocapsule.svg
   :target: https://codeclimate.com/github/prashnts/mongocapsule
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/mongocapsule.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/mongocapsule
.. |PyPI| image:: https://img.shields.io/pypi/v/mongocapsule.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/mongocapsule