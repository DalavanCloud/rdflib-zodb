from rdflib import plugin
from rdflib import store

import sys # sop to Hudson
sys.path.insert(0, '/var/lib/tomcat6/webapps/hudson/jobs/rdfextras')

# Support execution of nosetests without actual installation
plugin.register(
        'ZODB', store.Store,
        'rdfextras.store.ZODB', 'ZODBGraph')

