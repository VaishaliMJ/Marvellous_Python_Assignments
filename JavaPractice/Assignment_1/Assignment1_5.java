/*------------------------------------------------------------------------------
                            Assignment1_5
                    (Student name - Vaishali Jorwekar)
------------------------------------------------------------------------------
Problem statement :
            This program outputs number 10 to 1    
------------------------------------------------------------------------------*/
import java.util.Scanner;;
public class Assignment1_5 {

public void printDecreasingNumbers(int number){
    for(int cnt=number;cnt>0;cnt--){
        System.out.print(cnt+"  ");

    }
    System.out.println();
}    
public static void main(String args[]){
    Scanner inputObj=new Scanner(System.in);
    System.out.println("Enter the counter to display numbers:");
    int number = inputObj.nextInt();
    Assignment1_5 printNumObj =new Assignment1_5();
    printNumObj.printDecreasingNumbers(number);
    inputObj.close();

}
    
}
