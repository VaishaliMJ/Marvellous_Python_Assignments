/*--------------------------------------------------------------------------------------
                            Assignment1_3 
                    (Student name - Vaishali Jorwekar)
----------------------------------------------------------------------------------------
Problem statement :
                This program accepts two numbers from user and pass these numbers as 
                parameters to the function named Add(num1 , num2) and returns result 
                of addition 
-----------------------------------------------------------------------------------------*/
import java.util.Scanner;
public class Assignment1_3 {
    
    public int Addition(int num1,int num2){
        return num1+num2;
    }
    public static void main(String args[]){
        Scanner scanObj=new Scanner(System.in);
        System.out.println("Enter the first number:");
        int number1=scanObj.nextInt();

        System.out.println("Enter the second number:");
        int number2=scanObj.nextInt();

        Assignment1_3 addObj=new Assignment1_3();
        int result=addObj.Addition(number1, number2);
        System.out.println("Result of addition is :"+result);

        scanObj.close();

    }
}
