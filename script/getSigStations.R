

#### TODO 
# disregard peaks that occupy multiple valid stations 
f = "worc-Scan-87.0-108.0MHz.csv"
df <- read.csv(file=f,stringsAsFactors=FALSE)
stations = rep(87:108,each=5)+ c(seq(1,9,by=2)/10)
thresh = -45
df.above <- df[df[,3] > thresh, ]


# find the closest station index, select station, return only unique
found = unique(stations[sapply(df.above[,2], function(st)which((st-stations)^2 == min((st-stations)^2))[1])])

for (x in found){
		print(x);
}



