package za.org.capaciti;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Press 1 to start adding grades and 0 to exit");

        boolean in = true;

        while (in == true) {
            Scanner scan2 = new Scanner(System.in);
            int input2 = scan2.nextInt();

            if (input2 != 1) {
                in = false;
            } else {
                Scanner scan1 = new Scanner(System.in);
                System.out.println("Input grade:");
//                int grade = scan1.nextInt();
//                if (grade > 80) {
//                    System.out.println("A");
//                } else if (grade > 60 && grade <= 80) {
//                    System.out.println("B");
//                } else if (grade > 50 && grade <= 60) {
//                    System.out.println("C");
//                } else if (grade > 45 && grade <= 50) {
//                    System.out.println("D");
//                } else if (grade > 25 && grade <= 45) {
//                    System.out.println("E");
//                } else if (grade <= 25) {
//                    System.out.println("F");
//                } else {
//                    System.out.println("Invalid grade.");
//                }
                int grade = scan1.nextInt();
                switch (grade) {
                    case 80: case 81: case 82: // and so on till 100
                        System.out.println("A");
                        break;
                    case 79: case 78: // and so on till 61
                        System.out.println("B");
                        break;
                    case 60: case 59: // and so on till 51
                        System.out.println("C");
                        break;
                    case 50: case 49: // and so on till 46
                        System.out.println("D");
                        break;
                    case 45: case 44: // and so on till 26
                        System.out.println("E");
                        break;
                    default:
                        System.out.println("F");
                        break;
                }

                System.out.println("Please 1 to add another grade or 0 to exit");
            }
        }
    }
}