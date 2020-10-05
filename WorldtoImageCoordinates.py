#Extract Human motion data from world to Image Coodrinates (3D)

import bpy
import csv

#Path for extracted data from .bvh file
name = 'D:/GitHub/02_ExtractDataFromBlender/bvh_data'
txt_file = name + '.txt'
csv_file = name + '.csv'
csv_header = ['Frame', 'Name', 'X', 'Y', 'Z']
matrix_csv = open(csv_file,'a', newline = '')
header = csv.writer(matrix_csv)
header.writerow(csv_header)
matrix_csv.close()
sce = bpy.context.scene
ob = bpy.context.object

#Range from start and end frame in Blender
for f in range(sce.frame_start, sce.frame_end+1):
     matrix_file = open(txt_file,'a')
     matrix_csv = open(csv_file,'a', newline = '')
     sce.frame_set(f)
     for pbone in ob.pose.bones:
         writer = csv.writer(matrix_csv)
         writer.writerow([str(f), str(pbone.name), str(pbone.matrix[0][3]), str(pbone.matrix[1][3]), str(pbone.matrix[2][3])])
         print(pbone.name, pbone.matrix[0][3], pbone.matrix[1][3], pbone.matrix[2][3])
         matrix_file.write('Frame: ' + str(f) + ' ' + str(pbone.name) + ' (X, Y, Z) = ' + str(pbone.matrix[0][3]) + ' ' + str(pbone.matrix[1][3]) + ' '+ str(pbone.matrix[2][3]) + '\n')
     matrix_file.close()
     matrix_csv.close()
