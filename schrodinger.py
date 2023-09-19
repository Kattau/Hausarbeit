"""importing all necessary packages and modules"""
from argparse import ArgumentParser
import os
from solvers import schrodinger
from visualizer import visualizer


parser = ArgumentParser(description='Change working directory')
parser.add_argument("-d", "--directory", dest="directory", type=ascii)
path = parser.parse_args()
FILE_PATH = str(path.directory)[1:-1] + "/schrodinger.inp"
if str(path.directory) == "None":
    FILE_PATH = os.getcwd() + "/schrodinger.inp"
schrodinger(FILE_PATH)
visualizer(FILE_PATH)
