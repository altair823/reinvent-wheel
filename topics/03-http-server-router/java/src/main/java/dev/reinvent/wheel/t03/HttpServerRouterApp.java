package dev.reinvent.wheel.t03;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public final class HttpServerRouterApp {
    public record CliArgs(int port) {
    }

    private HttpServerRouterApp() {
    }

    private static int parseInt(String value, String label) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException ex) {
            throw new IllegalArgumentException(label + " must be an integer: " + value, ex);
        }
    }

    public static CliArgs parseArgs(String[] args) {
        if (args.length > 1) {
            throw new IllegalArgumentException("usage: t03-http-server-router-java [port]");
        }
        int port = args.length > 0 ? parseInt(args[0], "argv[1]") : Integer.parseInt(System.getenv().getOrDefault("PORT", "18080"));
        return new CliArgs(port);
    }

    static HttpServer start(int port) throws IOException {
        var server = HttpServer.create(new InetSocketAddress("127.0.0.1", port), 0);
        server.createContext("/health", exchange -> {
            if (!"GET".equals(exchange.getRequestMethod())) {
                send(exchange, 405, "method-not-allowed\n");
                return;
            }
            send(exchange, 200, "ok\n");
        });
        server.createContext("/echo", exchange -> {
            if (!"POST".equals(exchange.getRequestMethod())) {
                send(exchange, 405, "method-not-allowed\n");
                return;
            }
            send(exchange, 200, new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8));
        });
        server.createContext("/", exchange -> send(exchange, 404, "not-found\n"));
        server.start();
        return server;
    }

    private static void send(HttpExchange exchange, int status, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(status, bytes.length);
        exchange.getResponseBody().write(bytes);
        exchange.close();
    }

    public static void main(String[] args) throws Exception {
        CliArgs cliArgs = parseArgs(args);
        start(cliArgs.port());
        Thread.currentThread().join();
    }
}
