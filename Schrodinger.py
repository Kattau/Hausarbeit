"""importing all necessary packages and modules"""
from solvers import schrodinger
from visualizer import visualizer
from argparse import ArgumentParser
import os

parser = ArgumentParser(description='Change working directory')
parser.add_argument("-d", "--directory", dest="directory", default= os.path.dirname(__file__), type=ascii)
path = parser.parse_args()
file_path = str(path.directory)[1:-1] + "schrodinger.inp"
print(file_path)
schrodinger(file_path)
visualizer(file_path)
