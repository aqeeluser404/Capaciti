package za.org.capaciti;

import za.org.capaciti.domain.Company;
import za.org.capaciti.domain.Product;
import za.org.capaciti.domain.Store;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

//        products
        Product product1 = new Product("Ram 16gbx2 sticks", 50, 799.0);
        Product product2 = new Product("Ryzen 7 2700x 8-core CPU", 100, 499.0);
        ArrayList<Product> productList = new ArrayList<>();
        productList.add(product1);
        productList.add(product2);

//        stores
        Store store1 = new Store("Computer-mania Claremont Branch", "Cavendish", productList);
        ArrayList<Store> storeList = new ArrayList<>();
        storeList.add(store1);

//        companies
        Company company1 = new Company("Computer-mania", storeList);

//        printing everything
        System.out.println(company1);
    }
}