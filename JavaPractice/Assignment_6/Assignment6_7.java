import java.util.Scanner;
/*-----------------------------------------------------------------------------
                          Assignment6_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept 5 numbers from user and print largest number
----------------------------------------------------------------------------------------*/
public class Assignment6_7 {
	static char STAR='*';
	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter first number :"); 
		int num1=inputObj.nextInt();
		System.out.print("Enter second number :"); 
		int num2=inputObj.nextInt();
		System.out.print("Enter third number :"); 
		int num3=inputObj.nextInt();
		System.out.print("Enter fourth number :"); 
		int num4=inputObj.nextInt();
		System.out.print("Enter fifth number :"); 
		int num5=inputObj.nextInt();
		
		inputObj.close();
		findMaximum(num1,num2,num3,num4,num5);
		
	}

	private static void findMaximum(int num1,int num2,int num3,int num4,int num5) {
		int max=num1;
		if(max<num1) {
			max=num1;
		}
		if(max<num2) {
			max=num2;
		}		
		if(max<num3) {
			max=num3;
		}	
		if(max<num4)
			max=num4;
		if(max<num5)
			max=num5;
			
	    System.out.println("Maximum number is :"+max);                             

	}

}
