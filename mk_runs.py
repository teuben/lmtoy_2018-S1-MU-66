#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-66"
#
#

import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2018-S1-MU-66"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['IRAS05274+3345'] = [ 86030, 86034, 86038, 88510, 88512, 88659, 90024]

on['IRAS05358+3543'] = [ 86042, 86046, 86050, 88663, 88667, 88671]

on['IRAS18151-1208'] = [ 90958, 91045, 91574]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['IRAS05274+3345'] = "dv=80 dw=120 extent=200 vlsr=180 b_order=1" 
pars1['IRAS05358+3543'] = "dv=80 dw=120 extent=200 vlsr=160 b_order=1" 
pars1['IRAS18151-1208'] = "dv=80 dw=120 extent=200 vlsr=0   b_order=1"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['IRAS05274+3345'] = "pix_list=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"
pars2['IRAS05358+3543'] = "pix_list=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"
pars2['IRAS18151-1208'] = "pix_list=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"

runs.mk_runs(project, on, pars1, pars2)

