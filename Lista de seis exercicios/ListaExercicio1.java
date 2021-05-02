import java.util.Scanner; 
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe um número");
	    int n1 = sc.nextInt();
	    System.out.println("Informe um segundo número");
	    int n2 = sc.nextInt();
		System.out.println("A soma de "+n1+" + "+n2+" é igual a "+(n1+n2));
		System.out.println("A subtração de "+n1+" - "+n2+" é igual a "+(n1-n2));
		System.out.println("A divisão de "+n1+" / "+n2+" é igual a "+(n1/n2));
		System.out.println("A multiplicação de "+n1+" * "+n2+" é igual a "+(n1*n2));
		
	}
}
