/*------------------------------------------------------------------------------
                            Assignment1_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------
Problem statement :
            This program displays 5 times "Marvellous" on console   
------------------------------------------------------------------------------*/
import java.util.Scanner;
public class Assignment1_4 {
    public static void main(String args[]){
        Scanner input=new Scanner(System.in);

        System.out.println("Enter how many times you want to print String:");
        int number=input.nextInt();
        for(int cnt=0;cnt<number;cnt++){
            System.out.println("Number ("+cnt+") "+"Marvellous");
        }
        input.close();

    }
}
