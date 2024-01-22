package org.example;

public class Person {
    private int id;
    private String firstName;
    private String lastFirst;
    private int age;

    public Person(int id, String firstName, String lastFirst, int age) {
        this.id = id;
        this.firstName = firstName;
        this.lastFirst = lastFirst;
        this.age = age;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastFirst() {
        return lastFirst;
    }

    public void setLastFirst(String lastFirst) {
        this.lastFirst = lastFirst;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "person{" +
                "id=" + id +
                ", firstName='" + firstName + '\'' +
                ", lastFirst='" + lastFirst + '\'' +
                ", age=" + age +
                '}';
    }

    public static void main(String[] args) {
        Person user1 = new Person(1, "Aqeel", "Hanslo", 23);

        System.out.println("Hi my name is " + user1.getFirstName() + " and I am " + user1.getAge() + " years old!");
        user1.setAge(30);
        System.out.println("Hi my name is " + user1.getFirstName() + " and I am " + user1.getAge() + " years old!");
        System.out.println(user1);
    }
}
