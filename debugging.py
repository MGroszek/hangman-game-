
import logging

logging.basicConfig(filename="mylog.log", filemode="w", level=logging.DEBUG)

logging.debug("Debug ist the lowest log level in severity")
logging.info("Info ist the second lowest log level")
logging.warning("Warning ist the third")
logging.error("Error ist the fourth level")
logging.critical("Critical ist the fifth and highest level")
