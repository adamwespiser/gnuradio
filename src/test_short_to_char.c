#include <stdio.h>
// short program to test the conversion of short int(2 byte)
// to an unsigned char (1 byte)


int main(){


		unsigned int a = 1;
		unsigned int x = 135;
		unsigned int y = 135;


		unsigned char xc = (unsigned char) x;
		unsigned char yc = (unsigned char) y;
			
		printf ("x int = %i, y int = %i, a int = %i \n x uchar = %hu, y uchar = %hu\n", 
						x,y,a, xc, yc);

		unsigned char xyc = (unsigned char) (y + x);
		printf("x + y (uchar) = %hu \n", xyc);

		unsigned char xac = (unsigned char) (y + a);
		printf("x + a (uchar) = %hu \n", xac);



		
		return 0;
}
