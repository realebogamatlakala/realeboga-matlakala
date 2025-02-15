import java.util.Scanner;

public class FibonacciIterative {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get user input
        System.out.print("Enter the number of Fibonacci terms: ");
        int n = scanner.nextInt();

        // Print Fibonacci sequence
        System.out.println("Fibonacci Sequence:");
        fibonacciIterative(n);

        scanner.close();
    }

    public static void fibonacciIterative(int n) {
        int first = 0, second = 1;
        System.out.print(first + " " + second);

        for (int i = 2; i < n; i++) {
            int next = first + second;
            System.out.print(" " + next);
            first = second;
            second = next;
        }
        System.out.println();
    }
}
