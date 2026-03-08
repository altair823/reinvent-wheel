package dev.reinvent.wheel.t12;

public final class DiContainerApp {
    public record CliArgs() {
    }

    private DiContainerApp() {
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length != 0) {
            throw new IllegalArgumentException("this template does not accept command-line arguments");
        }
        return new CliArgs();
    }

    public static String helloMessage(CliArgs args) {
        var ignored = args;
        return "hello di\n";
    }

    public static void main(String[] args) {
        System.out.print(helloMessage(parseArgs(args)));
    }
}
