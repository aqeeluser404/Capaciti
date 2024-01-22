package org.example;

import java.util.Scanner;

public class HelloWorld {
    public static void getSum(float a, float b) {
        System.out.println("The sum is " + (a + b));
    }
    public static void getDifference(float a, float b) {
        if (a > b) {
            System.out.println("The difference between your numbers is: " + (a - b));
        } else System.out.println("The difference between your numbers is: " + (b - a));
    }
    public static void getProduct(float a, float b) {
        System.out.println("The product between your numbers is: " + (a * b));
    }
    public static void getAverage(float a, float b) {
        System.out.println("The average between your numbers is: " + (a + b)/2);
    }
    public static void getMaximumAndMin(float a, float b) {
        if (a > b) {
            System.out.println(a + " the maximum and " + b + " is the minimum.");
        } else if (b > a) {
            System.out.println(b + " the maximum and " + a + " is the minimum.");
        } else
            System.out.println(a + " is equal to " + b);
    }
    public static void main(String[] args) {
        float a;
        float b;

        // scanner and user input
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your first number: ");
        a = scanner.nextFloat();

        System.out.println("Enter your second number: ");
        b = scanner.nextFloat();

        scanner.close();

        // calling the methods to calc
        getSum(a, b);
        getDifference(a, b);
        getProduct(a, b);
        getAverage(a, b);
        getMaximumAndMin(a, b);
    }
}
