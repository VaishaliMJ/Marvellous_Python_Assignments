
/*-------------------------------------------------------------------------------------------
                           Assignment2_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement :This program accepts a number from user and displays 
                    number of digits in the given number
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_8 {
	
	public static void countNumberOfDigits(int number) {
		int digitsCount=0;
		while(number!=0) {
				number=number/10;
				digitsCount=digitsCount+1;		
			
		}
			
		System.out.println("Number Of digits are:"+digitsCount);	
		
		
	}

	
	
	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		countNumberOfDigits(number);
		System.out.println("--------------------------------");

		
		inputObj.close();
		

	}

}
