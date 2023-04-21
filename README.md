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
</br>
You will also need to have Anaconda on your machine. You can download the latest version of [Anaconda](https://www.anaconda.com/) here.

### Installing
Clone this repository onto your local machine.
```
git clone https://github.com/MuhammadAhmedSuhail/Image-Reconstruction-using-AI.git
```
Install the required packages.
```
pip install -r requirements.txt
```
**Note**
> Make Sure to have the picture named as pic.jpg in the same directory as the python program.
## Running the Program
To run the program, simply execute the following command in your terminal:
```
python main.py
```
The A* algorithm will begin running to find the optimal path to reconstruct the image. Once the algorithm has finished, the reconstructed image will be displayed.
## Built with:
- Python3 - Programming Language Used
- Skimage - Library used for reading/writing and formatting the image
- Matplotlib - Library used for displaying the image 
## Results
My implementation of the A* algorithm was successful in reconstructing the original image from the shuffled image.
The program displays the shuffled and reconstructed images side by side and the reconstructed image closely matched the original image.


Original Image             |  Initial Image            | Goal Image
:-------------------------:|:-------------------------:|:-------------------------:
 ![Original](https://user-images.githubusercontent.com/72251313/232824633-9dac0864-32fc-4206-bd7a-57b3ad4f0231.png) | ![Init](https://user-images.githubusercontent.com/72251313/232823971-a52ca173-81e3-4c99-a31c-054e2a472ce8.png) | ![Goal](https://user-images.githubusercontent.com/72251313/232823966-d93f8c42-c8c5-4b78-a498-6770ec4fdf88.png)

## Limitations
The limitation of my approach is that it may not be efficient for larger images or more complex puzzles. The A* algorithm is known to be computationally expensive, and the search tree can grow rapidly as the puzzle becomes larger or more complex. Additionally, my implementation assumed that the shuffled image was solvable, meaning that it could be reconstructed by moving the boxes. In cases where the image is not solvable, my program would not be able to reconstruct the original image.

## Future Work
In the future, I could explore other algorithms for solving image reconstruction puzzles, such as the depth-first search algorithm or the breadth-first search algorithm. I could also investigate techniques for optimizing the performance of the A* algorithm, such as using heuristic functions that more accurately estimate the distance to the goal state. Finally, I could test my program on a wider variety of images and puzzle sizes to evaluate its scalability and robustness.

## Author:
- Muhammad Ahmed Suhail

## Acknowledgments:
- This project was completed as an assignment for **Introduction to Artificial Intelligence** at FAST - NUCES Islamabad.









