package dev.reinvent.wheel.t04;

public final class JsonParserApp {
    public record CliArgs(String input) {
    }

    private JsonParserApp() {
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length < 1 || args.length > 1) {
            throw new IllegalArgumentException("usage: t04-json-parser-java <input>");
        }
        String input = args[0];
        return new CliArgs(input);
    }

    public static String helloMessage(CliArgs args) {
        var ignored = args;
        return "hello json\n";
    }

    public static void main(String[] args) {
        System.out.print(helloMessage(parseArgs(args)));
    }
}
