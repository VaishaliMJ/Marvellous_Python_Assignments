import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*-------------------------------------------------------------------------------------------
                          Assignment4_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers accepted from user 
                   Filter : Number list should be even only
                   Map : Calculate the square of number from list
                   Reduce : Addition of all numbers from the list
------------------------------------------------------------------------------------------*/

public class Assignment4_4{


	public static void main(String[] args) {

		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		//all 3 Steps in 1
//				int result=numberList.stream()
//						.filter(a-> a%2==0)
//						.map(n->n*n)
//						.reduce(0,(a,b)->a+b);
//				System.out.println(result);


		
		// Filtered list of EVEN numbers only		
		List<Integer> evenNumberList=numberList.stream()
							.filter(a-> a%2==0)
							.collect(Collectors.toList());


		System.out.println("Filtered list of EVEN numbers only):"+evenNumberList);

		//Mapped data(Square numbers)
		List<Integer> squaredNums=evenNumberList.stream()
							.map(n->n*n)
							.collect(Collectors.toList());
		
		System.out.println("Mapped data(Square Numbers): "+squaredNums);
		
		//Reduced data(Addition of list numbers)
		int addNums=squaredNums.stream().reduce(0, (a,b)->a+b);
		System.out.println("Reduced data(Addition of list numbers) : "+addNums);
		 

	}
	

}
