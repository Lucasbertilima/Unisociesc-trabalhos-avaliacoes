import java.util.Scanner; 
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe um número");
	    int n1 = sc.nextInt();
	    System.out.println("Informe um segundo número");
	    int n2 = sc.nextInt();
	    System.out.println("Informe um terceiro número");
	    int n3 = sc.nextInt();
	    System.out.println("V1="+n1+" V2="+n2+" V3="+n3);
		System.out.println("V1 + V2 = "+(n1+n2));
		System.out.println("V2 - V1 = "+(n2-n1));
		System.out.println("V3 * V1 = "+(n3*n1));
		System.out.println("V3 + V2 = "+(n3+n2));
		System.out.println("V3 - V2 = "+(n3-n2));
		System.out.println("V1 + V2 + V3 = "+(n1+n2+n3));
		
	}
}
