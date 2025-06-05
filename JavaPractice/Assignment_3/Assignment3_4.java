/*-------------------------------------------------------------------------------------------
                          Assignment3_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets N elements from the user and 
                    store it into a list
                    2. It also accepts another number to 
                    be searched in the list and find its frequency in the list
------------------------------------------------------------------------------------------*/


import java.util.ArrayList;
import java.util.Scanner;




public class Assignment3_4 {
	
	public static void main(String args[]) {
		
		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		Scanner inputObj=new Scanner(System.in);
		int searchNum=inputObj.nextInt();
		inputObj.close();
		findNumberAndFrequency(numberList,searchNum);
		

	
}

	private static void findNumberAndFrequency(ArrayList<Integer> numberList,int searchNum) {
		int numCount=0;
		for(int cnt=0;cnt<numberList.size();cnt++) {
			int element=numberList.get(cnt);
			if(searchNum==element) {
				
				numCount++;
			}
		}	
		System.out.println(searchNum+" Frequency is :"+numCount);
	}

}
