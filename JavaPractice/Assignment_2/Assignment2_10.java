
/*-------------------------------------------------------------------------------------------
                           Assignment2_10
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement :This program accepts a number from user and displays addition  
                    of digits in the given number
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_10 {
	
	public static void countNumberOfDigits(int number) {
		int sumDigit=0;
		int digit=0;
		while(number!=0) {
				digit=number%10;
				sumDigit=sumDigit+digit;
				number=number/10;
			
		}
			
		System.out.println("Sum Of digits are:"+sumDigit);	
		
		
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
