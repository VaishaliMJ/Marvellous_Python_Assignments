/*-------------------------------------------------------------------------------------------
                          Assignment3_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets N elements from the user and 
                    store it into a list
                    2. It finds prime number from the list
                    3. Returns addition of all prime numbers
------------------------------------------------------------------------------------------*/


import java.util.ArrayList;
import java.util.Scanner;




public class Assignment3_5 {

	public static void main(String args[]) {

		ArrayList<Integer> numberList=Module.acceptNumbers();
		System.out.println("List Elements are:"+numberList);

		sumPrimeNumbers(numberList);



	}

	public static boolean checkPrime(int number) {
		boolean isPrime=true;
		if(number<=1) {
			isPrime= false;
		}
		for(int cnt=2;cnt<number;cnt++) {
			if(number%cnt==0) {
				isPrime= false;
				break;
			}
		}
		return isPrime;
	}


	
	private static void sumPrimeNumbers(ArrayList<Integer> numberList) {
		int sumPrime=0;
		StringBuffer primeList=new StringBuffer();
		for(int cnt=0;cnt<(numberList.size());cnt++) {
			int number=numberList.get(cnt);
			if(checkPrime(number)) {
				primeList.append(number);
				primeList.append(" ");
				sumPrime=sumPrime+number;
			}
		}	
		System.out.println("Sum of "+primeList+" Prime Numbers is :"+sumPrime);
	}

}
