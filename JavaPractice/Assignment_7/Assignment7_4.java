import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/*-----------------------------------------------------------------------------
                          Assignment7_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement :  Accept list of integers from user and use reduce() function to 
                   find product of all numbers
----------------------------------------------------------------------------------------*/

public class Assignment7_4 {

	public static void main(String[] args) {
		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);


		//find product of all numbers
		int productNums=numberList.stream()
				.reduce(1,(a,b)->(a*b));
				

		System.out.println("Product of all numbers : "+productNums);

	}

}
