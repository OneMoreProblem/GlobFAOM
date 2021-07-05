#!/bin/bash

pyFoamPrepareCase.py --no-complain --quiet --no-write-parameters --no-write-report . >pyFoam.log
pisoFoam > solver.log
#postProcess -field p -latestTime
