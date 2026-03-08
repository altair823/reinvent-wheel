package dev.reinvent.wheel.t02

import kotlin.test.Test

class KeyValueStoreAppTest {
    @Test
    fun minimalTemplateCompilesAndRuns() {
        kotlin.test.assertEquals("hello kv-store\n", KeyValueStoreApp.helloMessage(KeyValueStoreApp.CliArgs("../fixtures/commands.txt")))
    }
}
