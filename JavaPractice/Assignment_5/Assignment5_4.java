import java.util.Scanner;
/*-------------------------------------------------------------------------------------------
                          Assignment 5_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts Three numeric inputs from the user and
                    finds maximum number 
----------------------------------------------------------------------------------------*/

public class Assignment5_4 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter first number :"); 
		int num1=inputObj.nextInt();
		System.out.print("Enter second number :"); 
		int num2=inputObj.nextInt();
		System.out.print("Enter third number :"); 
		int num3=inputObj.nextInt();
		
		
		findMaximumNumber(num1,num2,num3);
		inputObj.close();

	}

	private static void findMaximumNumber(int num1,int num2,int num3) {
		int max=0;
		if(max<num1)
			max=num1;
		if(max<num2)
			max=num2;
		if(max<num3)
			max=num3;
		System.out.println("Maximum number is :"+max);
			
			
			
	}


}
