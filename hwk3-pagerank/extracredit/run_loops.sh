#!/bin/bash

runHadoopJob() {
  # run one iteration of pagerank 
  hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -D mapreduce.job.reduces=1 \
  -files hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/mapper.py,hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/reducer.py \
  -mapper "python mapper.py" \
  -reducer "python reducer.py" \
  -input hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/data.txt \
  -output hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/output
  # set output file as new input file (note: at the end this will represent the OUTPUT)
  hdfs dfs -mv hwk3-pagerank-ec/output/part-00000 hwk3-pagerank-ec/data.txt
  # remove output directory 
  hdfs dfs -rf -r hwk3-pagerank-ec/output
}

main(){
  # run pagerank 3 times 
  for i in {1..3};
  do runHadoopJob;
  done 
}

main