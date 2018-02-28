Try pandoc!
pandoc --from markdown --to rst
   from    

# RobotFramework Advanced Logging Library

[![Build Status](https://travis-ci.org/peterservice-rnd/robotframework-advancedlogging.svg?branch=master)](https://travis-ci.org/peterservice-rnd/robotframework-advancedlogging)

Short Description
---

Creating additional logs when testing in [Robot Framework](http://www.robotframework.org).

Installation
---

```
pip install robotframework-advancedlogging
```

Documentation
---

See keyword documentation for robotframework-advancedlogging library in folder `docs`.

# Example
| Settings | Value | Value  | Value  |
|----|----|---|----|
| Library     |  AdvancedLogging   | C:/Temp  |   LogFromServer |
| Library     |  SSHLibrary        |          |                 |


| Test cases       | Action                    | Argument        | Argument               |
|------------------|---------------------------|-----------------|------------------------|
| Example_TestCase | ${out}=                   | Execute Command |  grep error output.log |
|                  | Write advanced testlog    | error.log       | ${out}                 |


``` 
File C:/Temp/LogFromServer/TestSuite name/Example_TestCase/error.log  with content from variable ${out}
```

License
---

Apache License 2.0




to    
RobotFramework Advanced Logging Library
=======================================

|Build Status|

Short Description
-----------------

Creating additional logs when testing in `Robot Framework`_.

Installation
------------

::

    pip install robotframework-advancedlogging

Documentation
-------------

See keyword documentation for robotframework-advancedlogging library in
folder ``docs``.

Example
=======

+----------+-----------------+---------+---------------+
| Settings | Value           | Value   | Value         |
+==========+=================+=========+===============+
| Library  | AdvancedLogging | C:/Temp | LogFromServer |
+----------+-----------------+---------+---------------+
| Library  | SSHLibrary      |         |               |
+----------+-----------------+---------+---------------+

+-----------------+-----------------+-----------------+-----------------+
| Test cases      | Action          | Argument        | Argument        |
+=================+=================+=================+=================+
| Example_TestCas | ${out}=         | Execute Command | grep error      |
| e               |                 |                 | output.log      |
+-----------------+-----------------+-----------------+-----------------+
|                 | Write advanced  | error.log       | ${out}          |
|                 | testlog         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

::

    File C:/Temp/LogFromServer/TestSuite name/Example_TestCase/error.log  with content from variable ${out}

License
-------

Apache License 2.0

.. _Robot Framework: http://www.robotframework.org

.. |Build Status| image:: https://travis-ci.org/peterservice-rnd/robotframework-advancedlogging.svg?branch=master
   :target: https://travis-ci.org/peterservice-rnd/robotframework-advancedlogging
pandoc 2.1.1

© 2013–2015 John MacFarlane