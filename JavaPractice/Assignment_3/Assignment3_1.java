/*-------------------------------------------------------------------------------------------
                          Assignment3_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts N elements from the user and 
                    store it into a list and returns the addition of 
                    elements of the list
-----------------------------------------------------------------*/

import java.util.ArrayList;

public class Assignment3_1 {
	
	public static void main(String args[]) {
		
		
		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		
		
		sumListElements(numberList);
		
		
	}

	private static void sumListElements(ArrayList<Integer> numberList) {
		int sumElements=0;
		for(int cnt=0;cnt<numberList.size();cnt++)
			sumElements=sumElements+numberList.get(cnt);
		
		System.out.println("Sum Of Elements is :"+sumElements);
	}

}
