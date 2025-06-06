/*-----------------------------------------------------------------------------
                          Assignment6_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to find and print sum of Even numbers between 1 to 100
---------------------------------------------------------------------------------*/
public class Assignment6_2 {

	public static void main(String[] args) {
		int sumEven=0;
		for(int cnt=1;cnt<=100;cnt++) {
			if(cnt%2==0) {
				sumEven+=cnt;
				
			}
			
		}
		System.out.println("------------------------------------------------------");
		System.out.println("\nSum of even numbers between 1 to 100 is :"+sumEven);
		System.out.println("------------------------------------------------------");
	}
	
}
