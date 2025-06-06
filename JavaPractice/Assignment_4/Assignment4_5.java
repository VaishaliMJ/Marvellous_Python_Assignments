import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*-------------------------------------------------------------------------------------------
                          Assignment4_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Number list contains only Prime number
                   Map : Multiply each number by 2
                   Reduce : Maximum of all numbers from the list
------------------------------------------------------------------------------------------*/

public class Assignment4_5{

	/*----------------------------------------------------------------------------------
	#  This function checks if the given number is prime or not
	#----------------------------------------------------------------------------------*/
	public static boolean ChkPrime(int number) {
	    if(number<=1)
	        return false;
	    for (int num=2;num<number;num++) {
	         if (number % num == 0)
	                return false;
	    }
	    return true;  
	} 		
	public static void main(String[] args) {

		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);
		//all 3 Steps in 1
		/*		Optional<Integer> result=numberList.stream()
						.filter(Assignment4_5::ChkPrime)
						.map(n->n*2)
						.reduce((a,b)->a>b? a : b);
				System.out.println(result);*/


		
		// Filtered list FOR PRIME numbers only		
		List<Integer> primeNumberList=numberList.stream()
							.filter(Assignment4_5::ChkPrime)
							.collect(Collectors.toList());


		System.out.println("Filtered list of PRIME numbers only):"+primeNumberList);

		//Mapped data(Multiply number by 2)
		List<Integer> doubledNums=primeNumberList.stream()
							.map(n->n*2)
							.collect(Collectors.toList());
		
		System.out.println("Mapped data(Square Numbers): "+doubledNums);
		
		//Reduced data(Maximum of list numbers)
		int maxNum=doubledNums.stream().reduce(0,(a,b)->a>b?a:b);
		System.out.println("Reduced data(Maximum of list numbers) : "+maxNum);
		 
	
	}
	

}
