import java.util.Scanner;
/*-----------------------------------------------------------------------------
                          Assignment6_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to print a multiplication table of a user accepted input
--------------------------------------------------------------------------------------------------*/
public class Assignment6_3 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter number to print the table:"); 
		int number=inputObj.nextInt();
		inputObj.close();
		

		printMultiplicationTable(number);
	}

	private static void printMultiplicationTable(int number) {
		System.out.println("------------------------------------------------------");
		System.out.println("\nPrinting multiplcation table of :"+number);
		System.out.println("------------------------------------------------------");
		for(int cnt=1;cnt<=10;cnt++) {
			
			System.out.println(number+"*"+cnt+"="+(number*cnt));
		}
	}
	
}
