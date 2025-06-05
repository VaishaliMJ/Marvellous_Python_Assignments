
import java.util.Scanner;
/*-------------------------------------------------------------------------------------------
			Assignment 2_2
			(Student name - Vaishali Jorwekar)
			Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
			Problem statement : This program accepts a number from user and displays
			number of * in following matrix format of number*number
						e.g. Input :accepted number 5
						Output * * * * *
 * * * * *  
 * * * * *
 * * * * *
 * * * * *  
-------------------------------------------------------------------------------------------*/


public class Assignment2_2 {
	static char STAR ='*';

	public static void printStars(int number) {
		System.out.println("Displaying * in "+number+"*"+number+" format");
		System.out.println("-------------------------------------------------");

		for(int row=1;row<=number;row++) {
			for(int column=1;column<=number;column++){
				System.out.print(STAR+" ");
			}
			System.out.println();
		}

		System.out.println("-------------------------------------------------");

	}
	public static void printStarsLoop(int number) {
		System.out.println("Displaying * in "+number+"*"+number+" format");
		System.out.println("-------------------------------------------------");
		int loopCounter=AssignmentModule.Multiply(number, number);

		for(int row=1;row<=loopCounter;row++) {
			if(row%number!=0) {
				System.out.print(STAR+" ");
			}
			else {
				System.out.print(STAR+"\n");
			}
		}
		System.out.println();


		System.out.println("-------------------------------------------------");

	}
	public static void main(String args[]) {
		Scanner inputObj=new Scanner(System.in);
		System.out.println("Enter the number to display * in matrix format:");
		int number=inputObj.nextInt();
		printStars(number);
		printStarsLoop(number);
		inputObj.close();
	}
}
