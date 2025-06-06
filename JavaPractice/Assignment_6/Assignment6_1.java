/*-----------------------------------------------------------------------------
                          Assignment6_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program using while loop to print the numbers from 1 to 50 
----------------------------------------------------------------------------------------*/
public class Assignment6_1 {

	public static void main(String[] args) {
		System.out.println("\n\nPrinting numbers upto 50 ...\n");
		System.out.println("--------------------------------------------------------------------------");
		int count = 1;
		while (count <= 50) {
			if (count%10==0) {
				System.out.println(count+"\n");
			}	
			else    
				System.out.print(count+"\t");
			count+=1;
			//System.out.println();
		}
		System.out.println("--------------------------------------------------------------------------");

	}

}
