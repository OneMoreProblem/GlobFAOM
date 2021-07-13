#!/bin/sh
rm -rf processor0/0.* processor0/[1-9]*
rm -rf processor1/0.* processor1/[1-9]*
rm -rf processor2/0.* processor2/[1-9]*
rm -rf processor3/0.* processor3/[1-9]*
rm -rf processor4/0.* processor4/[1-9]*
rm -rf processor5/0.* processor5/[1-9]*
rm -rf processor6/0.* processor6/[1-9]*
rm -rf processor7/0.* processor7/[1-9]*
rm -rf postProcessing
rm data/loss
rm log.interFoam
rm log.postProcess
rm log.calcLoss
rm log.pyFoam
rm PyFoam*
rm constant/turbulenceProperties

#------------------------------------------------------------------------------
