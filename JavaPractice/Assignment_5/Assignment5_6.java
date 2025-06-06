import java.util.Scanner;
/*-------------------------------------------------------------------------------------------
                          Assignment 5_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts temperature in 
                    Celsius and converts it into Farenheit
-------------------------------------------------------------------------------------*/

public class Assignment5_6 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter temperature in Celcius :"); 
		int tempInCelcius=inputObj.nextInt();
	    float tempInFarenheit = ((tempInCelcius*9)/5)+32;

		
		System.out.println(tempInCelcius + "°C Temperature in Farenheit is : "+tempInFarenheit+"°F");

		inputObj.close();

	}


}
