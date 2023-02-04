f = open("D:\\Program Files\\pointnet\\data\\indoor3d_sem_seg_hdf5_data\\all_files.txt", mode = "w")

#写字符串

for i in range(179):

    f.write("indoor3d_sem_seg_hdf5_data/ply_data_all_"+str(i)+".h5\n")

#写字符串或者列表

#f.writelines(内容)

#关闭输入流

f.close()