import os
import shutil 
def cp_test(filename):
	shutil.copy(filename,'E:\Python_work\cp_test')#��Ҫ���ƻ��߼��е�Ŀ��·��������ʱĿ���ļ��в��ܴ���һ�����ļ�
def gci(filepath):
	files=os.listdir(filepath)
	for fi in files:
		fi_d=os.path.join(filepath,fi)
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			cp_test(fi_d)
def main():
	gci('E:\Python_work\cp_test_1')#��Ҫ���ƻ��߼��е�Դ·��
if __name__=='__main__':
	main()