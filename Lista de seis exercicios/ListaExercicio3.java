import java.util.Scanner;
import java.util.Calendar;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Informe o ano em que você nasceu");
	    int n1 = sc.nextInt();
	    int year = Calendar.getInstance().get(Calendar.YEAR);
	    System.out.println("A sua idade aproximada é "+(year-n1)+" anos");
		
	}
}
