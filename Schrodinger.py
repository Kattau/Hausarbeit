"""importing all necessary packages and modules"""
from solvers import schrodinger
from visualizer import visualizer

file_path = input('Enter a file path: ')
schrodinger(file_path)
visualizer(file_path)
