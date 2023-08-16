import logging
import sys

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stream_handler)
