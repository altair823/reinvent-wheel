package dev.reinvent.wheel.t17

import kotlin.test.Test

class DslConfigParserAppTest {
    @Test
    fun minimalTemplateCompilesAndRuns() {
        kotlin.test.assertEquals("hello dsl\n", DslConfigParserApp.helloMessage(DslConfigParserApp.CliArgs("../fixtures/sample.dsl")))
    }
}
