# 03. HTTP 서버와 라우터 직접 만들기 / kotlin

## 어디에 작성하나

- 핵심 로직/앱: `src/main/kotlin/dev/reinvent/wheel/t03/HttpServerRouterApp.kt`
- 기본 테스트: `src/test/kotlin/dev/reinvent/wheel/t03/HttpServerRouterAppTest.kt`
- 프로젝트 설정: `build.gradle.kts`
- 프로젝트 명령: `Makefile`
- 입력 fixture: `../fixtures/`
- e2e 스크립트: `../e2e/kotlin-smoke.sh`

## 템플릿 기본 상태

- 기본 서버 계약: `GET /health -> ok`, `POST /echo -> body 그대로`
- CLI 스캐폴드: `main` 또는 `cli`가 `argv` 위치 계약만 이미 처리합니다.
- 이 상태는 시작점일 뿐이며, 실제 미션 성공 기준은 `make e2e`와 `../SPEC.md`에 있습니다.
- fresh scaffold 상태에서 `make e2e`는 실패해도 정상입니다.

## 인자 위치 계약

- `argv[1]`: 선택 사항 `port` (`기본값: 18080`)

## 어떻게 작성하나

- `src/main/kotlin`의 `*App.kt`를 시작점으로 두고, 로직이 커지면 같은 패키지에 파일을 나눠 추가하면 된다.
- 템플릿의 인자 개수, 위치, stdout 형식은 가능하면 유지하고 내부 구현만 교체하는 편이 가장 안전합니다.
- `../SPEC.md`의 번호형 요구사항을 만족시키는 구현을 목표로 합니다.
- `../QA.md`와 `../e2e/*.sh`가 실제 성공 기준입니다.
- 빌드 산출물(`build/`, `target/`, `bin/`, `__pycache__/`)은 수정 대상이 아닙니다.

## Make 명령

- `make build`
- `make run`
- `make test`
- `make e2e`
- `make smoke`

## make 없이 직접 실행하는 방법

- `source scripts/env.sh && ./gradlew :t03-http-server-router-kotlin:installDist`
- `source scripts/env.sh && ./gradlew -q :t03-http-server-router-kotlin:run`
- `source scripts/env.sh && topics/03-http-server-router/kotlin/build/install/t03-http-server-router-kotlin/bin/t03-http-server-router-kotlin`

## 권장 구현 순서

1. `../SPEC.md`에서 최종 미션 요구사항을 읽습니다.
2. `make run` 또는 `make smoke`로 서버 baseline이 뜨는지 먼저 확인합니다.
3. `../e2e/*.sh`를 열어서 health, echo, 오류 응답 기준을 확인합니다.
4. 먼저 `make build`와 `make run`이 유지되도록 구현한 뒤, `make test`와 `make e2e`를 맞춥니다.
