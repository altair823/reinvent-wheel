package dev.reinvent.wheel.t05;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class ThreadPoolQueueAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        assertEquals("hello thread-pool\n", ThreadPoolQueueApp.helloMessage(new ThreadPoolQueueApp.CliArgs("../fixtures/tasks.txt")));
    }
}
