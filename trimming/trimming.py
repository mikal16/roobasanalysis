import gzip
import os


for filename in os.listdir('/mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/'):
    if "_R1" in filename:
        tokens = filename.split('_R1')
        r1_name = tokens[0] + "_R1.fastq.gz"
        r1_name_trimmed = tokens[0] + "_R1.trimmed.fastq.gz"
        r2_name = tokens[0] + "_R2.fastq.gz"
        r2_name_trimmed = tokens[0] + "_R2.trimmed.fastq.gz"
        os.system('fastp --in1 /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/'+r1_name+' --in2 /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/'+r2_name+' --out1 /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/'+r1_name_trimmed+' --out2 /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/'+r2_name_trimmed+' -l 50 -h wgs.html &> wgs.log')
