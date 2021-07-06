#!/bin/bash

pyFoamClearCase.py .
rm *log*
rm PyFoam*
#postProcess -field p -latestTime
