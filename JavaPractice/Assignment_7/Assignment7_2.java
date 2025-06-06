import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/*-----------------------------------------------------------------------------
                          Assignment7_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept list of integers from user and use map() function to
                    double each value
----------------------------------------------------------------------------------------*/

public class Assignment7_2 {

	public static void main(String[] args) {
		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);


		//Mapped data(Double numbers)
		List<Integer> doubleNums=numberList.stream()
				.map(i->i*2)
				.collect(Collectors.toList());

		System.out.println("Mapped data(Double numbers) : "+doubleNums);

	}

}
