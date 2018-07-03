import os
from operator import add
from pyspark import SparkContext

os.environ["SPARK_HOME"] = "C:\\Users\\plfoley\\spark-2.3.1-bin-hadoop2.7"
os.environ["HADOOP_HOME"]="C:\\Users\\plfoley\\winutils"

sc = SparkContext()

sortMe = sc.parallelize([3, 6, 2, 1, 4])

sorted = sortMe.map(lambda x: (x, 1))\
    .reduceByKey(lambda a, b: a + b) \
    .sortByKey(lambda tup: len(tup[1])) \
    .collect()

saveList = []
for x in range (len(sorted)):
    saveList.append(sorted[x][0])

print(saveList)
