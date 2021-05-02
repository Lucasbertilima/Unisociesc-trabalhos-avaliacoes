import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe a primeira nota");
	    float n1 = sc.nextFloat();
	    System.out.println("Informe a segunda nota");
	    float n2 = sc.nextFloat();
	    System.out.println("Informe a terceira nota");
	    float n3 = sc.nextFloat();
	    double media = (n1+n2+n3)/3;
	    System.out.println("A média é obtida atraves da soma de "+n1+" + "+n2+" + "+n3+" dividido por 3");
	    System.out.println("Totalizando "+media);
	}
}
