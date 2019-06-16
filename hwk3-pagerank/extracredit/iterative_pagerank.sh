#!/bin/bash  

function runHadoopJob {

	echo "Running iteration $1..."
	output_path="hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/output_$1"
	output_file=$output_path"/part-00000"

	# run one iteration of pagerank 
	hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapreduce.job.reduces=1 \
	-files hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/mapper.py,hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/reducer.py \
	-mapper "python mapper.py" \
	-reducer "python reducer.py" \
	-input hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/input_data.txt \
	-output $output_path

	# set output file as new input file (note: at the end this will represent the OUTPUT)
	hdfs dfs -mv -f $output_file hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/input_data.txt

}


function main {

	# run Hadoop jobs iteratively 
	for i in $(seq 1 $num_iterations); do 
		runHadoopJob $i
	done 

	# save final result 
	final_path="hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/output_$num_iterations"
	hdfs dfs -mv final_path hdfs://dumbo/user/yjn214/hwk3-pagerank-ec/final_output

}

if [ $# -eq 0 ]; then 
	echo "No argument supplied. Setting num_iterations = 3!"
	num_iterations=3
else 
	num_iterations=$1
fi 

main 
