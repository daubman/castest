# -*- coding: utf-8 -*-
import logging
from cassandra import policies
from cassandra.cluster import Cluster

import test_log  # Make sure we aren't somehow getting all debug logging by mistake

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(message)s', filemode='w', filename='repro_error.log', level=logging.DEBUG)

    hosts = ['127.0.0.1']
    unused_cluster = Cluster(contact_points=hosts,
                             load_balancing_policy=policies.WhiteListRoundRobinPolicy(hosts))

    test_log.dummy()

    logger.info('I want to see this...')
    logger.info('I hope interpreter magic does not end up truncating this...')


if __name__ == '__main__':
    main()