package dev.reinvent.wheel.t03;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class HttpServerRouterAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        HttpServerRouterApp.CliArgs args = new HttpServerRouterApp.CliArgs(18081);
assertDoesNotThrow(() -> HttpServerRouterApp.start(args.port()).stop(0));
    }
}
