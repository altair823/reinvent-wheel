package dev.reinvent.wheel.t02;

public final class KeyValueStoreApp {
    public record CliArgs(String input) {
    }

    private KeyValueStoreApp() {
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length < 1 || args.length > 1) {
            throw new IllegalArgumentException("usage: t02-key-value-store-java <input>");
        }
        String input = args[0];
        return new CliArgs(input);
    }

    public static String helloMessage(CliArgs args) {
        var ignored = args;
        return "hello kv-store\n";
    }

    public static void main(String[] args) {
        System.out.print(helloMessage(parseArgs(args)));
    }
}
