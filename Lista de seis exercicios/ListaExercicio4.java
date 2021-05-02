import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe um valor real");
	    String n1 = sc.nextLine();
	    float valor;
	    if (n1.contains(",")){
	        n1 = n1.replace(",",".");
	    }
	    valor = Float.parseFloat(n1);
	    double acrescido = valor + (valor * (15.8/100));
	    System.out.println("O valor informado é "+n1);
	    System.out.println("Acrescentando 15,8% é igual a  "+acrescido);
		
	}
}
