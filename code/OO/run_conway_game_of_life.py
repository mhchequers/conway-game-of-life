import argparse
import sys, os
home_directory = '/home/matthew'
sys.path.append(home_directory+'/conway-game-of-life/code/OO/lib')
import conway_game_of_life as cgol

def main():
    # Sort out initialization parameter arguments
    parser = argparse.ArgumentParser(description="Runs OO implmentation of Conway's Game of Life")
    parser.add_argument('--grid-size', dest='grid_size', required=False)
    parser.add_argument('--interval-s', dest='interval', required=False)
    parser.add_argument('--num-steps', dest='steps', required=False)
    args = parser.parse_args()

    # set grid size
    grid_size = 10
    if args.grid_size:
        grid_size = args.grid_size
    
    # set interval between updates
    interval_s = 1.0
    if args.interval:
        interval_s = args.interval

    # set number of steps (updates)
    num_steps = 5
    if args.steps:
        num_steps = args.steps
    
    game = cgol.ConwayGameOfLife(grid_size, interval_s, num_steps)
    game.run()

# call main
if __name__ == '__main__':
    main()