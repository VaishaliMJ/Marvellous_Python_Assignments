import java.util.Scanner;
/*-------------------------------------------------------------------------------------------
                          Assignment 5_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a character from user and checks 
                    if it's a vowel or consonant
--------------------------------------------------------------------------------------------*/

public class Assignment5_2 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter the letter :"); 
		char inputChar=inputObj.next().charAt(0);
		inputChar=Character.toLowerCase(inputChar);
		checkIfVowel(inputChar);
		inputObj.close();

	}

	private static void checkIfVowel(char inputChar) {
		if(inputChar=='a' || inputChar=='e' || inputChar=='i' || inputChar=='o' || inputChar=='u') {
			System.out.println(inputChar+" is a vowel");
		}else {
			System.out.println(inputChar+" is a consonant");

		}
	}


}
