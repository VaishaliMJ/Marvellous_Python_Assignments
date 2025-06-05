
/*-------------------------------------------------------------------------------------------
                           Assignment2_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a number from user and 
                    displays the addition of it's factors
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_4 {
	
	public static void findFactors(int number) {
		System.out.println("Factors of "+number+" are:");
		for(int cnt=1;cnt<=number;cnt++) {
			if(number%cnt==0) {
				System.out.print(cnt+" ");
			}
		}
	}

	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		findFactors(number);
		inputObj.close();
		

	}

}
