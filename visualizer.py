"""Analyze the import arguments and plot the results"""
from argparse import ArgumentParser
import os
from plotter import visualizer

parser = ArgumentParser(description='Change working directory')
parser.add_argument("-d", "--directory", dest="directory", type=ascii)
parser.add_argument("-s", "--scalar", dest="scalar", type=ascii)
path = parser.parse_args()
FILE_PATH = str(path.directory)[1:-1]
if str(path.directory) == "None":
    FILE_PATH = os.getcwd()
scalar = 1
if str(path.scalar) != "None":
    scalar = float(path.scalar[1:-1])
visualizer(FILE_PATH, scalar)
