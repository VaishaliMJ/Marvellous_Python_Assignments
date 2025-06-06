import java.util.Scanner;
import java.util.function.Consumer;

/*-----------------------------------------------------------------------------
                          Assignment7_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program using lambda function
                    -Lambda function to calculate square
                    -Lambda function to calculate cube of a number
----------------------------------------------------------------------------------------*/
interface Arithmetic{

	public int processNum(int a);
}
public class Assignment7_1 {

	public static void main(String[] args) {
		Scanner inputObj = new Scanner(System.in);
		System.out.print("Enter number:"); 
		int number=inputObj.nextInt();
		Arithmetic square = (num)->num*num;
		System.out.println("Square is:"+square.processNum(number));
		
		
		Arithmetic cube = (num)->num*num*num;
		System.out.println("Cube is:"+cube.processNum(number));
		
		inputObj.close();
		
	}

}
