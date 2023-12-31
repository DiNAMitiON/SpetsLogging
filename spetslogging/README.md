SpetsLoging
=====

SpetsLogging is a simple way to log in the console and in a file.


Installing
----------

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):
```text
$ pip install spetsloging
```


A Simple Example
----------------


main.py
```python
import spetslogging
import time
log = spetslogging.logger.Log()
log.settings(
    Format='%d%.%m%.%y% %h%:%m%:%s% %stat% >> %message%',
    Colors={
        'INFO': 'CYAN',
        'DEBUG': 'YELLOW',
        'WARNING': 'LIGHTRED'
    }
)
for i in range(5):
    log.info(i, file='test.log')
    log.error('Test', file='test.log')
    time.sleep(0.5)

log.debug('Program completed')
```

Output
```text
31.10.2023 12:10:41 [INFO] >> 0
31.10.2023 12:10:41 [ERROR] >> Test
31.10.2023 12:10:42 [INFO] >> 1
31.10.2023 12:10:42 [ERROR] >> Test
31.10.2023 12:10:42 [INFO] >> 2
31.10.2023 12:10:42 [ERROR] >> Test
31.10.2023 12:10:43 [INFO] >> 3
31.10.2023 12:10:43 [ERROR] >> Test
31.10.2023 12:10:43 [INFO] >> 4
31.10.2023 12:10:43 [ERROR] >> Test
31.10.2023 12:10:44 [DEBUG] >> Program completed
```


test.log
```log
31.10.2023 12:10:41 [INFO] >> 0
31.10.2023 12:10:41 [ERROR] >> Test
31.10.2023 12:10:42 [INFO] >> 1
31.10.2023 12:10:42 [ERROR] >> Test
31.10.2023 12:10:42 [INFO] >> 2
31.10.2023 12:10:42 [ERROR] >> Test
31.10.2023 12:10:43 [INFO] >> 3
31.10.2023 12:10:43 [ERROR] >> Test
31.10.2023 12:10:43 [INFO] >> 4
31.10.2023 12:10:43 [ERROR] >> Test
```


Donate
------

To support the development of the library, support its author.
https://donationalerts.com/r/dinamition


Links
-----

-   PyPI Releases: https://pypi.org/project/SpetsLoging/
-   Source Code: https://github.com/DiNAMitiON/SpetsLoging/
-   Issue Tracker: https://github.com/DiNAMitiON/SpetsLogging/issues/
-   SpetsDevelopers | Support: https://discord.gg/z5hEVQ5agn/
