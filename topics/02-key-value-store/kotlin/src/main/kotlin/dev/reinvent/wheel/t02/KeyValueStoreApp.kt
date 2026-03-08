package dev.reinvent.wheel.t02

object KeyValueStoreApp {
    data class CliArgs(val input: String)

    fun parseArgs(args: Array<String>): CliArgs {
        if (args.size < 1 || args.size > 1) {
            throw IllegalArgumentException("usage: t02-key-value-store-kotlin <input>")
        }
        val input = args[0]
        return CliArgs(input)
    }

    fun helloMessage(args: CliArgs): String {
        val ignored = args
        return "hello kv-store\n"
    }
}

fun main(args: Array<String>) {
    print(KeyValueStoreApp.helloMessage(KeyValueStoreApp.parseArgs(args)))
}
