#!/bin/bash
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions
pyFoamPrepareCase.py --no-complain --quiet --no-write-parameters --no-write-report . >pyFoam.log

runApplication setFields
runApplication decomposePar -constant
runParallel $(getApplication) >log.solver
runParallel postProcess -parallel -func singleGraph
python3 calcLoss.py

#pisoFoam > solver.log
#postProcess -field p -latestTime
