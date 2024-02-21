import os
from collections import defaultdict

# 功能函数定义
def read_group_file(group_file_path):
    """读取分组文件并创建一个映射关系的字典"""
    group_map = {}
    with open(group_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                sample_name, group_name = parts
                group_map[sample_name] = group_name
    return group_map

def read_fasta_file(fasta_file_path):
    """读取fasta文件并返回一个包含样本名称和序列的字典"""
    fasta_data = {}
    current_sample = None
    with open(fasta_file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                current_sample = line.strip()[1:]
                fasta_data[current_sample] = ''
            else:
                fasta_data[current_sample] += line.strip()
    return fasta_data

def replace_and_sort_fasta_samples(fasta_file_path, group_file_path, output_file_path):
    """替换fasta文件中的样本名称并排序，然后保存到新的文件中"""
    group_map = read_group_file(group_file_path)
    fasta_data = read_fasta_file(fasta_file_path)
    replaced_fasta_data = {}
    for name, seq in fasta_data.items():
        group_name = group_map.get(name, 'Unknown')
        replaced_fasta_data[f'{group_name} {name}'] = {'sequence': seq, 'province': group_name}
    with open(output_file_path, 'w') as output_file:
        for sample in sorted(replaced_fasta_data, key=lambda x: replaced_fasta_data[x]['province']):
            output_file.write(f'>{sample}\n{replaced_fasta_data[sample]["sequence"]}\n')

# 主执行逻辑
if __name__ == "__main__":
    base_path = 'C:/Users/a/Desktop'
    fasta_file_path = os.path.join(base_path, 'Illumina_mtDNA_Filter_recode.fas')#改成你自己文件的名字
    group_file_path = os.path.join(base_path, '新建文本文档.txt')#改成你自己文件的名字
    output_file_path = os.path.join(base_path, 'New.fasta')#别改！！！Don't change it!

    replace_and_sort_fasta_samples(fasta_file_path, group_file_path, output_file_path)
########################################################################################
########################################################################################
########################################################################################

import os
from collections import defaultdict

# 设置基本路径
base_path = 'C:/Users/a/Desktop'#改成你的文件路径

# 文件路径
file_path = os.path.join(base_path, 'New.fasta') #别改！Don't change it!
new_file_path = os.path.join(base_path, 'New.arp')#别改！Don't change it!
new_file_txt_path = os.path.join(base_path, 'New.hap')#别改！Don't change it!
header_arp_path = os.path.join(base_path, '开头.arp')#别改！Don't change it!
final_arp_path = os.path.join(base_path, '最终.arp')#别改！Don't change it!

# 读取和解析 New.fasta 文件
sequences = {}
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            parts = line[1:].split(' ')
            group = parts[0]
            seq_id = parts[1]
            sequences[seq_id] = {'group': group, 'sequence': ''}
        else:
            sequences[seq_id]['sequence'] += line

# 计算组别数量
group_set = set(details['group'] for details in sequences.values())
Group_Number = len(group_set)

# 初始化用于存储唯一序列及其对应hap类型的字典和统计
unique_sequences = {}
group_hap_counts = defaultdict(lambda: defaultdict(int))
hap_counter = 1

# 分配hap类型并统计
for seq_id, details in sequences.items():
    seq = details['sequence']
    group = details['group']
    if seq not in unique_sequences:
        hap_label = f'Hap_{hap_counter}'
        unique_sequences[seq] = hap_label
        hap_counter += 1
    else:
        hap_label = unique_sequences[seq]
    group_hap_counts[group][hap_label] += 1

# 写入New.arp文件
with open(new_file_path, 'w', encoding='utf-8') as new_file:
    for group, haps in group_hap_counts.items():
        new_file.write(f'[[Samples]]\nSampleName = "{group}"\nSampleSize = {sum(haps.values())}\nSampleData= {{\n')
        for hap, count in haps.items():
            new_file.write(f'    {hap} {count}\n')
        new_file.write('}}\n\n')

# 写入New.hap文件
with open(new_file_txt_path, 'w', encoding='utf-8') as txt_file:
    for seq, hap_label in unique_sequences.items():
        txt_file.write(f'{hap_label}\t{seq}\n')

# 创建并写入开头.arp文件
with open(header_arp_path, 'w', encoding='utf-8') as header_file:
    header_file.write("[Profile]\n   Title = \"Haplotype Data from I fuck DnaSP file\"\n")
    header_file.write(f"   NbSamples = {Group_Number}\n   DataType = DNA\n   GenotypicData = 0\n")#如果你的数据是二倍体，需要将GenotypicData = 1
    header_file.write("   LocusSeparator = NONE\n   MissingData = \"?\"\n   CompDistMatrix = 1\n\n[Data]\n\n")
    header_file.write("[[HaplotypeDefinition]]\n   HaplList = EXTERN \"New.hap\"\n\n")

# 将New.arp的内容追加到开头.arp
with open(header_arp_path, 'a', encoding='utf-8') as header_file, open(new_file_path, 'r', encoding='utf-8') as new_file:
    header_file.write(new_file.read())

# 重命名或移动文件以创建最终.arp
os.rename(header_arp_path, final_arp_path)

# 删除生成的New.arp文件
os.remove(new_file_path)

print(f"最终文件已保存至: {final_arp_path}")
# 删除位于C:/Users/a/Desktop的New.fasta文件
fasta_file_path = os.path.join(base_path, 'New.fasta')
os.remove(fasta_file_path)

print(f"文件 {fasta_file_path} 已被删除。")
print("给我点个赞如何？")
