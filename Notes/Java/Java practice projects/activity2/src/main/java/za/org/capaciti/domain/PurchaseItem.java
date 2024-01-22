package za.org.capaciti.domain;

public class PurchaseItem {
    private String name;
    private double unitPrice;

    public PurchaseItem() {
        this.name = "no item";
        this.unitPrice = 0;
    }

    public PurchaseItem(String name, double unitPrice) {
        this.name = name;
        this.unitPrice = unitPrice;
    }

//    methods
    public String getName() {
        return name;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public double getPrice() {
        return unitPrice;
    }

    public void display() {
        System.out.println("no items to display");
    }
}
