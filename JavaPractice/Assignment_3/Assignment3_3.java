/* -------------------------------------------------------------------------------------------
                          Assignment3_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts N elements from the user and 
                    store it into a list and returns the Minimum number 
                    from the list
-----------------------------------------------------------------------------------------  */


import java.util.ArrayList;


public class Assignment3_3 {
	
	public static void main(String args[]) {
		
		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		findMinimumNumber(numberList);
		

	
}

	private static void findMinimumNumber(ArrayList<Integer> numberList) {
		int minNumber=numberList.get(0);
		for(int cnt=0;cnt<numberList.size();cnt++) {
			int element=numberList.get(cnt);
			if(minNumber>element) {
				
				minNumber=element;
			}
		}	
		System.out.println("Minimum element is :"+minNumber);
	}

}
