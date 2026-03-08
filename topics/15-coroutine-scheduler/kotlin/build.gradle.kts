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
            implementation(libs.kotlinx.coroutines.core)
}

        tasks.test {
            useJUnitPlatform()
        }

        application {
            mainClass.set("dev.reinvent.wheel.t15.CoroutineSchedulerAppKt")
        }
