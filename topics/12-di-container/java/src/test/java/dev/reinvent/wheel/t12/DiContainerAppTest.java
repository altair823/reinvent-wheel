package dev.reinvent.wheel.t12;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class DiContainerAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        assertEquals("hello di\n", DiContainerApp.helloMessage(new DiContainerApp.CliArgs()));
    }
}
