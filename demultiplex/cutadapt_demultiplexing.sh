#!/bin/bash

cd /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output

source /bioinformatics/miniconda3/bin/activate
conda activate scanpy

# Define the input files
r1_file="/mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/240812_A00546_0181_AHT5NCDRX3_demultiplexed2/Undetermined_S0_R1_001.fastq.gz"  # Path to your R1 file
r2_file="/mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/240812_A00546_0181_AHT5NCDRX3_demultiplexed2/Undetermined_S0_R2_001.fastq.gz"  # Path to your R2 file

# Path to your CSV file (containing sample_name, i7_index, i5_index)
csv_file="/mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/indices.csv"

# Read the CSV and process each sample
while IFS=, read -r sample_name i7_index i5_index
do
    echo "Processing sample: $sample_name"
    echo "i7 index: $i7_index, i5 index: $i5_index"

    # Run cutadapt for each sample
    cutadapt -g ^${i7_index} -G ^${i5_index} \
        -o ${sample_name}_R1.fastq.gz \
        -p ${sample_name}_R2.fastq.gz \
        ${r1_file} ${r2_file}

    echo "Completed processing for $sample_name"
done < "$csv_file"
