import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe o nome do funcionario");
	    String nom = sc.nextLine();
	    System.out.println("Informe quantidade de horas trabalhadas");
	    int horas = sc.nextInt();
	    System.out.println("Informe quantidade de dependentes do funcionario");
	    int dep = sc.nextInt();
	    double salh = 32 * horas;
	    double sald = 40 * dep;
	    double valbruto = salh + sald;
	    double inss = valbruto * 0.085;
	    double ir = valbruto * 0.05;
	    double valliquido = valbruto - inss - ir;
		System.out.println("O salário bruto do funcionario "+nom+" vai ser "+valbruto);
		System.out.println("O valor do INSS vai ser "+inss);
		System.out.println("O valor do imposto de renda vai ser "+ir);
		System.out.println("O salário liquido do funcionario vai ser "+valliquido);
	}
}
