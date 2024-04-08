# Lab5
## K-means clustering

### [**Code**](/Lab5/Lab5.ipynb)

### Data
The data consists of 2 feature columns. [**Dataset**](/Lab5/data3.txt).


### Task
1. Upload the data. Construct a graphical representation of the experimental data (scatter plot). Visually assess the number of clusters, k, based on the constructed representation.
2. Develop the k-means clustering algorithm and implement it programmatically in MATLAB.
3. Perform cluster analysis on the original data using the k-means method (see method parameters in Table 5.2). Determine the most optimal number of clusters, k.
5. Calculate the centroids of the obtained clusters. Visualize the found clusters graphically (utilize a colored scatter plot).


### Procedure
1. The dataset was obtained from a txt file and converted into a pd.Dataframe for greater convenience.
2. A scatter plot was constructed for the original dataset.
3. The elbow method was applied to determine the optimal number of clusters. In this task, 4 clusters were identified.
4. The k-means method was implemented from scratch with Euclidean distance metric and intra-cluster sum of distances as the clustering quality metric.
5. Plots were generated for each step of the k-means algorithm.
6. A joint plot was created to visualize the final distribution of data across clusters.