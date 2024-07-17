import cv2
import shutil
import os

# 定义输入文件夹和输出文件夹
input_folder = './data/boxes_6dof_colmap_easy/images_old'
output_folder = './data/boxes_6dof_colmap_easy/images_true'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有文件
input_files = os.listdir(input_folder)

# 遍历文件夹中的每个文件
# for i, filename in enumerate(input_files):
for i in range(0, len(input_files),1):
    # 构造完整的输入文件路径
    filename = input_files[i]
    input_file_path = os.path.join(input_folder, filename)
    
    # 构造输出文件名
    output_filename = '{:05d}.{}'.format(i, "png")
    # output_filename = '{:05d}.{}'.format(i+3, "png")
    # output_filename = '{:05d}.{}'.format(i+5, "png")
    
    # 构造完整的输出文件路径
    output_file_path = os.path.join(output_folder, output_filename)
    
    # 复制文件到输出文件夹，并重命名
    shutil.copy(input_file_path, output_file_path)
    print(f'Copied {filename} to {output_filename}')

print('All files copied successfully.')