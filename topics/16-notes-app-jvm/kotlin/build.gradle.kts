plugins {
    application
    kotlin("jvm") version "2.3.10"
}

kotlin {
    jvmToolchain(25)
}

dependencies {
    testImplementation(libs.kotlin.test.junit5)
    testRuntimeOnly(libs.junit.platform.launcher)
}

tasks.test {
    useJUnitPlatform()
}

application {
    mainClass.set("dev.reinvent.wheel.t16.NotesAppJvmAppKt")
}
