
import java.util.Scanner;
public class Assignment2_1 {

    public void performArithmaticOperations(int number1,int number2){
        System.out.println(
            "\nPerforming following arithmatic operations on "+number1+ "and"+number2+
            ":\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n");
        int answer = 0;
        
        answer =  AssignmentModule.Addition(number1,number2);
        System.out.println("Addition is :"+answer);  
        
		
		  answer = AssignmentModule.Subtraction(number1,number2);
		  System.out.println("Subtraction is :"+answer);
		  
		  answer = AssignmentModule.Multiply(number1,number2);
		  System.out.println("Multiplication is :"+answer);
		  
		  
		  float divAnswer = AssignmentModule.Division(number1,number2);
		  System.out.println("Division is :"+divAnswer);
		 

    }

    public static void main(String[] args) {
        Scanner inputObj = new Scanner(System.in);
        System.out.print("Enter First Number:"); 
        int number1 = inputObj.nextInt();
        System.out.print("Enter Second Number:"); 
        int number2 = inputObj.nextInt(); 
        Assignment2_1 arithmaticObj = new Assignment2_1();
       
        arithmaticObj.performArithmaticOperations(number1,number2);
        
        

          

        inputObj.close();
    }
    
}
