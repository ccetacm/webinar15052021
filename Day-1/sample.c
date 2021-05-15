
/*

During translations that they devide your code in two parts

GCC compiler (C-language)

->  =={
(global variables that are not static) .data
  
int c=2;
int b=0;
char d=0;


(uninitaialized variables that are static)   .bss
static int b=0;
static int c=0;

}
           


-> Intructions    .text
a=a+b
a=a--



//text section
     

*/


/*----------C Code--------------------*/

int c=2;         //4-bytes                
static int d=3;   //4-bytes
char f=2; //1-byte
static char e;   
int main(){                       
//some data                        
//some instructions

}

/*--------------translation.exe----------------
   
[00000100 00000000 00000000 00000000] .data
0000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
.
.
.
.
[00000000 00000000 00000000 00000000]   //bss-section
0000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000
.
.
.
.
.
[in binary form instructions]              //text-section
00000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000
.
.
.
.
.
.
0000000000000000000000000000000000000000000000EOF
*/