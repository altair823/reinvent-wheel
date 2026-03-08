package dev.reinvent.wheel.t15

import kotlin.test.Test

class CoroutineSchedulerAppTest {
    @Test
    fun minimalTemplateCompilesAndRuns() {
        kotlin.test.assertEquals("hello coroutine\n", CoroutineSchedulerApp.helloMessage(CoroutineSchedulerApp.CliArgs("../fixtures/jobs.txt")))
    }
}
