import java.util.Scanner;
/*-----------------------------------------------------------------------------
                          Assignment6_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept a number and print its factorial using for loop
------------------------------------------------------------------------------------*/
public class Assignment6_4 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter number to find the factorial:"); 
		int number=inputObj.nextInt();
		inputObj.close();
		calculateFactorial(number);
		
	}

	private static void calculateFactorial(int number) {
		int fact=1;
		if(number>0) {
			for(int cnt=number;cnt>=1;cnt--) {
				fact=fact*cnt;
			}
			System.out.println("------------------------------------------------------");
			System.out.println("\nFactorial of "+number+" is :"+fact);
			System.out.println("------------------------------------------------------");
			
			
		}
		else {
			System.out.println("Can not calculate factorial of 0");
		}
	}
	
}
