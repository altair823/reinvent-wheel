package dev.reinvent.wheel.t17

object DslConfigParserApp {
    data class CliArgs(val input: String)

    fun parseArgs(args: Array<String>): CliArgs {
        if (args.size < 1 || args.size > 1) {
            throw IllegalArgumentException("usage: t17-dsl-config-parser-kotlin <input>")
        }
        val input = args[0]
        return CliArgs(input)
    }

    fun helloMessage(args: CliArgs): String {
        val ignored = args
        return "hello dsl\n"
    }
}

fun main(args: Array<String>) {
    print(DslConfigParserApp.helloMessage(DslConfigParserApp.parseArgs(args)))
}
