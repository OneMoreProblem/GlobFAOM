#!/bin/bash
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions
./clearStep.sh
pyFoamPrepareCase.py --no-clear --stop-after-templates --no-complain --quiet --no-write-parameters --no-write-report . 2>&1 > log.pyFoam

runParallel $(getApplication)
runParallel postProcess -parallel -latestTime -func singleGraph
python3 calcLoss.py
