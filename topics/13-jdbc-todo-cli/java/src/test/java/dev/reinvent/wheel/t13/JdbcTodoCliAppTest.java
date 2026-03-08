package dev.reinvent.wheel.t13;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

final class JdbcTodoCliAppTest {
    @Test
    void minimalTemplateCompilesAndRuns() {
        assertEquals("hello todo\n", JdbcTodoCliApp.helloMessage(new JdbcTodoCliApp.CliArgs("../fixtures/todos.txt")));
    }
}
