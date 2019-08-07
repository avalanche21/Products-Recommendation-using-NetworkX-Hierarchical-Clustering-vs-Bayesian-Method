# Products-Recommendation-using-NetworkX-Hierarchical-Clustering-vs-Bayesian-Method
This project helps Retail Industries to analyze the purchase transactions and come up with the Product Recommendation.
This project compares 2 methods, Bayesian method called Apriori algorithm with Hierarchical Clustering method, which also made use of NetworkX to find the relationship between each products.

The dataset consists of 207,873 purchasing transactions, 24 actegories of products. The figures show the Co-occurrence count graph of all the 24 products, and the result from Hierarchical Clustering result of and compares this result to the one we get from Apriori algorithm (Bayesian method)

(P.S. The other way to make a promotion to the customer is to do customer segmentation on this transaction data using RFM criteria)

The analysis encapsulates 3 steps:

1. first, run Product_Recommendation_project.py. (in python) it will return a complete graph and create a destance dataframe (df3.csv) to be used further

2.Second, run make_symmetric_distance_matrix.py (in python) to convert df3.csv to be sym_dist_matrix.csv

3.Third, run Hierarchical_Clustering_R.R (in RStudio) to perform Hierarchical Clustering
