/*-----------------------------------------------------------------------------------------
                            Assignment1_6
                    (Student name - Vaishali Jorwekar)
-----------------------------------------------------------------------------------------
Problem statement :This program accepts number from user and 
                   checks if given number is positive or negative or Zero       
-----------------------------------------------------------------------------------------*/
import java.util.Scanner;
public class Assignment1_6 {
    public static void checkPositiveNegativeZero(int number){
        if(number>0)
            System.out.println(number+" number is POSITIVE");
        else if (number<0)
            System.out.println(number+" number is NEGATIVE");
        else
            System.out.println(number+ " number is ZERO");    
    }

    public static void main(String[] args) {
        Scanner scanObj = new Scanner(System.in);
        System.out.println("Enter the number:");
        int number=scanObj.nextInt();
        checkPositiveNegativeZero(number);


        scanObj.close();
    }
    
}
