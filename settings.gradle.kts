rootProject.name = "hand-coding-wheel"

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        mavenCentral()
    }
}

pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}

fun includeProject(pathName: String, dirName: String) {
    include(pathName)
    project(pathName).projectDir = file(dirName)
}

includeProject(":t02-key-value-store-java", "topics/02-key-value-store/java")
includeProject(":t02-key-value-store-kotlin", "topics/02-key-value-store/kotlin")
includeProject(":t03-http-server-router-java", "topics/03-http-server-router/java")
includeProject(":t03-http-server-router-kotlin", "topics/03-http-server-router/kotlin")
includeProject(":t04-json-parser-java", "topics/04-json-parser/java")
includeProject(":t05-thread-pool-queue-java", "topics/05-thread-pool-queue/java")
includeProject(":t12-di-container-java", "topics/12-di-container/java")
includeProject(":t13-jdbc-todo-cli-java", "topics/13-jdbc-todo-cli/java")
includeProject(":t14-rate-limiter-java", "topics/14-rate-limiter/java")
includeProject(":t15-coroutine-scheduler-kotlin", "topics/15-coroutine-scheduler/kotlin")
includeProject(":t16-notes-app-jvm-kotlin", "topics/16-notes-app-jvm/kotlin")
includeProject(":t17-dsl-config-parser-kotlin", "topics/17-dsl-config-parser/kotlin")
