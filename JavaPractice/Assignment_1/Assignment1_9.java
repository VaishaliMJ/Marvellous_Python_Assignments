/*-----------------------------------------------------------------------------------------
                            Assignment1_9
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
            This program displays first 10 even numbers on the screen
--------------------------------------------------------------------------------------*/

public class Assignment1_9 {
public static void main(String[] args) {
    int numCount=0;
    for(int cnt=1;cnt<22;cnt++){
        if(cnt%2==0){
            System.out.print(cnt+"  ");
            numCount++;
        }
        if(numCount==10)
            break;
    
    }
    System.out.println();
}
    
}
