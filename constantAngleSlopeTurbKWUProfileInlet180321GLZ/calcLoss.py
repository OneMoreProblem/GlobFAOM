import subprocess as sp
import pandas as pd
import numpy as np
from scipy.optimize import minimize
import math
from functools import partial

def readHV(fileName):
	try:
		df = pd.read_csv(fileName, sep='\t', header=None)
		HV = df.to_numpy()
		HV[:, 0] = HV[:, 0] * 0.001
		HV = normalizeHV(HV)
	except:
		H = np.arange(0, 10, 0.1, dtype=float)
		V = np.full(100, 100)
		HV = np.column_stack((H, V))
	return HV

def readHVPostProc(fileName):
	try:
		df = pd.read_csv(fileName, sep='\t', header=None)
		HV = df.iloc[:, [0,1]].to_numpy()
		HV[0,1] = 0.0
		HV = normalizeHV(HV)
	except:
		H = np.arange(0, 10, 0.1, dtype=float)
		V = np.zeros(100)
		HV = np.column_stack((H, V))
	return HV

def normalizeHV(HV):
	Hstart = HV[0,0]
	Hfinish = HV[-1,0]
	Hstep = 0.00001
	H = np.arange(Hstart, Hfinish + Hstep, Hstep, dtype=float)
	V = np.interp(H, HV[:,0], HV[:,1], left=0, right=0)
	HV = np.column_stack((H, V))
	return HV

def calcOneRMSE(HVRef, HVTmp):
	size = min(waterVelocityExtract(HVRef[:,1]), waterVelocityExtract(HVTmp[:,1]))
	URef = HVRef[:size, 1]
	UTmp = HVTmp[:size, 1]
	RMSE = (URef - UTmp)**2
	RMSE =  math.sqrt(RMSE.sum() / size)
	return RMSE

def waterVelocityExtract(U):
	nMax = np.amax(np.argmax(U))
	if nMax != U.size - 1:
		nMax += 1
	return nMax

def main():
	bounds = [[0., 2.], [0., 2.], [0., 2.], [0., 2.], [0., 0.5], [0., 0.5], [0., 0.5], [0., 2.], [0., 2.], [0., 2.], [0., 2.], [0., 20.]]
	coeffs = [0.85, 1.0, 0.5, 0.856, 0.075, 0.0828, 0.09, 0.5555556, 0.44, 0.31, 1.0, 10.0]
	refFile = ("data/outletExperimentalProfile.csv")
	turbFile = ("postProcessing/singleGraph/0.5/line_U.xy")
	dfHVRef = readHV(refFile)
	dfHVPostProc = readHVPostProc(turbFile)
	RMSE = calcOneRMSE(dfHVRef, dfHVPostProc)
	open("data/loss", "w").write(str(RMSE))

if __name__ == "__main__":
	main()
