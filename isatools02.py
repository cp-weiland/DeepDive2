#! /usr/bin/env python

import os, sys, re, json
from pathlib import Path

from isatools.model import *
from isatools import isatab
from isatools.isajson import ISAJSONEncoder

from isabase import create_descriptor as creadc

_isapath = "./ipath"

#invest = Investigation()
#invest.studies.append(Study())

#invest.title = "ISA Investigation test01"
#invest.studies[0].title = "test01 study_alpha"
#invest.studies[0].assays.append(Assay())

invest = creadc()

Path(_isapath).mkdir(parents=True, exist_ok=True)
#isatab.dump(invest, _isabpath)

with open(os.path.join(_isapath, 'isa_model02.json'), 'w', encoding='utf-8') as f:
    json.dump(invest, f, cls=ISAJSONEncoder, sort_keys=True, ensure_ascii=False, indent=4)
