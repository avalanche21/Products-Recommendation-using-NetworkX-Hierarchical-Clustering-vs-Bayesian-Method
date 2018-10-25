
# perform Hierarchical Clustering
dist_mtx = read.csv("sym_dist_matrix.csv")
print(dist_mtx)
max(dist_mtx)
# drop the first column
dist_mtx = dist_mtx[,-1]

# we see that the max value in the distance matrix = 4304
max(dist_mtx)
# invert the data by (max+1) - (value)
max = max(dist_mtx)
dist_mtx = (max+1)- dist_mtx

DF <- data.frame(dist_mtx)

d <- as.dist(DF)
mds.coor <- cmdscale(d)
plot(mds.coor[,1], mds.coor[,2], type="n", xlab="", ylab="")
text(jitter(mds.coor[,1]), jitter(mds.coor[,2]),
     rownames(mds.coor), cex=0.8)
abline(h=0,v=0,col="gray75")
plot(hclust(dist(1-DF), method="single"))



