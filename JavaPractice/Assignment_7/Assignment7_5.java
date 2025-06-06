import java.util.Scanner;
import java.util.function.Consumer;

/*---------------------------------------------------------------------------------------
                          Assignment7_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program checks if given string is palindrome or not
--------------------------------------------------------------------------------------------------------------*/

public class Assignment7_5 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter String:"); 
		String originalString=inputObj.next();
		StringBuffer reverseString=new StringBuffer();
		for(int cnt=originalString.length()-1;cnt>=0;cnt--) {
			char c=originalString.charAt(cnt);
			reverseString.append(c);
		}
		System.out.println("Reversed String is :"+reverseString.toString());
		if(originalString.equals(reverseString.toString()))
				System.out.println("'"+originalString+"' is a Palindrome");
		else
			System.out.println("'"+originalString+"' is not a Palindrome");

		inputObj.close();
		
	}

}
