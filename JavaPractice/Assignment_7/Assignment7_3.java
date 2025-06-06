import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/*-----------------------------------------------------------------------------
                          Assignment7_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement :  Accept list of integers from user and use filter() function to 
                   keep only even numbers
----------------------------------------------------------------------------------------*/

public class Assignment7_3 {

	public static void main(String[] args) {
		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);


		//Filter Even numbers only
		List<Integer> evenNumbers=numberList.stream()
				.filter(i->i%2==0)
				.collect(Collectors.toList());

		System.out.println("Filtered EVEN numbers only : "+evenNumbers);

	}

}
