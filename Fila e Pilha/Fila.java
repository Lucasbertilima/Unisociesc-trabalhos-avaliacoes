/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

import java.util.Scanner;
public class Fila
{
	public static void main(String[] args) {
	    String[] nomes = new String[20];
	    String[] idades = new String[20];
	    String[] descricoes = new String[20];
	    int tm = 0;
	    int op = 0;
	    Scanner sc = new Scanner(System.in);
	    do {
		System.out.println("Bem vindo, o que deseja fazer?");
		System.out.println("1 - Incluir Paciente");
		System.out.println("2 - Atender Paciente");
		System.out.println("3 - Atender Paciente especifico");
		System.out.println("4 - Sair");
		op = sc.nextInt();
		switch(op){
		    case 1:
		        System.out.println("Informe o nome do paciente.");
		        String x = sc.nextLine();
		        String nome = sc.nextLine();
		        nomes[tm] = nome;
		        System.out.println("Informe a idade do paciente");
		        String idade = sc.nextLine();
		        idades[tm] = idade;
		        System.out.println("Informe a descrição do atendimento");
		        String desc = sc.nextLine();
		        descricoes[tm] = desc;
		        tm = tm+1;
		        break;
		    case 2:
		        System.out.println("======================================================");
		        System.out.println("O paciente atendido é "+nomes[0]+" de "+idades[0]+" anos.");
		        System.out.println("O tipo de atendimento é "+descricoes[0]);
		        System.out.println("======================================================");
		        nomes = opcao2(nomes);
		        idades = opcao2(idades);
		        descricoes = opcao2(descricoes);
		        tm = tm-1;
		        break;
		    case 3:
		        System.out.println("======================================================");
		        int tam = tm;
		        for (int i=0;i<tam;i++){
		            System.out.println((i+1)+" - "+nomes[i]);
		        }
		        System.out.println("Qual o número do paciente a ser atendido?");
		        int numpaciente = (sc.nextInt() - 1);
		        System.out.println("======================================================");
		        System.out.println("O paciente atendido é "+nomes[numpaciente]+" de "+idades[numpaciente]+" anos.");
		        System.out.println("O tipo de atendimento é "+descricoes[numpaciente]);
		        System.out.println("======================================================");
		        nomes = opcao3(nomes, numpaciente);
		        idades = opcao3(idades, numpaciente);
		        descricoes = opcao3(descricoes, numpaciente);
		        tm = tm-1;
		        break;
		}
		int tam = tm;
		System.out.println("Pessoas na fila");
		System.out.println("======================================================");
		for (int i=0;i<tam;i++){
		            System.out.println((i+1)+" - "+nomes[i]);
		}
		System.out.println("======================================================");
	    }
	    while (op != 4);
	}
	static String[] opcao2(String[] array){
	    String[] arrayaux = new String[20];
	    int npos = 0;
	    for (int i=1;i<20;i++){
	        arrayaux[npos] = array[i];
	        npos = npos+1;
	    }
	    String[] changedarray = arrayaux;
	    return changedarray;
	}
	static String[] opcao3(String[] array, int index){
	    array[index] = null;
	    String[] arrayaux = new String[20];
	    int npos = 0;
	    for (int i=0;i<20;i++){
	        if (array[i] != null){
	            arrayaux[npos] = array[i];
	            npos = npos+1;}
	    }
	    String[] changedarray = arrayaux;
	    return changedarray;
	}
}