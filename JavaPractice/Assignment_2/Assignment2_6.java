
/*-------------------------------------------------------------------------------------------
                           Assignment2_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement :This program accepts a number from user and displays
                     number of * in following matrix format of number*number
                     e.g. Input :accepted number 5
                     Output * * * * *
                            * * * *  
                            * * * 
                            * * 
                            *  
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_6 {
	static char STAR ='*';
	
	public static void printStars(int number) {
		int loopCounter=AssignmentModule.Multiply(number, number);
		int colCnter=number;
		for(int row=0;row<number;row++) {
			for(int col=0;col<colCnter;col++) {
				System.out.print(STAR+" ");
			}
			colCnter=AssignmentModule.Subtraction(colCnter,1);	
			System.out.println();
			
			
		}		
		
		
	}

	public static void printStarsLoop(int number) {
		int loopCounter=AssignmentModule.Multiply(number, number);
		int colCnter=number;
		for(int row=number;row>=1;row--) {
			for(int col=1;col<=row;col++) {
				System.out.print(STAR+" ");

			}
			System.out.println();

		}
		
		
	}
	
	
	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		printStars(number);
		System.out.println("--------------------------------");

		printStarsLoop(number);
		System.out.println("--------------------------------");

		inputObj.close();
		

	}

}
