/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;
public class Pilha
{
	public static void main(String[] args) {
		String[] identificador = new String[10];
	    String[] alturas = new String[10];
	    String[] larguras = new String[10];
	    String[] profundidades = new String[10];
	    String[] tipos = new String[10];
	    int tm = 0;
	    Scanner sc = new Scanner(System.in);
	    int op;
	    do {
	    System.out.println("Bem vindo, o que deseja fazer?");
		System.out.println("1 - Incluir Caixa");
		System.out.println("2 - Retirar Caixa");
		System.out.println("3 - Sair");
		op = sc.nextInt();
		switch(op){
		    case 1:
		        System.out.println("Informe a identificação da caixa.");
		        String x = sc.nextLine();
		        String identificacao = sc.nextLine();
		        identificador[tm] = identificacao;
		        System.out.println("Informe a altura da caixa");
		        String altura = sc.nextLine();
		        alturas[tm] = altura;
		        System.out.println("Informe a largura da caixa");
		        String largura = sc.nextLine();
		        larguras[tm] = largura;
		        System.out.println("Informe a profundidade da caixa");
		        String profundidade = sc.nextLine();
		        profundidades[tm] = profundidade;
		        System.out.println("Informe se a caixa é fragil");
		        String tipo = sc.nextLine();
		        tipos[tm] = tipo;
		        tm = tm+1;
		        break;
		   case 2:
		       System.out.println("======================================================");
		        System.out.println("A caixa retirada é "+identificador[tm-1]+" do tipo "+tipos[tm-1]+".");
		        System.out.println("A altura é "+alturas[tm-1]+", a largura é "+larguras[tm-1]);
		        System.out.println("e a profundidade é "+profundidades[tm-1]);
		        System.out.println("======================================================");
		        identificador[tm] = null;
		        alturas[tm] = null;
		        larguras[tm] = null;
		        profundidades[tm] = null;
		        tipos[tm] = null;
		        tm = tm -1;
		}
		System.out.println("Caixas na pilha");
		System.out.println("======================================================");
		int tam = tm;
		for (int i=0;i<tam;i++){
		            System.out.println((i+1)+" - "+identificador[i]);
		}
		System.out.println("======================================================");
	    } 
	    while(op != 3);
	}
}
