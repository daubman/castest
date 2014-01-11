# -*- coding: utf-8 -*-
import logging

log = logging.getLogger(__name__)


def main():
    log.debug('I should not see this anywhere as there is no logging output configured for this module')


def dummy():
    pass


main()  # Call this on import and show that not all log.debug end up in the basicConfig log

