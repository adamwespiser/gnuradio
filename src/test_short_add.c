#include <stdio.h>


int main(){
		unsigned short int one = 255;
		unsigned short int two = 255;
		unsigned short int three = 255;
		unsigned short int total = one + two + three;
		printf("sum = %hu\nsum/3 = %hu\n",total, total/3);
		return 0;
}
