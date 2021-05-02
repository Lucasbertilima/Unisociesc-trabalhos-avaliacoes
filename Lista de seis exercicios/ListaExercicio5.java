import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe a base do triangulo");
	    int bas = sc.nextInt();
	    System.out.println("Informe a altura do triangulo");
	    int alt = sc.nextInt();
	    double area = (bas * alt)/2;
	    System.out.println("A Area do triangulo com base "+bas+" e altura "+alt+" é "+area);
		
	}
}
