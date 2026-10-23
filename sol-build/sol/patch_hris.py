import sys
sys.path.insert(0,'sol'); from common import *
s=open('mk/hris.html').read()
s=swap_ledger(s)
s=hris_block(s)
s=scrub(s)
open('sol/hris.html','w').write(s)
