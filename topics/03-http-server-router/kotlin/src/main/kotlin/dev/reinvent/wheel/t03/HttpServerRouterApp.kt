package dev.reinvent.wheel.t03

import com.sun.net.httpserver.HttpExchange
import com.sun.net.httpserver.HttpServer
import java.net.InetSocketAddress

object HttpServerRouterApp {
    data class CliArgs(val port: Int)

    private fun parseInt(value: String, label: String): Int {
        return value.toIntOrNull() ?: throw IllegalArgumentException("$label must be an integer: $value")
    }

    fun parseArgs(args: Array<String>): CliArgs {
        if (args.size > 1) {
            throw IllegalArgumentException("usage: t03-http-server-router-kotlin [port]")
        }
        val port = if (args.isNotEmpty()) parseInt(args[0], "argv[1]") else System.getenv("PORT")?.let { parseInt(it, "PORT") } ?: 18080
        return CliArgs(port)
    }

    fun start(port: Int): HttpServer {
        val server = HttpServer.create(InetSocketAddress("127.0.0.1", port), 0)
        server.createContext("/health") { exchange ->
            if (exchange.requestMethod != "GET") {
                send(exchange, 405, "method-not-allowed\n")
            } else {
                send(exchange, 200, "ok\n")
            }
        }
        server.createContext("/echo") { exchange ->
            if (exchange.requestMethod != "POST") {
                send(exchange, 405, "method-not-allowed\n")
            } else {
                send(exchange, 200, exchange.requestBody.readBytes().decodeToString())
            }
        }
        server.createContext("/") { exchange ->
            send(exchange, 404, "not-found\n")
        }
        server.start()
        return server
    }

    private fun send(exchange: HttpExchange, status: Int, body: String) {
        val bytes = body.toByteArray()
        exchange.sendResponseHeaders(status, bytes.size.toLong())
        exchange.responseBody.use { it.write(bytes) }
        exchange.close()
    }
}

fun main(args: Array<String>) {
    val cliArgs = HttpServerRouterApp.parseArgs(args)
    HttpServerRouterApp.start(cliArgs.port)
    Thread.currentThread().join()
}
