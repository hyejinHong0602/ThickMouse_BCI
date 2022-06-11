# -*- coding: cp949 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from time import sleep

data = [] # data ���� �迭
address = 'C:/MAVE_RawData/2022-06-10_���� 2_57' # ������ ���� ���
#sleep(5)


# �� ����
def draw_graph(data):
    #ecg = np.loadtxt(file,delimiter="�t",unpack=False)
    # x��
    time = data[:, 0]
    # y��
    amplitude = data[:, 1]

    # plot ����
    plt.figure(num=1, dpi=100, facecolor='white')
    plt.plot(time, amplitude, color="blue", linewidth=0.5)

    plt.title('ecg')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.xlim(1, 1204)
    plt.ylim(-0.0003, 0.0003)

    plt.show()

#���⼭����
delay_time_1 = 0 # ������ �ð�
with open(r"C:/MAVE_RawData/2022-06-10_���� 2_57/Fp1_FFT.txt","r") as f:  # mave���� recoding �� ���� ��� ����
    while True:
        where = f.tell()
        line = f.readline().strip().replace('����','').split(sep='�t',maxsplit=641)
        # ���پ� �б� / FFT�� '����' ������ �׷��� �ȱ׷����� ����. split tab�������� 641�� ��
        if not line or line == ['']:
            sleep(0.1)
            delay_time_1 += 0.1
            f.seek(where)
            if delay_time_1 > 1.5:
                print("Delay has benn exceed.")
                break
        else:
            delay_time_1 = 0
            print(line)
            data.append(line)
            df = pd.DataFrame(data)
            #df.to_csv(address + '/test1.csv', sep='�t', index=False)
            #draw_graph(data)