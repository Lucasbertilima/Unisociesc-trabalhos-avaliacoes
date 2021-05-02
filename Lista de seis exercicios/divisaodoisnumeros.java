import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe um número");
	    float n1 = sc.nextFloat();
	    System.out.println("Informe o segundo número");
	    float n2 = sc.nextFloat();
	    double res = n1 / n2;
	    System.out.println("O resultado da divisão de "+n1+" e "+n2+" é "+res);
	}
}
