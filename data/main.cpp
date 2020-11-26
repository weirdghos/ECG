#include <iostream> 
#include<string> //string 引用 
using namespace std;//注释 

int main(){
	int a=10;
	++a;  //先加1再计算  b2=++a*10 b2=a++*10(先算出b的值 b=100 然后a+1) 
	float b=4.344f;//加f表示单精度 双精度不用加 
	bool c= true; 
	char cdd[]="hello world"; 
	cout<<cdd<<endl;
	cout<<"hello world\n";
	cout<<"a="<<sizeof(a)<<endl;
	system("pause");

	return 0;
}
/*
数据类型 int char float
1常量  #define与const+变量 
2关键字（标识符）
3 整型 short 2字节 int4 long4  longlong8   实型 float（7位有效数字） double （15 16位有效数字） 字符型 char char='a' 单引号只能一个字母 
4 sizeof()求出数据类型占用字节 
5 转义字符 \aa打印出来添加空格 对齐后面内容 多行 \n \t \\
6 字符串 char a[]="sffffff" 中括号 双引号
   string 变量名="z字符串" 
7 布尔类型  数据输入 cin>> 从键盘输入 
8 运算符 a++  ++a区别  +=与自生加然后赋值   逻辑运算符 ！非  &&与 ||或 if （）{} else if（）   三目运算符 a>b ?a:b 满足条件返回a否则b
9 switch(判别条件){case1 case2 ..break}  do{}while（判断条件）先执行再判断 
*/
