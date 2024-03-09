# Lab3 
## PCA

### [**Code**](/Lab3/Lab3.ipynb)

### Data

The data consists of 8 feature columns. The date is available [here](/Lab3/data3.txt).

### Task:

1. Develop the algorithm for the Principal Component Analysis (PCA) method and implement it programmatically.
2. Conduct an analysis of experimental data using the Principal Component Analysis method.
    1. Load the data according to your variant. Display the data on the monitor as a table.
    2. Normalize (standardize) the original experimental data. Build a correlation matrix.
    3. Ensure that the correlation matrix significantly differs from the identity matrix.
    4. Calculate the projections of objects onto the principal components.
3. Analyze the results of the Principal Component Analysis method.
    1. Check the equality of the sums of sample variances of the original features and the sample variances of projections onto the principal components.
    2. Determine the relative proportion of variance attributable to the principal components. Build a covariance matrix for projections onto the principal components.
    3. Based on the first M = 2 principal components, construct a scatter plot. Provide a meaningful interpretation of the first two principal components.


### Procedure:

1. Data was obtained from a .txt file.
2. Exploratory Data Analysis (EDA) was conducted on the obtained data. Descriptive statistics were displayed, distribution histograms and boxplot graphs were constructed.
3. The data were normalized using StandardScaler. Distribution histograms and boxplots were also created for the normalized data.
4. For the normalized data, Pearson and Kendall correlation matrices were constructed and displayed, along with a covariance matrix, which resembled the correlation matrix due to the normalization.
5. The value of d was calculated from the covariance matrix. From the theory: If the correlation matrix of the original data does not differ from the identity matrix (i.e., $\(d \leq \chi^2\)$ calculated at a given confidence level and degrees of freedom), then the application of the Principal Component Analysis method is not advisable.
6. Eigenvalues and eigenvectors were obtained using np.linalg.eig. The eigenvectors were used to project the original data onto the principal components, resulting in the Z matrix.
7. The variance of the projected data and the original data was calculated, and they closely matched, indicating the correct implementation of the PCA method.
8. The covariance matrix for Z was displayed.
9. The relative proportion of the spread attributable to the main components and the relative share of the spread attributable to the first i components were calculated.
10. A scatter plot for the first two principal components was constructed.
11. The results of the PCA implemented in sklearn were compared, and the same patterns were observed.
12. Another dimensionality reduction method, t-SNE, was applied, resulting in improved outcomes.
13. Yet another dimensionality reduction method, UMAP, demonstrated the best results.

