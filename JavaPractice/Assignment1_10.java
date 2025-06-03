/*-----------------------------------------------------------------------------------------
                            Assignment1_10
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
            This program accepts NAME from user and displays it's length            
---------------------------------------------------------------------------------*/
import java.util.Scanner;
public class Assignment1_10 {
    public static void main(String[] args) {
        Scanner scanObj = new Scanner(System.in);
        System.out.println("Enter the name:");
        String name = scanObj.nextLine();
        int nameLen = name.length();
        System.out.println("Length of '"+name+"' is :"+nameLen);
        scanObj.close();
    }
    
}
