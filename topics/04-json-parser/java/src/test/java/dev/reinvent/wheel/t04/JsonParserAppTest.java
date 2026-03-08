package dev.reinvent.wheel.t04;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class JsonParserAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        assertEquals("hello json\n", JsonParserApp.helloMessage(new JsonParserApp.CliArgs("../fixtures/sample.json")));
    }
}
