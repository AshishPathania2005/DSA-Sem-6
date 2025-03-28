import java.util.Scanner;

public class findElementInArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[10]; // Array of size 10
        int = n;
        // Taking input
        System.out.println("Enter 10 elements:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = scanner.nextInt();
        }

        // Searching for the second occurrence of 4
        int count = 0;

        int index = -1; // To store the index of the second occurrence

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 4) {
                count++;
                if (count == n) { // If it's the second occurrence
                    index = i;
                    break;
                }
            }
        }

        // Output the result
        if (index != -1) {
            System.out.println("The second occurrence of 4 is at index: " + index);
        } else {
            System.out.println("The number 4 does not appear twice in the array.");
        }

        scanner.close();
    }
}
