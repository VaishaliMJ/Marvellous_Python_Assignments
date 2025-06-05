
/*-------------------------------------------------------------------------------------------
                          Assignment2_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets a number from user and displays
                    factorial of given number
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_3 {
	public static void calculate_Factorial(int number) {
		int fact=1;
		for(int cnt=1;cnt<=number;cnt++) {
			fact=AssignmentModule.Multiply(fact,cnt);
			
		}
		System.out.println("Factorial of "+number+" Is:"+fact);
		
		
	}

	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		calculate_Factorial(number);
		inputObj.close();
		

	}

}
