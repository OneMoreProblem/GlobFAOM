#!/bin/bash
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions
pyFoamPrepareCase.py --no-complain --quiet --no-write-parameters --no-write-report . >log.pyFoam

runApplication setFields
runApplication decomposePar -constant
runParallel $(getApplication)
runParallel postProcess -parallel -func singleGraph
python3 calcLoss.py

#pisoFoam > solver.log
#postProcess -field p -latestTime
