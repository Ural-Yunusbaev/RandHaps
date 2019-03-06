#!/usr/bin/python

from __future__ import division

import pandas as pd
import numpy as np
import random
import sys


assoc_SNPs_file=sys.argv[1] # associated SNPs from GRASP

Illumina_map_file=sys.argv[2] # Illumina 610k physical map range for each chromosome

IBDlength=int(sys.argv[3]) # length of IBD haplotype

rd=int(sys.argv[4]) # number of random haplotype pairs to be generated

# importing

d_Illumina_map = pd.read_csv(Illumina_map_file, sep=' ', delimiter=None)

d_assoc_SNPs = pd.read_csv(assoc_SNPs_file, sep='\t', delimiter=None)


# *** define functions:

# RANDOM HAPLOTYPE GENERATOR
# choose a random chromosome, then get its lower and upper intervals in b.p.
def random_hap(draws,dset):
  IBD_segs = []
  for k in range(0,draws):
    chroms = range(1,23)
    chr_i=random.choice(chroms)
    lower=dset.ix[dset.ix[:,'chr']==chr_i,'start']
    upper=dset.ix[dset.ix[:,'chr']==chr_i,'end']
    start = np.random.randint(lower, upper - IBDlength)
    end = start + IBDlength
    IBD_segs.append([chr_i,start,end])
  return IBD_segs

# COUNT N of assoc SNPs in the random HAPLOTYPEs and report indicator variable=1 when a defined event is encountered
# for example two haplotypes y and z have exactly one and two matches each, otherwise report indicator variable=0

def report_event_X(hap_y,hap_z,event_X,snp_set=d_assoc_SNPs):
  event_yes=None
  y_matches=None
  z_matches=None
  #global k
  #global t
  k=None
  t=None
  to_check_with_y=snp_set.ix[snp_set.ix[:,'CHR']==hap_y[0],'POS'].values.tolist()
  to_check_with_z=snp_set.ix[snp_set.ix[:,'CHR']==hap_z[0],'POS'].values.tolist()
  if len(to_check_with_y) == 0:
    y_matches=0
  else:
    y_matches=len([ int(1) for k in to_check_with_y if k >= hap_y[1] and k <= hap_y[2] ])
  if len(to_check_with_z) == 0:
    z_matches=0
  else:
    z_matches=len([ int(1) for t in to_check_with_z if k >= hap_z[1] and k <= hap_z[2] ])
  all_matches=[y_matches,z_matches]
  all_matches.sort()
  event_X.sort()
  if all_matches[0] >= event_X[0] and all_matches[1] >= event_X[1]:
    event_yes=1
  else:
    event_yes=0
  return event_yes

# *** define functions - end

print('Number of associated SNPs queried: ',len(d_assoc_SNPs.ix[:,'POS']))

# generate list of random haplotypes [(chrom,start,end),...]
list_of_rand_haps_A = random_hap(draws=rd,dset=d_Illumina_map)
list_of_rand_haps_B = random_hap(draws=rd,dset=d_Illumina_map)


Event_X_1_0=[ report_event_X(hap_y=y,hap_z=z,event_X=[2,7],snp_set=d_assoc_SNPs) for y,z in zip(list_of_rand_haps_A,list_of_rand_haps_B) ]

N_event_X=sum(x>0 for x in Event_X_1_0)
total_haps=len(Event_X_1_0)
prob_X=N_event_X / total_haps
print(prob_X)

