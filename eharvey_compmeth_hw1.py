import argparse as arg
import numpy as np

Parser = arg.ArgumentParser()
Parser.add_argument('-i','--input',type=str,help='Input file')
args = Parser.parse_args()
Parser.add_argument('-o','--output',type=str,help='Output file')


def ball_drop(h,g):
    time = np.sqrt(2*h/g)
    print("The time it takes for the ball to land from", h ,"meters is", time,
    "seconds")
    return

ball_drop(300, 9.8)
