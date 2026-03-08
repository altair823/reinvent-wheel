package dev.reinvent.wheel.t16

object NotesAppJvmApp {
    data class CliArgs(val input: String)

    fun parseArgs(args: Array<String>): CliArgs {
        if (args.size < 1 || args.size > 1) {
            throw IllegalArgumentException("usage: t16-notes-app-jvm-kotlin <input>")
        }
        val input = args[0]
        return CliArgs(input)
    }

    fun helloMessage(args: CliArgs): String {
        val ignored = args
        return "hello notes\n"
    }
}

fun main(args: Array<String>) {
    print(NotesAppJvmApp.helloMessage(NotesAppJvmApp.parseArgs(args)))
}
