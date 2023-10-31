import spetslogging
import time
log = spetslogging.logger.Log()
log.settings(
    Format='%d%.%m%.%y% %h%:%m%:%s% %stat% >> %message%',
    Colors={
        'INFO': 'CYAN',
        'DEBUG': 'YELLOW'
    }
)
for i in range(5):
    log.info(i, file='test.log')
    log.error('Test', file='test.log')
    time.sleep(0.5)

log.debug('Program complite')
