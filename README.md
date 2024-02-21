# FASTA_arp-hap-haplotype-
## 介绍
This script is designed for processing FASTA files to generate ARP and HAP files, specifically tailored for haplotype analysis. 
这段代码主要用于处理FASTA文件，将其转化成ARP和HAP文件，特别适用于单倍型分析（haplotype analysis）。代码首先读取并解析FASTA文件，然后根据指定的分组文件将序列分组，并按组别排序。最后，它生成了两个文件：一个是包含序列信息的ARP文件，另一个是HAP文件，其中包含了各个单倍型的序列。此外，代码还支持删除原始的FASTA文件，以及生成的中间文件，从而只留下最终的ARP文件。这个脚本特别适合于那些需要对来自不同样本的序列进行分组和单倍型分析的研究人员。

This script is designed for processing FASTA files to generate ARP and HAP files, specifically tailored for haplotype analysis. It starts by reading and parsing a FASTA file, then groups and sorts the sequences according to a provided grouping file. The script outputs two files: an ARP file containing sequence information and a HAP file listing sequences of individual haplotypes. Additionally, the script supports deleting the original FASTA file and any intermediate files, leaving only the final ARP file. This script is particularly useful for researchers who need to group sequences from different samples for haplotype analysis.

## 使用方法
## windows平台可以运行，Linux我没试过。

1. 准备好你的FASTA文件。
2. 准备好你的分组文件。

FASTA文件格式应该类似于
>Li_Hainan1                            
CATTGTCGGTTTATTGACTGCGTTAGCTAAAGACAAATCGCTAGAGGCTTTCTTTGATATGTTGTATAAATCTTGAGCTCGTTCTACTCCACCTGTCCAGTTCATCGTATCA
>Li_Hainan2                            
CATTGTCGGTTTATTGACTGCGTTAGCTAAAAACAAATCGCTAGAGGCTTTCTTTGATATGTTGTATGAATCTTGAGCTCGTTCTACTCCACCTGTCCAGTTCATCGTATCA
>Li_Hainan3                            
CATTGTCGGTTTATTGACTGCGTTAGCTAAAGACAAATCGCTAGAGGCTTTCTTTGATATGTTGTATGAATCTTGAGCTCGTTCTACTCCACCTGTCCAGTTCATCGTATCA
.........
分组文件格式应该类似于：
Han_Banan_O1185	Chongqing
Han_Banan_o1236	Chongqing
Han_Bishan_o1448	Chongqing
Han_Changshou_O1835	Chongqing
Han_Chongqing787	Chongqing
Han_Chongqing800	Chongqing
Han_Chongqing801	Chongqing
Han_Chongqing807	Chongqing
Han_Chongqing809	Chongqing
Han_Chongqing816	Chongqing
Han_Chongqing848	Chongqing
Han_Chongqing857	Chongqing
Han_Chongqing863	Chongqing
Han_Chongqing875	Chongqing
............

3.修改代码中的路径
你只需要更改如下几个地方：
base_path = 'C:/Users/a/Desktop'#改成你的文件路径
    fasta_file_path = os.path.join(base_path, 'Illumina_mtDNA_Filter_recode.fas')#改成你自己文件的名字
    group_file_path = os.path.join(base_path, '新建文本文档.txt')#改成你自己文件的名字

base_path = 'C:/Users/a/Desktop'#改成你的文件路径

## 为什么？
为什么我不同DnaSP来分组？因为我懒得点。
而且，一旦我的数据太多，就会报错。
没办法。
