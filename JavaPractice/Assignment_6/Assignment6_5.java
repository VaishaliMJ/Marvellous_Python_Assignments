import java.util.Scanner;
/*------------------------------------------------------------------------------
                          Assignment6_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept a number from user checks if it's prime or not
----------------------------------------------------------------------------------------*/
public class Assignment6_5 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter number to find the Prime or not:"); 
		int number=inputObj.nextInt();
		inputObj.close();

		boolean isPrime=checkPrime(number);
		if(isPrime) {
			System.out.println(number+" is a Prime number");

		}		
		else {
			System.out.println(number+" is not a Prime number");
		}

	}

	private static boolean checkPrime(int number) {
		if(number<=1) {
			return false;
		}
		for(int cnt=2;cnt<number;cnt++) {
			if(number%cnt==0)
				return false;

		}

		return true;


	}

}
