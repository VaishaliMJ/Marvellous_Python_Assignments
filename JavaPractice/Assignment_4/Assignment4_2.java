import java.util.Scanner;

/*-------------------------------------------------------------------------------------------
                          Assignment4_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program contains a lambda function and returns number power of 2
------------------------------------------------------------------------------------------*/

public class Assignment4_2{

	
	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter First Number:"); 
		int number = inputObj.nextInt();
		
		MathsFunction square=  (num) ->num*num;
		int result=square.Square(number);
		System.out.println("Square of "+number+" is :"+result);
		
		
		inputObj.close();
	}

	
}
