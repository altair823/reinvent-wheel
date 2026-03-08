# 03. HTTP 서버와 라우터 직접 만들기

프레임워크 없이 웹의 기본을 체득하기 좋다.

## 언어

- Rust, Java, Kotlin

## 먼저 볼 것

- `SPEC.md`: 최종 미션 요구사항과 템플릿 baseline을 함께 설명합니다.
- `QA.md`: 어떤 테스트를 통과해야 하는지와 e2e 성공 기준을 정리합니다.
- `fixtures/`: hello 출력용 fixture와 mission 출력용 fixture를 함께 둡니다.
- `e2e/`: 언어별 미션 acceptance test 스크립트가 있습니다.

## 템플릿 기본 상태

- 이 토픽의 fresh template은 작은 실제 HTTP 서버를 띄웁니다. 기본 계약은 `GET /health -> ok`, `POST /echo -> body 그대로`입니다.
- `make smoke`는 이 최소 실행 경로만 확인합니다.
- `make e2e`는 최종 미션 성공 기준을 검증합니다. 처음에는 실패해도 정상입니다.

## 어떻게 진행하나

1. `SPEC.md`와 `QA.md`를 먼저 읽습니다.
2. `fixtures/expected-health.txt`, `fixtures/expected-echo.txt`, `e2e/*.sh`를 함께 열어 baseline과 mission 기준을 확인합니다.
3. 원하는 언어 폴더에서 가능하면 `make -C <language> build`와 `make -C <language> run`을 먼저 실행합니다.
4. 아래 언어별 구현 파일을 직접 수정합니다.
5. 작업 중에는 `make -C <language> test`를 자주 돌리고, 마무리 단계에서 `make -C <language> e2e`로 미션 성공 여부를 확인합니다.
6. 가능하면 현재 인자 개수/위치와 stdout 형식은 유지한 채 내부 구현만 교체하는 방식으로 진행합니다.

## 언어별 구현 위치

### Rust

- 핵심 로직: `rust/src/lib.rs`
- CLI 진입점: `rust/src/main.rs`
- 기본 테스트: `rust/tests/smoke.rs`
- 프로젝트 명령: `rust/Makefile`
- 작성 방식: 핵심 로직은 `lib.rs`에 두고 `main.rs`는 인자 파싱과 출력만 담당하게 두는 편이 좋다.
- 템플릿 기본 상태: 작은 실제 HTTP 서버가 `GET /health`와 `POST /echo`만 처리합니다.
- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.
- 인자 위치 계약:
  - `argv[1]`: 선택 사항 `port` (`기본값: 18080`)
- Make 명령: `make -C rust build`, `make -C rust run`, `make -C rust test`, `make -C rust e2e`, `make -C rust smoke`
- 직접 실행 예시:
  - `source scripts/env.sh && cargo build --manifest-path topics/03-http-server-router/rust/Cargo.toml`
  - `source scripts/env.sh && cargo run --manifest-path topics/03-http-server-router/rust/Cargo.toml`
  - `./target/debug/t03_http_server_router_rust`
- e2e 스크립트: `e2e/rust-smoke.sh`

### Java

- 핵심 로직/앱: `java/src/main/java/dev/reinvent/wheel/t03/HttpServerRouterApp.java`
- 기본 테스트: `java/src/test/java/dev/reinvent/wheel/t03/HttpServerRouterAppTest.java`
- 프로젝트 설정: `java/build.gradle.kts`
- 프로젝트 명령: `java/Makefile`
- 작성 방식: `src/main/java`의 `*App.java`를 시작점으로 두고, 구현이 커지면 같은 패키지 아래 클래스를 추가하는 방식이 무난하다.
- 템플릿 기본 상태: 작은 실제 HTTP 서버가 `GET /health`와 `POST /echo`만 처리합니다.
- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.
- 인자 위치 계약:
  - `argv[1]`: 선택 사항 `port` (`기본값: 18080`)
- Make 명령: `make -C java build`, `make -C java run`, `make -C java test`, `make -C java e2e`, `make -C java smoke`
- 직접 실행 예시:
  - `source scripts/env.sh && ./gradlew :t03-http-server-router-java:installDist`
  - `source scripts/env.sh && ./gradlew -q :t03-http-server-router-java:run`
  - `source scripts/env.sh && topics/03-http-server-router/java/build/install/t03-http-server-router-java/bin/t03-http-server-router-java`
- e2e 스크립트: `e2e/java-smoke.sh`

### Kotlin

- 핵심 로직/앱: `kotlin/src/main/kotlin/dev/reinvent/wheel/t03/HttpServerRouterApp.kt`
- 기본 테스트: `kotlin/src/test/kotlin/dev/reinvent/wheel/t03/HttpServerRouterAppTest.kt`
- 프로젝트 설정: `kotlin/build.gradle.kts`
- 프로젝트 명령: `kotlin/Makefile`
- 작성 방식: `src/main/kotlin`의 `*App.kt`를 시작점으로 두고, 로직이 커지면 같은 패키지에 파일을 나눠 추가하면 된다.
- 템플릿 기본 상태: 작은 실제 HTTP 서버가 `GET /health`와 `POST /echo`만 처리합니다.
- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.
- 인자 위치 계약:
  - `argv[1]`: 선택 사항 `port` (`기본값: 18080`)
- Make 명령: `make -C kotlin build`, `make -C kotlin run`, `make -C kotlin test`, `make -C kotlin e2e`, `make -C kotlin smoke`
- 직접 실행 예시:
  - `source scripts/env.sh && ./gradlew :t03-http-server-router-kotlin:installDist`
  - `source scripts/env.sh && ./gradlew -q :t03-http-server-router-kotlin:run`
  - `source scripts/env.sh && topics/03-http-server-router/kotlin/build/install/t03-http-server-router-kotlin/bin/t03-http-server-router-kotlin`
- e2e 스크립트: `e2e/kotlin-smoke.sh`

## 빠른 실행

- Rust: `make -C rust build`, `make -C rust run`, `make -C rust test`, `make -C rust e2e`, `make -C rust smoke`
- Java: `make -C java build`, `make -C java run`, `make -C java test`, `make -C java e2e`, `make -C java smoke`
- Kotlin: `make -C kotlin build`, `make -C kotlin run`, `make -C kotlin test`, `make -C kotlin e2e`, `make -C kotlin smoke`

## 문서

- `SPEC.md`
- `QA.md`

언어별 상세 직접 실행 예시는 각 언어 폴더의 `README.md`에도 정리되어 있습니다.
