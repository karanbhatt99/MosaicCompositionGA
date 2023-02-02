# Solving a Mosaic Art using Genetic Algorithm Approach
A Genetic Algorithm Approach to solve a shuffled image like a Mosaic Art using python.

# Importance and working of the Project
The interesting nature of solving a jigsaw puzzle captures the attention of research workers for the past few years. They use the same technique for the reconstruction of different images. A process of creating an original image from a broken image. This technique has scope in satellite imaging, medical imaging, computer vision, augmented reality, image-based search engines, etc. In this project, we try out a new technique, which works the same as the process of solving a jigsaw puzzle. We use an approach known as the Genetic algorithm (GA), we are checking every tile edge and orientation distance for solving the image using the cosine function because it performs very well for high dimensional data.

A GA is a sort of optimization algorithm inspired by the natural selection process. Each piece of the puzzle can be represented as a gene and each configuration of the puzzle as a chromosome. The GA method generally begins with a population of randomly created chromosomes and then performs genetic operators such as selection, crossover, and mutation to generate new generations of chromosomes repeatedly. The aim is to identify the best chromosome that symbolizes the proper puzzle layout. GA gradually explores the solution space and converges toward the optimal solution. We also use two image classification models Visual Geometry Group (VGG16) and Alex Net for identifying the objects in the image. We compared the scores of both models during every generation result.

We took a random image from the internet and split it into 25 tiles. Then we applied random shuffle on the tiles and use the shuffle image as our input image. 
Different images require setting up different parameters in the main file. Those parameters are:
- P_count: Number of Population.
- range: Number of Generations.
- retain: Percentage of choosing the best score individuals.
- random_select: Random selection of parents for mutation.
- mutate: Percentage of change in mutation. 

For our input image, the GA solved the image in 30 generations. we selected the target value as 1.0, population count as 1000, generation cycle as 50, retain as 0.2, random select as 0.05, and mutation as 0.01 to get the desired results. The image below shows the shape of the image during generation 0 and after generation 30. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/87089227/216111035-cf4896ee-c7f4-45b7-817e-7399993ac9dd.jpg?raw=true" alt="From gen 0 to gen 30"/>
</p>

We recorded every generation's fitness score. Our fitness score started from 2.450096484 and reached 0.75 fitness score where it completely solved the image. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/87089227/216119977-6232cee6-d6e4-45ca-90ed-c98e4cf0ae66.png?raw=true" alt="Score Plot"/>
</p>

#Image Classification Comparision
In this project, we also used two image classification models (AlexNet and VGG16) for detecting the objects on the image. This will help in applications like mosaic art reconstruction. We can use image classification models for detecting the objects in the images before reconstructing them. So we applied AlexNet and VGG16 on every image, starting from the shuffled image to the last generation image. These are the scores we get. Both models perform very well in detecting the object in the image but you can see the accuracy of VGG16 is better than Alex Net.

<p align="center">
  <img src="https://user-images.githubusercontent.com/87089227/216125317-feab3779-b38e-42c9-a849-56b3d162b44d.png?raw=true" alt="Image Model Comparison"/>
</p>

# Running of this Project
We did this whole project on Jupyter Notebook. If you want to run this project we recommend running it on Jupyter Notebook. For that you need to install:
- Python 3.7
- Anaconda
- Install all the required packages using the "Requirement.txt" file.
