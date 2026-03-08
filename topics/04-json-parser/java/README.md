# 04. 간단한 `JSON parser` / java

## 어디에 작성하나

- 핵심 로직/앱: `src/main/java/dev/reinvent/wheel/t04/JsonParserApp.java`
- 기본 테스트: `src/test/java/dev/reinvent/wheel/t04/JsonParserAppTest.java`
- 프로젝트 설정: `build.gradle.kts`
- 프로젝트 명령: `Makefile`
- 입력 fixture: `../fixtures/`
- e2e 스크립트: `../e2e/java-smoke.sh`

## 템플릿 기본 상태

- 기본 출력: `hello json`
- CLI 스캐폴드: `main` 또는 `cli`가 `argv` 위치 계약만 이미 처리합니다.
- 이 상태는 시작점일 뿐이며, 실제 미션 성공 기준은 `make e2e`와 `../SPEC.md`에 있습니다.
- fresh scaffold 상태에서 `make e2e`는 실패해도 정상입니다.

## 인자 위치 계약

- `argv[1]`: `input` (`예: ../fixtures/sample.json`)

## 어떻게 작성하나

- `src/main/java`의 `*App.java`를 시작점으로 두고, 구현이 커지면 같은 패키지 아래 클래스를 추가하는 방식이 무난하다.
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

- `source scripts/env.sh && ./gradlew :t04-json-parser-java:installDist`
- `source scripts/env.sh && ./gradlew -q :t04-json-parser-java:run --args='topics/04-json-parser/fixtures/sample.json'`
- `source scripts/env.sh && topics/04-json-parser/java/build/install/t04-json-parser-java/bin/t04-json-parser-java topics/04-json-parser/fixtures/sample.json`

## 권장 구현 순서

1. `../SPEC.md`에서 최종 미션 요구사항을 읽습니다.
2. `../fixtures/expected.txt`로 hello baseline을 확인합니다.
3. `../fixtures/mission-expected.txt` 또는 대응 fixture를 보고 e2e 성공 기준을 확인합니다.
4. 먼저 `make build`와 `make run`이 유지되도록 구현한 뒤, `make test`와 `make e2e`를 맞춥니다.
