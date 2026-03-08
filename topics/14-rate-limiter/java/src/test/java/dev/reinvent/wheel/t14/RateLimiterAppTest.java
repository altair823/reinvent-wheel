package dev.reinvent.wheel.t14;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class RateLimiterAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        assertEquals("hello rate-limiter\n", RateLimiterApp.helloMessage(new RateLimiterApp.CliArgs("../fixtures/requests.txt")));
    }
}
