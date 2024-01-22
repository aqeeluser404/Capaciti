package za.org.capaciti.domain;

public class CountedItem extends PurchaseItem {
    private int quantity;

    public CountedItem(String name, double unitPrice, int quantity) {
        super(name, unitPrice);
        this.quantity = quantity;
    }

//    methods
    @Override
    public double getUnitPrice() {
        return super.getUnitPrice();
    }

    @Override
    public double getPrice() {
        return super.getPrice() * quantity;
    }

    @Override
    public void display() {
        System.out.println(getName() + " @ " + getUnitPrice() + " per unit, " + quantity + " units, Total: R" + getPrice());
    }
}
