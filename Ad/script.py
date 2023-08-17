import logging
import sys

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stream_handler)
file_handler = logging.FileHandler('output.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
# print(logging.NOTSET)
# print(logging.DEBUG)
# print(logging.INFO)
# print(logging.WARNING)
# print(logging.ERROR)
# print(logging.CRITICAL)

def division():
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return 
  if divisor == 0:
    logging.error("Attempting to divide by 0!")
    return None
  else:
    return dividend/divisor
result = division()

if result == None:
    logging.WARNING("The result value is None!")
