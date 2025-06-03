/*-----------------------------------------------------------------------------------------
                            Assignment1_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
    This program accepts 'number' from user and checks if given number is divisible by 5   
----------------------------------------------------------------------------------------*/

import java.util.Scanner;

public class Assignment1_7 {
    public static boolean checkDivisibleBy5(int number){
        if(number%5==0)
            return true;
        else 
            return false;    
    }

    public static void main(String[] args) {
        Scanner scanObj = new Scanner(System.in);
        System.out.println("Enter the number:");
        int number=scanObj.nextInt();
        boolean flag=checkDivisibleBy5(number);
        System.out.println(number+"  is divisible by 5  :"+flag);

        scanObj.close();
    }
    
}
