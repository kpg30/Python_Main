import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

this_set = {"apple", "banana", "cherry"}

for x in this_set:
    logger.info(x)
