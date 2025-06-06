import java.util.Scanner;

/*-------------------------------------------------------------------------------------------
                          Assignment 5_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts age from the user and checks 
                if person is eligible for vote
---------------------------------------------------------------------------------------------*/

public class Assignment5_3 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter the age :"); 
		int age=inputObj.nextInt();
		
		isEligibleToVote(age);
		inputObj.close();

	}

	private static void isEligibleToVote(int age) {
		if(age<18) {
			System.out.println("Not eligible to vote");
		}else {
			System.out.println("Eligible to vote");

		}
	}


}
