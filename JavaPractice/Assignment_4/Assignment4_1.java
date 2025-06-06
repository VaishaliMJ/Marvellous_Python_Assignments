import java.util.Scanner;

/*-------------------------------------------------------------------------------------------
                          Assignment4_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program contains a lambda function and returns multiplication
------------------------------------------------------------------------------------------*/

public class Assignment4_1{

	
	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter First Number:"); 
		int number1 = inputObj.nextInt();
		System.out.print("Enter Second Number:"); 
		int number2 = inputObj.nextInt();
		
		
		Arithmetic multi=  (num1,num2) ->num1*num2;
		int result=multi.processNums(number1,number2);
		System.out.println("Multiplication of "+number1+"*"+number2+" is :"+result);
		
		
		inputObj.close();
	}

	
}
