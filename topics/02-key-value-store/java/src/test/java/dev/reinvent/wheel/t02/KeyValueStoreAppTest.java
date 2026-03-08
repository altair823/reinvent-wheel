package dev.reinvent.wheel.t02;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class KeyValueStoreAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        assertEquals("hello kv-store\n", KeyValueStoreApp.helloMessage(new KeyValueStoreApp.CliArgs("../fixtures/commands.txt")));
    }
}
