

import java.util.ArrayList;
import java.util.Scanner;

public class Module {

	public static ArrayList<Integer> acceptNumbers(){
		Scanner inputObj=new Scanner(System.in);

		ArrayList<Integer> numberList=new ArrayList<Integer>();

		System.out.println("Enter the number of elements in list:");
		int listSize=inputObj.nextInt();

		System.out.println("Enter "+listSize+" elements of the list:");
		for (int cnt=1;cnt<=listSize;cnt++) {
			System.out.print("\nNumber["+cnt+"]:");
			int number = inputObj.nextInt();
			numberList.add(number);

		}
		inputObj.close();
		return numberList;


	}
	
	
}


