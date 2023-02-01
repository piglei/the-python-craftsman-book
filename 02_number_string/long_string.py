# -*- coding: utf-8 -*-
# A simple logger as print
import textwrap
import logging
import logging.handlers

hdr = logging.StreamHandler()
hdr.setFormatter(logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(hdr)
logger.setLevel(logging.DEBUG)

def main():
    logger.info(("There is something really bad happened during the "
                 "process. Please contact your administrator."))

def main():
    # if user.is_active:
    if True:
        message = textwrap.dedent("""\
            Welcome, here is your movie list:
            - Jaw (1975)
            - The Shining (1980)
            - Saw (2004)""")
    print(message)



if __name__ == '__main__':
    main()
