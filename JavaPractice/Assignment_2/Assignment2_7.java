
/*-------------------------------------------------------------------------------------------
                           Assignment2_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement :This program accepets a number from user and displays
                     number in following matrix format of number*number
                     e.g. Input :accepted number 5
                     Output : 1 2 3 4 5
                              1 2 3 4 5
                              1 2 3 4 5
                              1 2 3 4 5
                              1 2 3 4 5  
------------------------------------------------------------------------------------------*/
import java.util.Scanner;




public class Assignment2_7 {
	static char STAR ='*';
	
	public static void printNumbers(int number) {
		
		for(int row=1;row<=number;row++) {
			for(int col=1;col<=number;col++) {
				System.out.print(col+" ");
			}
			System.out.println();
			
			
		}		
		
		
	}
	
	
	public static void main(String[] args) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number:");
		int number=inputObj.nextInt();
		printNumbers(number);
		System.out.println("--------------------------------");


		inputObj.close();
		

	}

}
