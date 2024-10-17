import gzip
import os

for filename in os.listdir('/mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/trimmed_fastqfiles/'):
    if "_R1" in filename:
        tokens = filename.split('_R1')
        r1_name = tokens[0] + "_R1.trimmed.fastq.gz"
        r2_name = tokens[0] + "_R2.trimmed.fastq.gz"
        pf_name = tokens[0]
        os.system('STAR --genomeDir /mnt/data/genomes/hg38_FullRef_OL/ --readFilesCommand zcat --runThreadN 16 --readFilesType Fastx --readFilesIn /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/trimmed_fastqfiles/'+r1_name+' /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/trimmed_fastqfiles/'+r2_name+' --outFileNamePrefix /mnt/data/archive/Smith_B_lungs_2024-08-20/working_copy/demultiplexing_cutadapt_output/rooba_human_cells/mapped/'+pf_name)

