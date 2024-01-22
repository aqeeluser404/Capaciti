package za.org.capaciti;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

//        Units to convert from
        System.out.println("Choose the unit you want to convert from: ");
        System.out.println("""
                           1. Feet
                           2. Pounds
                           3. Fahrenheit
                           """);

        int inputUnit = scan.nextInt();

//        Value to convert
        System.out.println("Enter the value to convert: ");
        double inputValue = scan.nextDouble();

//        converter object to convert
        Converter converter = new Converter(inputValue);

        switch (inputUnit) {

            case 1:
                System.out.println("Enter the unit you want to convert to:");
                System.out.println("1. Meters");

                double outputUnitFeet = scan.nextDouble();
                if (outputUnitFeet == 1) {
                    double result = converter.feetToMeters();
                    System.out.println("Result: " + result + " meters");
                } else {
                    System.out.println("Invalid output unit selection for feet conversion");
                }
                break;

            case 2:
                System.out.println("Enter the unit you want to convert to:");
                System.out.println("1. Kilograms");

                double outputUnitPounds = scan.nextDouble();
                if (outputUnitPounds == 1) {
                    double result = converter.poundsToKgs();
                    System.out.println("Result: " + result + " kilograms");
                } else {
                    System.out.println("Invalid output unit selection for pounds conversion");
                }
                break;

            case 3:
                System.out.println("Enter the unit you want to convert to:");
                System.out.println("1. Celsius");

                double outputUnitFahrenheit = scan.nextDouble();
                if (outputUnitFahrenheit == 1) {
                    double result = converter.fahrenheitToCelsuis();
                    System.out.println("Result: " + result + " Celsius");
                } else {
                    System.out.println("Invalid output unit selection for Fahrenheit conversion");
                }
                break;

            default:
                System.out.println("Invalid input unit selection");
                break;
        }
    }
}


