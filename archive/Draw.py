import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

Matrix1 = [
	[4,9,2],
	[3,5,7],
	[8,1,6]
]

Matrix2 = [
	[2,16,13,3],
	[11,5,8,10],
	[7,9,12,6],
	[14,4,1,15]
]

Matrix3 = [
	[1,23,16,4,21],
	[15,14,7,18,11],
	[24,17,13,9,2],
	[20,8,19,12,6],
	[5,3,10,22,25]
]

Matrix4 = [
	[13,22,18,27,11,20],
	[31,4,36,9,29,2],
	[12,21,14,23,16,25],
	[30,3,5,32,34,7],
	[17,26,10,19,15,24],
	[8,35,28,1,6,33]
]
#FILL MATRIX FOR COLOR
Matrix = [
	[5,5,5],
	[5,5,5],
	[5,5,5]
]

#FILL MATRIX FOR MATRIX 3
MatrixF3 = [
	[0,0,0,0,0],
	[0,1,1,1,0],
	[0,1,1,1,0],
	[0,1,1,1,0],
	[0,0,0,0,0]
]

#FILL MATRIX FOR MATRIX 4
MatrixF4 = [
	[1,1,0,0,1,1],
	[1,1,0,0,1,1],
	[0,0,1,1,0,0],
	[0,0,1,1,0,0],
	[1,1,0,0,1,1],
	[1,1,0,0,1,1]
]

#For 3x3
fig, ax = plt.subplots()

ax.imshow(Matrix, cmap='gray_r')
for RowNo in range(3):
	for ColNo in range(3):
		ax.text(RowNo,ColNo, Matrix1[ColNo][RowNo], color='black', va='center', ha='center')

#ax.text(0,0, 4, color='black', va='center', ha='center')
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5,3,1));
ax.set_yticks(np.arange(-.5,3,1));

#for 4x4
fig_2, ax_2 = plt.subplots()
ax_2.imshow(Matrix, cmap='gray_r')
for RowNo in range(4):
	for ColNo in range(4):
		ax_2.text(RowNo, ColNo, Matrix2[ColNo][RowNo], color='black',va='center', ha='center')
ax_2.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax_2.set_xticks(np.arange(-.5,4,1));
ax_2.set_yticks(np.arange(-.5,4,1));

cmap = colors.ListedColormap(['white', 'grey'])
#for 5x5
fig_3, ax_3 = plt.subplots()
ax_3.imshow(MatrixF3, cmap=cmap)

for RowNo in range(5):
	for ColNo in range(5):
		ax_3.text(RowNo, ColNo, Matrix3[ColNo][RowNo], color='black', va='center', ha='center')
ax_3.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax_3.set_xticks(np.arange(-.5,5,1));
ax_3.set_yticks(np.arange(-.5,5,1));

#for 6x6
fig_4, ax_4 = plt.subplots()
ax_4.imshow(MatrixF4, cmap=cmap)

for RowNo in range(6):
	for ColNo in range(6):
		ax_4.text(RowNo, ColNo, Matrix4[ColNo][RowNo], color='black', va='center', ha='center')
ax_4.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax_4.set_xticks(np.arange(-.5,6,1));
ax_4.set_yticks(np.arange(-.5,6,1));
plt.show()
