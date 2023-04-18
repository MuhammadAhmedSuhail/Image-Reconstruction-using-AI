# Image Reconstruction using A* Algorithm

## Project Description

In this project, I implemented the A* algorithm to solve the problem of image reconstruction. My task was to reconstruct a 512x512 image that had been divided into 16x16 boxes and shuffled. To accomplish this, I created a Python program that takes input as the shuffled image and uses the A* algorithm to determine the optimal sequence of moves to reconstruct the original image. I used the skimage library to display the shuffled and reconstructed images side by side.

## Approach

- I first divided the original image into 16x16 boxes and shuffled them randomly to create the shuffled image.
- I then represented each state of the puzzle as a node in a search tree. The nodes included the current state of the puzzle, the cost of moving from the initial state to the current state, and the estimated cost of moving from the current state to the goal state.
- I used the A* algorithm to search the tree for the optimal path from the initial state to the goal state. The algorithm considered both the cost of moving from the initial state to the current state and the estimated cost of moving from the current state to the goal state.
- Once the algorithm had found the optimal path, I used it to reconstruct the original image by moving the 16x16 boxes one by one.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have Python 3.x installed on your machine. You can download the latest version of [Python](https://www.python.org/downloads/) here.

#### Installing
```








