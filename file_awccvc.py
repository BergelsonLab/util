import pandas as pd
from shutil import copy
import os

aclew = pd.read_csv("data/aclew_data.csv")


df = aclew.query("Corpus == \"Bergelson\"")

itsdir = "../../seedlings/collect/all_its"

outdir = "data/its"

for i, x in df.iterrows():
    prefix = x.ID[2:]
    if x.AgeMonths < 10:
        prefix += "_0" + str(x.AgeMonths)
    else:
        prefix += "_" + str(x.AgeMonths)
    fname = "{}.its".format(prefix)
    copy(os.path.join(itsdir, fname), os.path.join(outdir, fname))
print
