import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*-------------------------------------------------------------------------------------------
                          Assignment4_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers accepted from user 
                   Filter : Numbers should be 70 < = Number list <= 90 
                   Map : Increase numbers in list by 10
                   Reduce : Product of all numbers from the list

------------------------------------------------------------------------------------------*/

public class Assignment4_3{


	public static void main(String[] args) {

		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		// all 3 Steps in 1
		//		int result=numberList.stream()
		//				.filter(a-> a >= 70 && a<=90)
		//				.map(n->n+10)
		//				.reduce(1,(a,b)->a*b);
		//		System.out.println(result);


		
		// Filtered list of number with criteria (70<=number<=90)		
		List<Integer> numsInRange=numberList.stream()
							.filter(a-> a >= 70 && a<=90)
							.collect(Collectors.toList());


		System.out.println("Filtered list of number with criteria (70<=number<=90):"+numsInRange);

		//Mapped data(Increased by 10)
		List<Integer> addBy10=numsInRange.stream()
							.map(i->i+10)
							.collect(Collectors.toList());
		
		System.out.println("Mapped data(Increased by 10) : "+addBy10);
		
		//Reduced data(Multiplication of list numbers)
		int resultMultiply=addBy10.stream().reduce(1, (a,b)->a*b);
		System.out.println("Reduced data(Multiplication of list numbers) : "+resultMultiply);


	}


}
