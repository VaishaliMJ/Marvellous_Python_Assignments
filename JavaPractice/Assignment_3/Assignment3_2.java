/* -------------------------------------------------------------------------------------------
                          Assignment3_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts N elements from the user and 
                    store it into a list and returns the maximum number 
                    from the list
-----------------------------------------------------------------------------------------  */


import java.util.ArrayList;


public class Assignment3_2 {

	public static void main(String args[]) {

		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		findMaximumNumber(numberList);



	}

	private static void findMaximumNumber(ArrayList<Integer> numberList) {
		int maxNumber=0;
		for(int cnt=0;cnt<numberList.size();cnt++) {
			int element=numberList.get(cnt);

			if(maxNumber<element) {

				maxNumber=element;
			}
		}
		System.out.println("Maximum element is :"+maxNumber);
	}

}
