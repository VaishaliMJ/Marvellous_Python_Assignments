import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.function.Consumer;
import java.util.stream.Collectors;

/*---------------------------------------------------------------------------------------
                          Assignment7_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program checks if given string is palindrome or not
--------------------------------------------------------------------------------------------------------------*/

public class Assignment7_6 {

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


		// Filtered list FOR PRIME numbers only		
		List<Integer> primeNumberList=numberList.stream()
				.filter(Assignment7_6::ChkPrime)
				.collect(Collectors.toList());



		System.out.println("Prime Numbers in the list : "+primeNumberList);

	}

}


