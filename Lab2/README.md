# Lab2
## Nonlinear least squares method

### [**Code**](/Lab2/lab2.ipynb)

### Data

The data consists of interval values of a variable, functions, and error values at each point. A total of 200 samples.

### Procedure:
1. Data on the argument, function, and errors were obtained from a .txt file.
2. Attempts were made to approximate the empirical data using three different distribution laws: Normal, Rayleigh, and Chi-square. Corresponding distribution functions were created.
3. The curve_fit function from the scipy module was imported to fit the parameters of the function used to approximate the data. The parameters are adjusted to minimize the squared error between the assumed function and the empirical data.
4. The normalized Chi-square criterion was calculated for each model with a significance level alpha = 0.05. Based on the p-value, a decision was made to accept or reject the null hypothesis of statistical difference between empirical data and the approximating function.
5. A residual distribution plot was created to visually assess the degree of agreement between measured data and the theoretical model.
6. An autocorrelation function of weighted residuals was constructed. If there are minor systematic deviations between experimental and theoretical characteristics that are indistinguishable from the residual distribution plot, an autocorrelation function of weighted residuals is used to detect them.
7. Confidence intervals were calculated for each parameter of the distribution function. Confidence intervals are intervals of values of the estimated parameter within which the true value of the parameter is with a certain probability β.
8. R2-score and Mean Squared Error (MSE) were calculated. R2-score, or the coefficient of determination, measures the proportion of the variance in the dependent variable that is predictable from the independent variable. A higher R2-score, closer to 1, indicates a better fit of the model to the data. Mean Squared Error (MSE) quantifies the average squared difference between predicted and actual values, providing a measure of the model's accuracy. A lower MSE signifies a better fit, with smaller errors between predicted and observed values.

### Resualts

| Function | Chi-square | p-value | Null-hypothesis | R2-score | MSE | Calculated param | Left confidence interval | Right confidence interval |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Normal | 38.34 | 0.0 | Reject | 0.84 | $0.00097$ | 1.44 | 1.42 | 1.75 |
|  |  |  |  | |  | 1.76 | 1.46 | 1.78 |
| Rayleigh | 62.17 | 0.0 | Reject | 0.19 | $0.00499$ | 1.98 | 1.96 | 2.00 |
| Chi-square | 1.10 | 0.15 | Accept | 0.98 | $7.72*10{-5}$ | 2.80 | 2.79 | 2.81 |