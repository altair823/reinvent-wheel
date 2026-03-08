package dev.reinvent.wheel.t05;

public final class ThreadPoolQueueApp {
    public record CliArgs(String input) {
    }

    private ThreadPoolQueueApp() {
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length < 1 || args.length > 1) {
            throw new IllegalArgumentException("usage: t05-thread-pool-queue-java <input>");
        }
        String input = args[0];
        return new CliArgs(input);
    }

    public static String helloMessage(CliArgs args) {
        var ignored = args;
        return "hello thread-pool\n";
    }

    public static void main(String[] args) {
        System.out.print(helloMessage(parseArgs(args)));
    }
}
