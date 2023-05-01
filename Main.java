import javax.swing.JOptionPane;

public class Main {

    public static void main(String[] args) {
        String name;
        int age;
        String power;
        name = JOptionPane.showInputDialog("What is your heroes name?");
        age = Integer.parseInt("What is your heroes age?");
        power = JOptionPane.showInputDialog("What is your heroes power?");
        JOptionPane.showMessageDialog(null, "Your hero is called" + name);
        JOptionPane.showMessageDialog(null, "Your hero is " + age + " years old");
        JOptionPane.showMessageDialog(null,"Your heroes power is" + power);

    }
}
