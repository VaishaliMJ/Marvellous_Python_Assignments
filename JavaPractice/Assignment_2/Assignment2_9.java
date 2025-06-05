
/*-------------------------------------------------------------------------------------------
                           Assignment2_9
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement :This program accepets a number from user and displays
                     number in following matrix format of number*number
                     e.g. Input :accepted number 5
                     Output : 1 
                              1 2
                              1 2 3 
                              1 2 3 4 
                              1 2 3 4 5  
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_9 {
	
	public static void printNumberLeftTriangle(int number) {
		int loopCounter=AssignmentModule.Multiply(number, number);
		int colCnter=number;
		for(int row=0;row<number+1;row++) {
			for(int col=1;col<number+1;col++) {
				if(row<col) {
					break;
				}
				else
					System.out.print(col+" ");
			}
			System.out.println();
			
			
		}		
		
		
	}

	
	
	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		printNumberLeftTriangle(number);
		System.out.println("--------------------------------");

		
		inputObj.close();
		

	}

}
