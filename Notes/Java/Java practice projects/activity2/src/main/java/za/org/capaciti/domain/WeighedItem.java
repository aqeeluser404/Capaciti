package za.org.capaciti.domain;

public class WeighedItem extends PurchaseItem {
    private double weight;

    public WeighedItem(String name, double unitPrice, double weight) {
        super(name, unitPrice);
        this.weight = weight;
    }

//    methods
    @Override
    public double getUnitPrice() {
        return super.getUnitPrice();
    }

    @Override
    public double getPrice() {
        return super.getPrice() * weight;
    }

    @Override
    public void display() {
        System.out.println(getName() + " @ " + getUnitPrice() + " per unit, " + weight + " Kg, Total: R" + getPrice());
    }
}
