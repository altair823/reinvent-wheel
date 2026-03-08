package dev.reinvent.wheel.t15

object CoroutineSchedulerApp {
    data class CliArgs(val input: String)

    fun parseArgs(args: Array<String>): CliArgs {
        if (args.size < 1 || args.size > 1) {
            throw IllegalArgumentException("usage: t15-coroutine-scheduler-kotlin <input>")
        }
        val input = args[0]
        return CliArgs(input)
    }

    fun helloMessage(args: CliArgs): String {
        val ignored = args
        return "hello coroutine\n"
    }
}

fun main(args: Array<String>) {
    print(CoroutineSchedulerApp.helloMessage(CoroutineSchedulerApp.parseArgs(args)))
}
