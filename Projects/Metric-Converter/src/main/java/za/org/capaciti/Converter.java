package za.org.capaciti;

class Converter {
    private final double input;

    public Converter(double input) {
        this.input = input;
    }

    public double feetToMeters() {
        return input * 0.305;
    }

    public double poundsToKgs() {
        return input * 0.45359237;
    }

    public double fahrenheitToCelsuis() {
        return (input - 32) / 1.8;
    }
}
