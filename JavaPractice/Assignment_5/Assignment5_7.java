import java.util.Scanner;
/*-------------------------------------------------------------------------------------------
                          Assignment 5_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts length and width from the user and 
                    calculates area and perimeter of a rectangle
----------------------------------------------------------------------------------*/

public class Assignment5_7 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter rectangle length:"); 
		int len=inputObj.nextInt();
		System.out.print("Enter rectangle width:"); 
		int width=inputObj.nextInt();
		calculateAreaAndPerimeter(len,width);
		inputObj.close();

	}	
	//-----------------------------------------------------------------------------------
	//This function calculates area and perimeter of a rectangle
	//-----------------------------------------------------------------------------------
	public static void  calculateAreaAndPerimeter(int length,int width) {  
		System.out.println("------------------------------------------------------");
	    float area = length * width;
	    float perimeter = 2*(length + width);
	    System.out.println("Area of rectangle :"+area);
	    System.out.println("Perimeter of rectangle:"+perimeter);
	    System.out.println("------------------------------------------------------");
	}
}
