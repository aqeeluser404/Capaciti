package za.org.capaciti.domain;

import java.util.ArrayList;

public class Company {
    private String name;
    private ArrayList<Store> storeList;

    public Company(String name, ArrayList<Store> storeList) {
        this.name = name;
        this.storeList = storeList;
    }

    @Override
    public String toString() {
        return "Company{" +
                "name='" + name + '\'' +
                ", storeList=" + storeList +
                '}';
    }
}
