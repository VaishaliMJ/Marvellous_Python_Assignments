/*--------------------------------------------------------------------------------------
                            Assignment1_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
    This program accepts number from user and prints * on the console 
----------------------------------------------------------------------------------------- */
import java.util.Scanner;

public class Assignment1_8 {
    static char STAR='*';
    public static void printStars(int number){
        for(int cnt=0;cnt<number;cnt++)
            System.out.print(STAR+" ");
        System.out.println();    
    }

    public static void main(String[] args) {
      Scanner scanObj = new Scanner(System.in);
      System.out.print("Enter how many * you want to print:"); 
      int number =scanObj.nextInt();
      printStars(number);
      scanObj.close();
    }
    
}
