package dev.reinvent.wheel.t03

import kotlin.test.Test

class HttpServerRouterAppTest {
    @Test
    fun minimalTemplateCompilesAndRuns() {
        val args = HttpServerRouterApp.CliArgs(18082)
HttpServerRouterApp.start(args.port).stop(0)
kotlin.test.assertTrue(true)
    }
}
