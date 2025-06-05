
/*-------------------------------------------------------------------------------------------
                           Assignment2_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a number from user and 
                    checks if number is PRIME
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_5 {
	
	public static boolean checkPrime(int number) {
		boolean isPrime=true;
		if(number<=1) {
			isPrime= false;
		}
		for(int cnt=2;cnt<number;cnt++) {
			if(number%cnt==0) {
				isPrime= false;
				break;
			}
		}
		return isPrime;
	}

	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		boolean flag=checkPrime(number);
		System.out.println(flag);
		if(flag)
			System.out.println(number+" is a PRIME number");
		else
			System.out.println(number+" is not a PRIME Number");
			
		inputObj.close();
		

	}

}
