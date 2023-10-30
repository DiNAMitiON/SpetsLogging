SpetsLoging
=====

Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

.. _WSGI: https://wsgi.readthedocs.io/
.. _Werkzeug: https://werkzeug.palletsprojects.com/
.. _Jinja: https://jinja.palletsprojects.com/


Installing
----------

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):
```text
$ pip install spetsloging
```


A Simple Example
----------------


```python
import spetsloging

spetsloging.settings(
    format='%d.%m.%y %h:%m %stat >> %message',
    color={
        info='blue',
        debug='orange',
        warning='red'
    }
)

for i in range(5):
    spetsloging.info(i)
```

```text
30.10.2023 22:13 [info] >> 0
30.10.2023 22:13 [info] >> 1
30.10.2023 22:13 [info] >> 2
30.10.2023 22:13 [info] >> 3
30.10.2023 22:13 [info] >> 4
30.10.2023 22:13 [info] >> 5
```

Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to Flask, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/pallets/flask/blob/main/CONTRIBUTING.rst


Donate
------

To support the development of the library, support its author.
https://donationalerts.com/r/dinamition


Links
-----

-   Documentation: https://flask.palletsprojects.com/
-   Changes: https://flask.palletsprojects.com/changes/
-   PyPI Releases: https://pypi.org/project/SpetsLoging/
-   Source Code: https://github.com/DiNAMitiON/SpetsLoging/
-   Issue Tracker: https://github.com/pallets/flask/issues/
-   Chat: https://discord.gg/pallets
