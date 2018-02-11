from multiprocessing import Process
import threading
import time
import os
import glob

from pyke import kepdraw, kepstitch, kepflatten, kepfold, keptrial, kepperiodogram, keprange, kepbls
from pyke import KeplerLightCurveFile, KeplerQualityFlags

stitch_path = 'D:\\pdaskas\\udacity\\machine-learning\\projects\\capstone\\output_stitch_test'    
flatten_destination = 'D:\pdaskas\\udacity\\machine-learning\\projects\\capstone\\output_stitch_flatten_test\\'
os.chdir(stitch_path)
	
def f(file):
	file_name = file.split('.')[0]
	kepflatten(file, outfile=flatten_destination + file_name + '-kepflatten.fits', overwrite=True)
	
if __name__ == '__main__':
	for file in glob.glob("*.fits"):
		p = Process(target=f, args=(file,))
		p.start()
		p.join()