import java.util.Scanner;
/*-------------------------------------------------------------------------------------------
                          Assignment 5_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts two numeric inputs from the user and performs 
                    arithmetic operations on them. 
-----------------------------------------------------------------------------------------"*/

public class Assignment5_1 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter First Number:"); 
		int number1 = inputObj.nextInt();
		System.out.print("Enter Second Number:"); 
		int number2 = inputObj.nextInt();
		processNumbers(number1,number2, inputObj);
		inputObj.close();

	}

	private static void processNumbers(int number1, int number2,Scanner inputObj) {
		// TODO Auto-generated method stub
		int choice=0;
		String continueProcess= "yes";
		while(continueProcess.equalsIgnoreCase("yes")|| continueProcess.equalsIgnoreCase("y")) {
			System.out.println("\n1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Exit");
			System.out.println("\nEnter the choice of operation:");

			choice=inputObj.nextInt();
			switch(choice) {
			case 1:
				ArtithmeticModule add=(num1,num2)->num1+num2;
				int result=add.Arithmetic(number1,number2);
				System.out.println("Addition of "+number1+"+"+number2+" is :"+result);
				break;




			case 2:
				ArtithmeticModule sub=  (num1,num2) -> num1-num2;
				result=sub.Arithmetic(number1,number2);
				System.out.println("Subtraction of "+number1+"-"+number2+" is :"+result);
				break;


			case 3:
				ArtithmeticModule multi=  (num1,num2) -> num1*num2;
				result=multi.Arithmetic(number1,number2);
				System.out.println("Multiplication of "+number1+"*"+number2+" is :"+result);
				break;

			case 4:
				if(number2==0) {
					System.out.println("Division not possible...");
				}else {
					ArtithmeticModule div=  (num1,num2) -> num1/num2;
					result=div.Arithmetic(number1,number2);
					System.out.println("Division of "+number1+"*"+number2+" is :"+result);
				}
				break;

			default:
				System.out.println("Invalid choice....");

			}

			System.out.println("Do you want to contuinue(yes/no)?:");
			continueProcess= inputObj.next();
		}
	}

}
