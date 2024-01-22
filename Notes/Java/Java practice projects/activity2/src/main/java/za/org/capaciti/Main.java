package za.org.capaciti;


import za.org.capaciti.domain.CountedItem;
import za.org.capaciti.domain.PurchaseItem;
import za.org.capaciti.domain.WeighedItem;

public class Main {
    public static void main(String[] args) {
        PurchaseItem item1 = new WeighedItem("Apple", 50.0, 2.5);
        item1.display();

        PurchaseItem item2 = new CountedItem("Pens", 5.0, 20);
        item2.display();
    }
}