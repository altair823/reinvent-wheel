package dev.reinvent.wheel.t13;

public final class JdbcTodoCliApp {
    public record CliArgs(String input) {
    }

    private JdbcTodoCliApp() {
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length < 1 || args.length > 1) {
            throw new IllegalArgumentException("usage: t13-jdbc-todo-cli-java <input>");
        }
        String input = args[0];
        return new CliArgs(input);
    }

    public static String helloMessage(CliArgs args) {
        var ignored = args;
        return "hello todo\n";
    }

    public static void main(String[] args) {
        System.out.print(helloMessage(parseArgs(args)));
    }
}
