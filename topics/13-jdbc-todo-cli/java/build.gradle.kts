plugins {
            application
            java
        }

        java {
            toolchain {
                languageVersion.set(JavaLanguageVersion.of(25))
            }
        }

        dependencies {
            testImplementation(libs.junit.jupiter)
            testRuntimeOnly(libs.junit.platform.launcher)
            implementation(libs.h2)
}

        tasks.test {
            useJUnitPlatform()
        }

        application {
            mainClass.set("dev.reinvent.wheel.t13.JdbcTodoCliApp")
        }
