package org.example;

public class Employee {
    private String name;
    private int age;
    private String destination;
    private float salary;

    public Employee(String name) {
        this.name = name;
    }

    public void printEmployee() {
        System.out.println("Employee Details: ");
        System.out.println("~~~~~~~~~~~~~~~~~");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Destination: " + destination);
        System.out.println("Salary: " + salary);
        System.out.println("\n");
    }

    public static void main(String[] args) {
        Employee employee1 = new Employee("Aqeel");
        Employee employee2 = new Employee("Ammaarah");
        Employee employee3 = new Employee("Aarif");

//        object 1
        employee1.age = 23;
        employee1.destination = "Manager";
        employee1.salary = 30000.0f;
//        object 2
        employee2.age = 19;
        employee2.destination = "Student";
        employee2.salary = 15000.0f;
//        object 3
        employee3.age = 16;
        employee3.destination = "High-school";
        employee3.salary = 4500.0f;

//        print the objects
        employee1.printEmployee();
        employee2.printEmployee();
        employee3.printEmployee();
    }
}
