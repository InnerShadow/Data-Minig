# Lab3 
## Hierarchical clustering

### [**Code**](/Lab4/Lab4.ipynb)

### Data
The data consists of 2 feature columns. [**Dataset**](/Lab4/data3.txt).


### Task
1. Load the data according to your variant. Construct a graphical representation of the experimental data.
2. Compute distances between objects. Use measures to calculate distances: Euclidean distance, standardized Euclidean distance, Minkowski distance with p = 4.
3. Perform cluster analysis of the original data using hierarchical clustering methods: single linkage clustering, complete linkage clustering, median linkage clustering.
4. Perform clustering quality analysis by calculating the cophenetic correlation coefficient. Fill in the table for the cophenetic correlation coefficient.
5. Determine the most and least effective hierarchical clustering methods for analyzing the original dataset (maximum and minimum coefficients and their corresponding clustering methods). For the most effective hierarchical clustering method, construct a dendrogram of the clustering analysis results.
6. Determine the number of reliable clusters. To identify significant clusters, use a threshold value calculated using distance metrics or by specifying a fixed number of clusters.
7. Calculate the centroids and intra-cluster dispersion of the obtained clusters, geometric distances from the elements to the cluster centers, and distances between the cluster centers. Graphically display the identified clusters and their centroids (use a scatter plot in color).

docs"
### Procedure
1. The data was loaded from a txt file and converted into a Pandas DataFrame.
2. A scatter plot was constructed showing all values on the plane, with possible clusters also indicated by gradients.
3. The elbow method was used to determine the number of clusters, which in this case is 4 clusters.
4. A table was created to store correlation coefficients.
5. Hierarchical clustering was performed using the scipy library for three different linkage methods. For each linkage method, the correlation coefficient was calculated and entered into the table.
6. For the best clustering method (standardized Euclidean distance with median linkage), a dendrogram was constructed showing the clustering process.
7. The cluster centers and dispersion within each cluster were calculated, along with descriptive statistics for each cluster.
8. A jointplot was constructed to visualize the distribution of objects across clusters.


### Results

|  | nearest neighbor | far neighbor | median relationship |
|:-:|:-:|:-:|:-:|
| Euclidean | 0.906 | 0.915 | 0.918 |
| standardized Euclidean | 0.958 | 0.958 | 0.960 |
| Minkowski | 0.902 | 0.918 | 0.920 |