import os
from time import time

from mills.func.tools import time_formatter


from . import client, start_time
from mills.utils.logger import log
from mills.classes.importer import Importer
from mills.func.startup import startup



log.info("Initialising...")

client.run(startup())


suc_msg = """
            ----------------------------------------------------------------------
                Ikka CC Checker Bot has been deployed! Visit @TakashiKovace for updates!!
            ----------------------------------------------------------------------
"""


Importer('mills/plugins', True)


if '__main__' == __name__:
    log.info("Took {} seconds to deploy Ikka CC Checker Bot".format(time_formatter((time() - start_time) * 1000)))
    log.info(suc_msg)
    client.rud()