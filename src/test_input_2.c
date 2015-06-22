#include <stdio.h> 


int verbose_read() {
		int i=0;
		unsigned char buffer[16], i_data[8], q_data[8];

		// read from buffer, load into array IQ, seperate IQ into
		// two diff arrays
		fread(&buffer,1,16,stdin);
		for ( i = 0; i < 8; i++){
				i_data[i]=buffer[i*2];
				
				q_data[i]=buffer[i*2 + 1];
				printf( "read: %hu\n", buffer[i]);
		}

		// print I array & Q array
		for ( i = 0; i < 8; i++){
				printf( " iq data: i = %hu, q = %hu\n", i_data[i], q_data[i]);
		}


		// convert IQ arrays into ints for additions
		unsigned short int i_ave, q_ave,i_sum = 0, q_sum = 0;
	//	= (unsigned short) buffer[i];
		for ( i = 0 ; i < 8; i++){
				i_sum += (unsigned short) i_data[i];
				q_sum += (unsigned short) q_data[i];
		}
		i_ave = i_sum / 8	;
		q_ave = q_sum / 8	;
		printf("i sum = %u, q sum = %u\ni ave = %u, q ave = %u\n", 
						i_sum, q_sum, i_ave, q_ave);
		return 0;
}


int main(){
		int i;
		for ( i = 0; i< 10; i++){

				int res = verbose_read();
				printf("==========================\n");
		}
		return 0;
}




