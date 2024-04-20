# Neural Networks. Kohonen Networks

## [**Code**](/Lab6/Lab6.ipynb)

## [**Data**](/Lab6/Cohonen_data3.txt)

## Task 1: Solving the classification problem using a Kohonen layer.

1. Load the raw data into the computer's memory and display it on the screen. File Cohonen_data*.txt.
2. Create and train a Kohonen layer by setting the number of neurons equal to the assumed number of clusters.
3. Determine the cluster centers – coordinates of neurons net.IW{}, IW – cell array with weight matrices. IW{i, j} – matrices for layer i from input vector j. View the contents of the cell array.
4. Classify the original objects into clusters based on the principle of "the index of the neuron corresponds to the index of the cluster to which the given object is assigned."
5. Graphically display the found clusters and their centers (gscatter).
6. Define an arbitrary object close to one of the cluster centers (neurons). Classify this object (sim, vec2ind). Check the correctness of the object classification.

## Task2: Solving the clustering problem using Kohonen maps.

## [**Data_Fitting**](/Lab6/Learning_data3.txt)
## [**Data_PCA**](/Lab6/PCA_data3.txt)

1. Create a neural network (example, 2×2) based on Kohonen maps.
2. Train the network based on Kohonen maps (net.trainParam.epochs
=100, train) using your variant of the dataset. File Learning_data*.txt.
3. Classify the original objects into clusters using the developed neural network.
4. Load the PCA_data3.txt file according to your variant. The file contains the original data in the coordinates of the first two principal components Z1 and Z2. Graphically display the original data on a scatter plot considering the classification of objects by the neural network.
5. Group the objects into clusters, calculate the mean values for each feature in the clusters.
6. For each cluster, plot the average feature values of the objects (characteristic vectors) that belong to the cluster.
7. Display the projections of objects onto the Z1 and Z2 axes included in each cluster.

