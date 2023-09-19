"""importing all necessary packages and modules"""
from argparse import ArgumentParser
import os
from solvers import schrodinger
from visualizer import visualizer


parser = ArgumentParser(description='Change working directory')
parser.add_argument("-d", "--directory", dest="directory", default= os.path.dirname(__file__), type=ascii)
path = parser.parse_args()
FILE_PATH = str(path.directory)[1:-1] + "schrodinger.inp"
print(FILE_PATH)
schrodinger(FILE_PATH)
visualizer(FILE_PATH)
