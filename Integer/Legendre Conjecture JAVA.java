import java.util.Scanner;

public class LegendreConjecture {

    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        if (num <= 3) return true;
        if (num % 2 == 0 || num % 3 == 0) return false;
        
        for (int i = 5; i <= Math.sqrt(num); i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number: ");
        
        // Check if input is an integer
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter an integer.");
            scanner.close();
            return;
        }
        
        int n = scanner.nextInt();
        scanner.close();
        
        int start = n * n;
        int end = (n + 1) * (n + 1);
        System.out.println("PRIME NUMBERS IN RANGE OF " + start + " and " + end + ":");
        
        boolean found = false;
        for (int i = start; i < end; i++) {
            if (isPrime(i)) {
                System.out.println(i);
                found = true;
            }
        }
        
        if (!found) {
            System.out.println("NONE");
        }
    }
}
