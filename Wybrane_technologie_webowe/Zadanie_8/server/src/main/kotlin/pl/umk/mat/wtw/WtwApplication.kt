package pl.umk.mat.wtw

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class WtwApplication

fun main(args: Array<String>) {
    runApplication<WtwApplication>(*args)
}
