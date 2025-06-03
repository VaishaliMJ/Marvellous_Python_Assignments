/*-------------------------------------------------------------------------
                            Assignment1_2                         
                    (Student name - Vaishali Jorwekar)
-------------------------------------------------------------------------
Problem statement :
               - This program checks if number is even or odd
-------------------------------------------------------------------------*/
import java.util.Scanner;
class Assignment1_2{

    public static void chcekNumber(int number){
        if(number%2==0)
            System.out.println(number+":is EVEN number");
        else
            System.out.println(number+" is ODD Number");

    }
    public static void main(String args[]){
        Scanner scanObj=new Scanner(System.in);
        System.out.print("Enter the number:");
        int number=scanObj.nextInt();
        System.out.println("Entered number is :"+number);
        scanObj.close();
        chcekNumber(number);
        
    }

}
