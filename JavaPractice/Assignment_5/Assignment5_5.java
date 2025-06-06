import java.util.Scanner;

/*-------------------------------------------------------------------------------------------
                          Assignment 5_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a number from the user and 
                    finds if number is even or odd
-----------------------------------------------------------------------------------------*/

public class Assignment5_5 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter  number :"); 
		int num=inputObj.nextInt();
		checkEvenOrOdd(num);
		inputObj.close();

	}

	private static void checkEvenOrOdd(int num) {
		if(num%2==0)
			System.out.println(num+" is an even number");
		else
			System.out.println(num+" is an odd number");		
			
	}


}
