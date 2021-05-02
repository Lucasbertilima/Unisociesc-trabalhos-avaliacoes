import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe um número");
	    int n1 = sc.nextInt();
	    System.out.println("Informe o segundo número");
	    int n2 = sc.nextInt();
	    double res = n1 * n2;
	    System.out.println("O resultado da multiplicação de "+n1+" e "+n2+" é "+res);
	}
}
