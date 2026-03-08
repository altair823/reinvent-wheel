package dev.reinvent.wheel.t14;

public final class RateLimiterApp {
    public record CliArgs(String input) {
    }

    private RateLimiterApp() {
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length < 1 || args.length > 1) {
            throw new IllegalArgumentException("usage: t14-rate-limiter-java <input>");
        }
        String input = args[0];
        return new CliArgs(input);
    }

    public static String helloMessage(CliArgs args) {
        var ignored = args;
        return "hello rate-limiter\n";
    }

    public static void main(String[] args) {
        System.out.print(helloMessage(parseArgs(args)));
    }
}
