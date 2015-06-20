#include <stdio.h> 


int main() {
		int i=0;
		char buffer[4096], byte;

		while ((fread(&byte,1,1,stdin))) {
				if (byte=='\n') break;
				buffer[i]=byte; 
				i++; }

		buffer[i+1]='\0'; /* null terminate */
		printf("You entered: \"%s\"\n",buffer);

		for ( i = 0 ; i < 8; i++){
				unsigned short int uint = (unsigned short) buffer[i];
				printf("%c %hu\n", buffer[i], uint);
		}
		return 0;
}
