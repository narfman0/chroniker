chroniker
==============

.. image:: https://badge.fury.io/py/chroniker.png
    :target: https://badge.fury.io/py/chroniker

.. image:: https://travis-ci.org/narfman0/chroniker.png?branch=master
    :target: https://travis-ci.org/narfman0/chroniker

Verify speedruns using ML and ~the cloud~

Installation
------------

Install via pip::

    pip install sr-chroniker

Development
-----------

Ensure pipenv is installed for development.

Run test runners to ensure everything works::

    make test

Architecture
------------

* Front end serverless web app adds SQS message with info to DL video
* Front end inspecter includes time slider can show significant events with annotations
* Worker AMI consumes the queue to completion
* Lambda (?) monitors queue and spawns AMIs as needed (?)
* Results in dynamo with key images and metrics

TODO
----

MVP:

* Create locally running inspector to identify end/start time (opencv?)
* Save output in dynamodb
* Create front end to view results and add new runs

Stretch:

* Analyze audio for breaks (to identify splices)
* Count frames by diffing each frame
* Compare known times for flags

License
-------

Copyright (c) 2019 Jon Robison

See LICENSE for details
