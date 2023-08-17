import logging
import sys

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stream_handler)

print(logging.NOTSET)
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)
