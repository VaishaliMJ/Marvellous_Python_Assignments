import java.util.Scanner;
/*-----------------------------------------------------------------------------
                          Assignment6_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Print triangle * pattern using nested loop
--------------------------------------------------------------------------------------------*/
public class Assignment6_6 {
	static char STAR='*';
	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter number to print * :"); 
		int number=inputObj.nextInt();
		inputObj.close();
		printStars(number);
		
	}

	private static void printStars(int number) {
		for(int row=0;row<number;row++) {
			for(int col=0;col<=row;col++) {
				System.out.print(STAR+" ");
			}
			System.out.println("\n");
		}


	}

}
