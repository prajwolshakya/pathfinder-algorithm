import argparse
from bfs import *
from  Algorithm_A import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main.py')
    parser.add_argument('--a', help='insertion sort algorithm',dest='a',action="store_true")
    parser.add_argument('--bfs', help='Bubble sort algorithm', dest='bfs',action="store_true")
    parser.add_argument(
        '--start', help='start point', type=int, nargs="+", dest='start')
    parser.add_argument(
    '--end', help='start point', type=int, nargs="+" ,dest='end')
    args = parser.parse_args()
    print(args)
    if args.a:
        a(args.start,args.end)
    if args.bfs:
        bfs(args.start,args.end)
    
