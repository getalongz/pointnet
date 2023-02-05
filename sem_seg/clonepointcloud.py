import numpy as np
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

fold_path=BASE_DIR

def clonepcd(path,i):
    #文件名
    old_file1=path+"/jiancewall.txt"
    old_file2=path+"/jiancewindows.txt"
    new_file1=path+"/annotations/"+ str(i)+r"/wall_"+str(i)+".txt"
    new_file2=path+"/annotations/"+ str(i)+r"/windows_"+ str(i)+".txt"
    #偏移参数
    x_offset=random.uniform(-10, 10)
    y_offset=random.uniform(-10, 10)
    z_offset=random.uniform(-10, 10)

    #缩放参数
    scale=1.0

    #旋转角度
    roate_x=random.uniform(-np.pi/10, np.pi/10)
    roate_y=random.uniform(-np.pi/10, np.pi/10)
    roate_z=random.uniform(-np.pi/10, np.pi/10)

    roate_x_matrix=np.array([
                    [1,0,0,0],
                    [0,np.cos(roate_x),-np.sin(roate_x),0],
                    [0,np.sin(roate_x),np.cos(roate_x),0],
                    [0,0,0,1]
                    ])
    roate_y_matrix=np.array([
                    [np.cos(roate_y),0,np.sin(roate_y),0],
                    [0,1,0,0],
                    [-np.sin(roate_y),0,np.cos(roate_y),0],
                    [0,0,0,1]
                    ])
    roate_z_matrix=np.array([
                    [np.cos(roate_z),-np.sin(roate_z),0,0],
                    [np.sin(roate_z),np.cos(roate_z),0,0],
                    [0,0,1,0],
                    [0,0,0,1]
                    ])

    #变换矩阵
    transformation_matrix=np.array([
                            [scale,0,0,x_offset],
                            [0,scale,0,y_offset],
                            [0,0,scale,z_offset],
                            [0,0,0,1]
                            ]).dot(roate_z_matrix).dot(roate_y_matrix).dot(roate_x_matrix)


    #加载文件
    old_array1=np.loadtxt(old_file1)
    old_xyz1=old_array1[:,:3]
    old_array2=np.loadtxt(old_file2)
    old_xyz2=old_array2[:,:3]
    #补充数据为齐次项
    ones_data1=np.ones(old_xyz1.shape[0])
    old_xyz1=np.insert(old_xyz1,3,values=ones_data1,axis=1)
    ones_data2=np.ones(old_xyz2.shape[0])
    old_xyz2=np.insert(old_xyz2,3,values=ones_data2,axis=1)
    #变换数据
    new_xyz1 = np.dot(transformation_matrix,old_xyz1.T)
    new_array1=np.concatenate((new_xyz1.T[:,:3],old_array1[:,3:]),axis=1)
    np.savetxt(new_file1,new_array1,fmt='%.06f')
    new_xyz2 = np.dot(transformation_matrix,old_xyz2.T)
    new_array2=np.concatenate((new_xyz2.T[:,:3],old_array2[:,3:]),axis=1)
    np.savetxt(new_file2,new_array2,fmt='%.06f')

for i in range(0,100):
    clonepcd(fold_path,i)
