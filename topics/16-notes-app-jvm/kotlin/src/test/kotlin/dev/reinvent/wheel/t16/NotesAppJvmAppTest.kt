package dev.reinvent.wheel.t16

import kotlin.test.Test

class NotesAppJvmAppTest {
    @Test
    fun minimalTemplateCompilesAndRuns() {
        kotlin.test.assertEquals("hello notes\n", NotesAppJvmApp.helloMessage(NotesAppJvmApp.CliArgs("../fixtures/notes.txt")))
    }
}
