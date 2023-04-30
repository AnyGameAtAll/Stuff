import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String name;
        int age;
        String power;
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your heroes name?");
        name = scanner.next();
        System.out.println("What is your heroes age?");
        age = scanner.nextInt();
        System.out.println("What is your heroes power?");
        power = scanner.next();
        Hero hero1 = new Hero(name, age, power);
        System.out.println(hero1.name);
        System.out.println(hero1.age);
        System.out.println(hero1.power);
    }
}
