# -*- coding: utf-8 -*-
A=['   #   ','  # #  ',' #   # ',' ##### ','#     #','#     #','#     #']
B=['###### ','#     #','#     #','###### ','#     #','#     #','###### ']
C=[' ##### ','#     #','#      ','#      ','#      ','#     #',' ##### ']
D=['#####  ','#    # ','#     #','#     #','#     #','#    # ','#####  ']
E=['#######','#      ','#      ','#######','#      ','#      ','#######']
F=['#######','#      ','#      ','#######','#      ','#      ','#      ']
G=[' ##### ','#     #','#      ','#  ####','#     #','#     #',' ##### ']
H=['#     #','#     #','#     #','#######','#     #','#     #','#     #']
I=[' ##### ','   #   ','   #   ','   #   ','   #   ','   #   ',' ##### ']
J=['#######','    #  ','    #  ','    #  ','    #  ','#   #  ',' ###   ']
K=['#     #','#    # ','#   #  ','####   ','#   #  ','#    # ','#     #']
L=['#      ','#      ','#      ','#      ','#      ','#      ','#######']
M=[' #   # ','# # # #','#  #  #','#  #  #','#  #  #','#  #  #','#  #  #']
N=['#     #','##    #','# #   #','#  #  #','#   # #','#    ##','#     #']
O=[' ##### ','#     #','#     #','#     #','#     #','#     #',' ##### ']
P=['###### ','#     #','#     #','###### ','#      ','#      ','#      ']
Q=[' ##### ','#     #','#     #','#  #  #','#   # #','#    # ',' #### #']
R=['###### ','#     #','#     #','###### ','#   #  ','#    # ','#     #']
S=[' ######','#      ','#      ',' ##### ','      #','      #','###### ']
T=['#######','   #   ','   #   ','   #   ','   #   ','   #   ','   #   ']
U=['#     #','#     #','#     #','#     #','#     #','#     #',' ##### ']
V=['#     #','#     #','#     #','#     #',' #   # ','  # #  ','   #   ']
W=['#  #  #','#  #  #','#  #  #','#  #  #','#  #  #',' # # # ','  # #  ']
X=['#     #',' #   # ','  # #  ','   #   ','  # #  ',' #   # ','#     #']
Y=['#     #',' #   # ','  # #  ','   #   ','   #   ','   #   ','   #   ']
Z=['#######','     # ','    #  ','   #   ','  #    ',' #     ','#######']
alphabet=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
str=raw_input()                     #输入字符串
list=list(str)                      #将字符串转换为list
list_length=len(list)               #计算list长度
for i in range(list_length):
    list[i]=ord(list[i])-65         #将list中每一个字符对应的ASCII码转换为其在alphabet中的索引位置
for j in range(7):                  #将所输入的字符串中字母对应图案分行输出
    for k in list:
        print alphabet[k][j],' ',   #输出所输入的字符串中所有字母对应图案的其中一行
    print                           #输出完一行后换行