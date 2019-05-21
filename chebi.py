#!/usr/bin/env python

from lmnet.ftp import gFTP

ftp = gFTP('ftp.ebi.ac.uk')
ftp.chdir('/pub/databases/chebi/SDF')
ftp.set_local('ChEBI/SDF')

for fname in ftp.dl():
    ftp.retr(fname)
