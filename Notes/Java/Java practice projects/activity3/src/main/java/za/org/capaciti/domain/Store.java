package za.org.capaciti.domain;

import java.util.ArrayList;

public class Store {
    private String name;
    private String location;
    private ArrayList<Product> productList;

    public Store(String name, String location, ArrayList<Product> productList) {
        this.name = name;
        this.location = location;
        this.productList = productList;
    }

    @Override
    public String toString() {
        return "Store{" +
                "name='" + name + '\'' +
                ", location='" + location + '\'' +
                ", productList=" + productList +
                '}';
    }
}
