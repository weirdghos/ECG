#include <iostream> 
#include<string> //string ���� 
using namespace std;//ע�� 

int main(){
	int a=10;
	++a;  //�ȼ�1�ټ���  b2=++a*10 b2=a++*10(�����b��ֵ b=100 Ȼ��a+1) 
	float b=4.344f;//��f��ʾ������ ˫���Ȳ��ü� 
	bool c= true; 
	char cdd[]="hello world"; 
	cout<<cdd<<endl;
	cout<<"hello world\n";
	cout<<"a="<<sizeof(a)<<endl;
	system("pause");

	return 0;
}
/*
�������� int char float
1����  #define��const+���� 
2�ؼ��֣���ʶ����
3 ���� short 2�ֽ� int4 long4  longlong8   ʵ�� float��7λ��Ч���֣� double ��15 16λ��Ч���֣� �ַ��� char char='a' ������ֻ��һ����ĸ 
4 sizeof()�����������ռ���ֽ� 
5 ת���ַ� \aa��ӡ������ӿո� ����������� ���� \n \t \\
6 �ַ��� char a[]="sffffff" ������ ˫����
   string ������="z�ַ���" 
7 ��������  �������� cin>> �Ӽ������� 
8 ����� a++  ++a����  +=��������Ȼ��ֵ   �߼������ ����  &&�� ||�� if ����{} else if����   ��Ŀ����� a>b ?a:b ������������a����b
9 switch(�б�����){case1 case2 ..break}  do{}while���ж���������ִ�����ж� 
*/
