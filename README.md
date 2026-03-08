# Hand-Coding Monorepo

손코딩 연습용 모노레포입니다. `HAND_CODING_TOPICS.md`에 있는 25개 토픽과 42개 실제 프로젝트를 함께 관리합니다.
이 저장소의 기본 템플릿은 의도적으로 아주 얇습니다. 대부분의 프로젝트는 `make run`에서 최소 hello 동작만 보장하고, 실제 미션 성공 기준은 `make e2e`에 들어 있습니다.

## 빠른 시작

1. `make bootstrap`
2. `make smoke`
3. `make verify`

`bootstrap`은 로컬 툴체인을 준비합니다. `smoke`는 42개 프로젝트의 hello 템플릿 실행 경로를 실제로 돌립니다. `verify`는 테스트와 e2e를 끝까지 순회하며, 실패가 있어도 요약을 남기고 마지막에만 실패 코드로 종료합니다.
에디터의 `rust-analyzer`는 repo-local `.toolchains/` 경로를 자동으로 모를 수 있습니다. Rust 관련 `cargo`/`rustc` not found 오류가 나면 `source scripts/env.sh`를 실행한 셸에서 에디터를 다시 열거나, 에디터 PATH에 `.toolchains/cargo/bin`을 추가하세요.

## 템플릿 철학

이 저장소는 “거의 완성된 예제 모음”이 아니라 “직접 구현해야 하는 시작점”을 목표로 합니다.

- 비HTTP 프로젝트의 기본 템플릿은 `main`, `lib/core`, 기본 테스트 구조만 남긴 최소 실행 골격입니다.
- 각 언어 템플릿의 `main` 또는 `cli`에는 기본 `argv` 위치 계약만 이미 들어 있으므로, 구현 시에는 보통 로직 파일만 채우면 됩니다.
- HTTP 프로젝트만 예외로 작은 실제 서버를 제공합니다. 기본 계약은 `GET /health -> ok`, `POST /echo -> body 그대로`입니다.
- `fixtures/expected.txt`는 hello 템플릿용 기대 출력입니다.
- `fixtures/mission-expected.txt`는 최종 미션 성공 기준입니다.
- 따라서 freshly generated 상태에서 `make smoke`는 통과할 수 있지만, `make e2e`와 루트 `make verify`는 실패할 수 있습니다.
- 미션 성공 여부는 언어별 `e2e/*.sh`, 토픽의 `SPEC.md`, `QA.md`를 함께 보고 판단합니다.

## 실행 환경과 기술 스택

이 저장소는 아래 환경을 기준으로 테스트했습니다.

| 항목 | 기준 |
| --- | --- |
| OS | Ubuntu 24.04 LTS |
| 아키텍처 | Linux `x86_64` / `amd64` |
| 기본 셸 | `bash` |
| 네트워크 | 첫 `make bootstrap` 시 외부 HTTPS 다운로드 필요 |

### 언어와 빌드 도구 버전

| 구성요소 | 버전 | 용도 |
| --- | --- | --- |
| Rust | `1.94.0` | Rust 토픽 빌드/테스트 |
| C++ 표준 | `C++23` | C++ 토픽 빌드 기준 |
| Java | `25.0.2` | Java 토픽 및 Gradle 실행용 JDK |
| Kotlin | `2.3.10` | Kotlin 토픽 소스/테스트 |
| Gradle | `9.4.0` | Java/Kotlin 빌드 |
| Python | `3.14.3` | Python 토픽 실행/테스트 |

### 추가 라이브러리와 프레임워크

| 구성요소 | 버전 | 사용 위치 |
| --- | --- | --- |
| JUnit Jupiter | `5.13.1` | Java 테스트 |
| JUnit Platform Launcher | `1.13.1` | Gradle JVM 테스트 런처 |
| Kotlin Test JUnit5 | `2.3.10` | Kotlin 테스트 |
| kotlinx-coroutines-core | `1.10.2` | Kotlin coroutine 토픽 |
| H2 | `2.3.232` | `jdbc-todo-cli` |
| DuckDB | `>=1.3.2` | SQL 기준선 비교가 필요한 Python 토픽 |

### 시스템 도구 요구사항

아래 도구 또는 그에 준하는 패키지가 필요합니다.

- `build-essential`: `gcc`, `g++`, `make` 포함
- `curl`: Rust/JDK/Gradle/Python 소스 다운로드
- `tar`, `gzip`, `xz-utils`: 아카이브 해제
- `pkg-config`: Python 빌드 보조
- 기본 유닉스 도구: `find`, `grep`, `head`, `chmod`

### Ubuntu 24.04 권장 패키지

전체 부트스트랩을 안정적으로 수행하려면 아래 패키지 구성을 권장합니다.

```bash
sudo apt update
sudo apt install -y build-essential curl ca-certificates pkg-config \
  zlib1g-dev libssl-dev libbz2-dev libffi-dev liblzma-dev \
  libreadline-dev libsqlite3-dev tk-dev xz-utils
```

위 패키지들은 특히 Python `3.14.3`를 소스에서 빌드할 때 중요합니다. `libssl-dev`와 `zlib1g-dev`가 없으면 현재 부트스트랩 스크립트 기준으로 `pip`/`duckdb` 설치가 제한될 수 있습니다.

### 언어별 구현 특성

- Rust 템플릿은 외부 crate 없이 표준 라이브러리 중심입니다.
- C++ 템플릿은 외부 프레임워크 없이 표준 라이브러리와 `g++`만 사용합니다.
- Java/Kotlin 템플릿은 Gradle과 Maven Central 의존성 해석을 사용합니다.
- Python 템플릿은 기본적으로 표준 라이브러리 중심이며, 일부 데이터 토픽만 `duckdb`를 사용합니다.
- HTTP 토픽 smoke/e2e 테스트에는 `curl`이 필요합니다.

## 템플릿 저장소로 볼 때 가장 중요한 점

이 저장소는 단순 샘플 모음이 아니라, 파이썬 생성 스크립트로 전체 뼈대를 다시 만들어낼 수 있는 템플릿 저장소입니다.

- 손코딩 사용자 관점: `topics/` 아래 생성된 프로젝트를 직접 수정해서 연습합니다.
- 템플릿 유지보수자 관점: `scripts/scaffold_*.py` 쪽을 수정한 뒤 다시 생성합니다.
- 매우 중요: `python3 scripts/scaffold_repo.py`를 실행하면 루트 문서, 토픽 문서, fixture, e2e, 언어별 hello 템플릿이 다시 작성됩니다.
- 따라서 손으로 구현한 결과를 보존해야 하는 작업 브랜치에서는 `scaffold_repo.py`를 함부로 다시 돌리지 않는 편이 안전합니다.
- 외부 공개용 템플릿을 운영할 때는 `template` 성격의 브랜치와 실제 손코딩 결과 브랜치를 분리하는 편이 관리하기 쉽습니다.

## 어디서 구현하나

모든 작업은 `topics/` 아래에서 진행합니다.

- 토픽 하나는 `topics/NN-topic-slug/` 디렉터리 하나에 대응합니다.
- 토픽 설명은 `README.md`에 있습니다.
- 요구사항은 `SPEC.md`에 있습니다.
- 체크리스트는 `QA.md`에 있습니다.
- 샘플 입력과 기대 출력은 `fixtures/`에 있습니다.
- 종단간 테스트 스크립트는 `e2e/`에 있습니다.
- 실제 구현은 각 언어 폴더(`rust/`, `cpp/`, `java/`, `kotlin/`, `python/`) 안에서 진행합니다.

예를 들어 `mini-grep`을 Rust로 풀고 싶다면 아래 순서로 보면 됩니다.

1. `topics/01-mini-grep/SPEC.md`
2. `topics/01-mini-grep/QA.md`
3. `topics/01-mini-grep/fixtures/`
4. `topics/01-mini-grep/rust/src/lib.rs`
5. `topics/01-mini-grep/rust/src/main.rs`
6. `topics/01-mini-grep/rust/tests/smoke.rs`

## 언어별로 어디를 고치나

### Rust

- 핵심 로직: `topics/NN-topic-slug/rust/src/lib.rs`
- CLI 진입점: `topics/NN-topic-slug/rust/src/main.rs`
- 테스트: `topics/NN-topic-slug/rust/tests/`
- 빌드: `make -C topics/NN-topic-slug/rust build`
- 실행: `make -C topics/NN-topic-slug/rust run`
- 테스트: `make -C topics/NN-topic-slug/rust test`
- e2e: `make -C topics/NN-topic-slug/rust e2e`

권장 방식은 `lib.rs`에 로직을 두고 `main.rs`는 인자 파싱과 출력만 얇게 유지하는 것입니다.

### C++

- 공개 인터페이스: `topics/NN-topic-slug/cpp/include/topic.hpp`
- 핵심 로직: `topics/NN-topic-slug/cpp/src/lib.cpp`
- CLI 진입점: `topics/NN-topic-slug/cpp/src/main.cpp`
- 테스트: `topics/NN-topic-slug/cpp/tests/test_main.cpp`
- 빌드: `make -C topics/NN-topic-slug/cpp build`
- 실행: `make -C topics/NN-topic-slug/cpp run`
- 테스트: `make -C topics/NN-topic-slug/cpp test`
- e2e: `make -C topics/NN-topic-slug/cpp e2e`

보통 `topic.hpp`에 함수 시그니처를 두고, `lib.cpp`에서 구현하고, `main.cpp`는 입출력만 담당하게 두면 관리하기 쉽습니다.

### Java

- 핵심 로직/앱: `topics/NN-topic-slug/java/src/main/java/...`
- 테스트: `topics/NN-topic-slug/java/src/test/java/...`
- 빌드 설정: `topics/NN-topic-slug/java/build.gradle.kts`
- 빌드: `make -C topics/NN-topic-slug/java build`
- 실행: `make -C topics/NN-topic-slug/java run`
- 테스트: `make -C topics/NN-topic-slug/java test`
- e2e: `make -C topics/NN-topic-slug/java e2e`

일반적으로 `src/main/java`의 `*App.java`를 시작점으로 보시면 됩니다.

### Kotlin

- 핵심 로직/앱: `topics/NN-topic-slug/kotlin/src/main/kotlin/...`
- 테스트: `topics/NN-topic-slug/kotlin/src/test/kotlin/...`
- 빌드 설정: `topics/NN-topic-slug/kotlin/build.gradle.kts`
- 빌드: `make -C topics/NN-topic-slug/kotlin build`
- 실행: `make -C topics/NN-topic-slug/kotlin run`
- 테스트: `make -C topics/NN-topic-slug/kotlin test`
- e2e: `make -C topics/NN-topic-slug/kotlin e2e`

일반적으로 `src/main/kotlin`의 `*App.kt`를 시작점으로 보시면 됩니다.

### Python

- 핵심 로직: `topics/NN-topic-slug/python/src/<package>/core.py`
- CLI 진입점: `topics/NN-topic-slug/python/src/<package>/cli.py`
- 테스트: `topics/NN-topic-slug/python/tests/test_topic.py`
- 패키지 설정: `topics/NN-topic-slug/python/pyproject.toml`
- 실행: `make -C topics/NN-topic-slug/python run`
- 테스트: `make -C topics/NN-topic-slug/python test`
- e2e: `make -C topics/NN-topic-slug/python e2e`

권장 방식은 `core.py`에 순수 로직을 두고 `cli.py`는 파일 읽기, 인자 파싱, 출력만 맡기는 것입니다.

## 어떻게 진행하나

각 프로젝트에는 이미 최소 hello 템플릿이 들어 있습니다. 손코딩 연습은 그 템플릿을 완전히 갈아엎기보다, 현재 CLI와 출력 계약을 유지한 채 내부 구현을 직접 다시 쓰는 방식이 가장 편합니다.

권장 순서는 아래와 같습니다.

1. 토픽의 `SPEC.md`와 `QA.md`를 먼저 읽습니다.
2. `fixtures/expected.txt`와 `fixtures/mission-expected.txt` 또는 대응 fixture를 함께 보고 hello 기준과 mission 기준을 분리해서 확인합니다.
3. 현재 hello 템플릿을 `make run` 또는 `make smoke`로 한 번 실행합니다.
4. `lib`, `core`, `App` 쪽 구현 파일을 직접 다시 씁니다.
5. 필요한 단위 테스트를 추가하거나 보강합니다.
6. 개발 중에는 가능한 언어에서 `make build`를 쓰고, 공통적으로 `make run`, `make test`를 자주 실행합니다.
7. 미션 완료 여부는 언어별 `make e2e`로 확인합니다.
8. 토픽이 끝나면 루트에서 `make verify` 또는 `make smoke`로 전체 상태를 확인합니다.

## 구현할 때 지키면 좋은 기준

- `main`이나 `cli`는 얇게 두고 핵심 로직은 라이브러리 쪽 파일에 두는 편이 좋습니다.
- `fixtures/expected.txt`는 템플릿 baseline, `fixtures/mission-expected.txt`는 미션 baseline으로 봅니다.
- `fixtures/` 입력 형식과 `e2e/` 스크립트가 기대하는 인자 개수/위치, stdout 형식은 가능하면 유지합니다.
- `build/`, `target/`, `bin/`, `__pycache__/`는 생성 산출물이므로 직접 수정하지 않습니다.
- 루트 `verify`는 의도적으로 실패를 모아 보여주므로, 개발 중에는 토픽 단위 `build/run/test/e2e`를 먼저 실행하는 편이 낫습니다.

## 직접 실행은 어디에 적혀 있나

각 토픽의 `README.md`와 각 언어 폴더의 `README.md`에는 아래 두 가지가 모두 들어 있습니다.

- `make run`, `make test`, `make e2e`, `make smoke` 같은 템플릿 공통 진입점
- `cargo run`, `./gradlew :project:run`, `./bin/<app>`, `python -m ...` 같은 직접 실행 경로

따라서 실제 구현할 때는 루트 README보다 토픽 README와 언어 README를 먼저 보는 편이 좋습니다.

## 템플릿 생성 스크립트 설명

외부 공개용 템플릿으로 관리할 때는 `scripts/` 아래 파일들의 역할을 구분해서 이해하는 것이 중요합니다.

### 1. 메타데이터와 문서 생성

- `scripts/scaffold_catalog.py`
- 이 파일이 템플릿의 가장 중요한 소스 오브 트루스입니다.
- `TOPICS` 리스트에 토픽 번호, 슬러그, 언어, 설명, 훈련 포인트, 최소 목표, 확장 목표가 들어 있습니다.
- `fixtures_for(topic)`는 hello 기준 fixture와 mission 기준 fixture를 함께 만듭니다.
- `render_hand_coding_topics()`는 루트 `HAND_CODING_TOPICS.md`를 생성합니다.
- `render_root_readme()`는 루트 `README.md`를 생성합니다.
- `render_topic_readme()`, `render_topic_spec()`, `render_topic_qa()`는 각 토픽 문서를 생성합니다.
- 즉, 토픽 설명 문구나 문서 구조를 바꾸고 싶다면 보통 여기부터 수정하면 됩니다.

### 2. 전체 스캐폴드 오케스트레이션

- `scripts/scaffold_repo.py`
- 전체 템플릿을 실제 파일 트리로 생성하는 진입점입니다.
- `main()`은 루트 문서, 루트 빌드 파일, 툴체인 설정 파일, 보조 스크립트, 토픽 디렉터리를 한 번에 생성합니다.
- `create_topic(topic)`은 토픽 하나를 만들고, 언어별 생성 함수로 분기합니다.
- 루트 `Makefile`, `Cargo.toml`, `settings.gradle.kts`, `build.gradle.kts`, `toolchains/versions.env`, `scripts/bootstrap-*.sh`, `scripts/verify-all.sh`, `scripts/smoke-all.sh`도 이 파일에서 생성됩니다.
- 따라서 템플릿 구조 자체를 바꾸고 싶다면 보통 이 파일의 `render_*` 또는 `create_topic()` 흐름을 수정합니다.

### 3. 언어별 프로젝트 템플릿

- `scripts/scaffold_rust_projects.py`
- Rust 프로젝트의 `Cargo.toml`, `Makefile`, `src/lib.rs`, `src/main.rs`, `tests/smoke.rs`, `e2e/rust-smoke.sh`를 생성합니다.
- 비HTTP hello 템플릿과 HTTP 최소 서버, Rust e2e 미션 기준, `make build` 경로를 여기에서 관리합니다.

- `scripts/scaffold_cpp_projects.py`
- C++ 프로젝트의 `Makefile`, `include/topic.hpp`, `src/lib.cpp`, `src/main.cpp`, `tests/test_main.cpp`, `e2e/cpp-smoke.sh`를 생성합니다.
- C++ hello 템플릿, 직접 실행 binary 경로, mission e2e 기준을 여기서 조정합니다.

- `scripts/scaffold_jvm_projects.py`
- Java와 Kotlin 프로젝트의 `build.gradle.kts`, `Makefile`, `src/main/...`, `src/test/...`, `e2e/*.sh`를 생성합니다.
- JVM hello 템플릿, HTTP 최소 서버, `installDist` 기반 직접 실행 경로, mission e2e 정책도 이 파일에서 관리합니다.

- `scripts/scaffold_python_projects.py`
- Python 프로젝트의 `pyproject.toml`, `Makefile`, `src/<package>/core.py`, `src/<package>/cli.py`, `tests/test_topic.py`, `e2e/python-smoke.sh`를 생성합니다.
- Python hello 템플릿, 인자 위치 계약, mission e2e 기준을 여기서 수정합니다.

### 4. 실행 환경과 검증 스크립트

- `scripts/env.sh`
- repo-local 툴체인 경로, `CARGO_HOME`, `RUSTUP_HOME`, `JAVA_HOME`, `PYTHON_BIN`, `GRADLE_BIN` 등을 통일해서 잡아줍니다.
- 각 프로젝트의 `Makefile`은 이 스크립트를 source해서 실행 환경을 맞춥니다.
- 다만 에디터나 LSP는 이 스크립트를 자동으로 source하지 않을 수 있으므로, 특히 Rust 작업 시에는 이 셸에서 에디터를 열거나 `.toolchains/cargo/bin`이 PATH에 포함되도록 맞춰야 합니다.

- `scripts/bootstrap-rust.sh`, `scripts/bootstrap-jdk.sh`, `scripts/bootstrap-gradle.sh`, `scripts/bootstrap-python.sh`
- 템플릿을 처음 받는 사용자가 `make bootstrap`만으로 필요한 툴체인을 로컬 `.toolchains/` 아래에 준비할 수 있게 해줍니다.
- 외부 공개용 템플릿에서는 설치 과정을 한곳에서 관리하기 위해 이 스크립트들이 중요합니다.

- `scripts/verify-all.sh`
- Rust workspace 테스트, C++ 테스트, Python 테스트, Gradle JVM 테스트, 모든 e2e 스크립트를 끝까지 순회합니다.
- 실패가 있어도 중간에 멈추지 않고, `artifacts/verify/summary.txt`에 요약을 남깁니다.
- 템플릿 기본 상태에서는 e2e 실패가 날 수 있으므로, 이 스크립트는 “현재 미완성 상태까지 포함한 전체 점검”에 가깝습니다.

- `scripts/smoke-all.sh`
- 각 프로젝트의 hello/demo 실행 경로를 실제로 한 번씩 실행합니다.
- 실패가 있어도 끝까지 돌고 `artifacts/smoke/summary.txt`에 요약을 남깁니다.
- 템플릿이 “최소 실행 가능 상태”인지 확인할 때 사용합니다.

- `scripts/list-projects.py`
- 현재 생성된 프로젝트 디렉터리를 기준으로 순회 목록을 만듭니다.
- `verify-all.sh`와 `smoke-all.sh`가 이 목록을 사용합니다.

## 어떤 파일이 생성되고, 어떤 파일을 수정해야 하나

템플릿 유지보수자 입장에서는 “생성 스크립트를 고쳐야 하는 파일”과 “직접 수정해도 되는 파일”을 구분해야 합니다.

### 생성 스크립트를 고쳐야 하는 경우

아래 파일들은 `python3 scripts/scaffold_repo.py`를 다시 실행하면 덮어써질 수 있습니다.

- 루트 `README.md`
- 루트 `HAND_CODING_TOPICS.md`
- 루트 `Makefile`, `Cargo.toml`, `settings.gradle.kts`, `build.gradle.kts`
- `toolchains/versions.env`
- `scripts/env.sh`, `scripts/bootstrap-*.sh`, `scripts/verify-all.sh`, `scripts/smoke-all.sh`, `scripts/list-projects.py`
- `topics/*/README.md`, `topics/*/SPEC.md`, `topics/*/QA.md`
- `topics/*/fixtures/*`, `topics/*/e2e/*`
- `topics/*/<language>/` 아래 기본 hello 템플릿 파일들

이런 파일을 영구적으로 바꾸고 싶다면 생성 결과물을 직접 수정하지 말고, 해당 `render_*` 함수나 `TOPICS` 메타데이터를 수정한 뒤 다시 생성해야 합니다.

### 손코딩 사용자가 직접 수정하는 파일

아래 파일들은 연습용 구현을 넣는 자리입니다.

- `topics/*/rust/src/*.rs`
- `topics/*/cpp/include/*`, `topics/*/cpp/src/*`, `topics/*/cpp/tests/*`
- `topics/*/java/src/main/*`, `topics/*/java/src/test/*`
- `topics/*/kotlin/src/main/*`, `topics/*/kotlin/src/test/*`
- `topics/*/python/src/*`, `topics/*/python/tests/*`

다만 이 파일들도 `scaffold_repo.py`를 다시 실행하면 hello 템플릿으로 돌아갈 수 있으니, 손코딩 결과를 보존하려면 재생성 작업과 분리해서 관리하는 편이 좋습니다.

## 새 토픽을 추가하거나 기존 템플릿을 바꾸는 절차

템플릿 유지보수자는 보통 아래 순서로 작업하시면 됩니다.

1. `scripts/scaffold_catalog.py`의 `TOPICS`에 새 토픽 메타데이터를 추가합니다.
2. 같은 파일의 `fixtures_for(topic)`, `spec_items(topic)`, 문서 렌더러가 새 토픽을 이해하도록 맞춥니다.
3. 새 `kind`가 필요한 경우 각 언어 스크립트(`scaffold_rust_projects.py`, `scaffold_cpp_projects.py`, `scaffold_jvm_projects.py`, `scaffold_python_projects.py`)에 해당 토픽 분기를 추가합니다.
4. 루트 구조나 공통 스크립트가 바뀌면 `scripts/scaffold_repo.py`의 `render_*` 함수 또는 `create_topic()`를 수정합니다.
5. `python3 scripts/scaffold_repo.py`로 파일 트리를 다시 생성합니다.
6. `make verify`와 `make smoke`로 전체 상태를 확인합니다.

기존 토픽의 문구만 바꿀 때는 대부분 `scaffold_catalog.py`만 고치면 충분합니다. 반대로 실제 hello 코드 동작이나 인자 위치 계약을 바꾸는 경우는 언어별 `scaffold_*_projects.py`까지 같이 수정해야 합니다.

## 템플릿 유지보수용 자주 쓰는 명령

- 전체 재생성: `python3 scripts/scaffold_repo.py`
- 툴체인 준비: `make bootstrap`
- 전체 검증: `make verify`
- 전체 스모크: `make smoke`
- 생성기 문법 체크: `python3 -m py_compile scripts/scaffold_catalog.py scripts/scaffold_repo.py scripts/scaffold_rust_projects.py scripts/scaffold_cpp_projects.py scripts/scaffold_jvm_projects.py scripts/scaffold_python_projects.py`

## 자주 쓰는 명령

- 전체 검증: `make verify`
- 전체 스모크: `make smoke`
- Rust 하나만: `make -C topics/01-mini-grep/rust smoke`
- C++ 하나만: `make -C topics/01-mini-grep/cpp smoke`
- Java 하나만: `make -C topics/02-key-value-store/java smoke`
- Kotlin 하나만: `make -C topics/02-key-value-store/kotlin smoke`
- Python 하나만: `make -C topics/18-dataset-profiler/python smoke`

## 프로젝트 목록

| 번호 | 슬러그 | 언어 | 설명 |
| --- | --- | --- | --- |
| 01 | `mini-grep` | rust, cpp | `grep` 비슷한 미니 텍스트 검색기 |
| 02 | `key-value-store` | rust, java, kotlin | 인메모리 `key-value store` |
| 03 | `http-server-router` | rust, java, kotlin | HTTP 서버와 라우터 직접 만들기 |
| 04 | `json-parser` | rust, cpp, java | 간단한 `JSON parser` |
| 05 | `thread-pool-queue` | rust, cpp, java | 스레드 풀과 작업 큐 |
| 06 | `mini-git-object-store` | rust | 미니 `git` 객체 저장소 |
| 07 | `arena-allocator` | rust | `arena allocator` |
| 08 | `tiny-async-executor` | rust | `tiny async executor` |
| 09 | `tiny-vector` | cpp | 작은 벡터/문자열 클래스 구현 |
| 10 | `expression-evaluator` | cpp | expression evaluator |
| 11 | `file-log-library` | cpp | 파일 기반 로그 라이브러리 |
| 12 | `di-container` | java | 작은 dependency injection container |
| 13 | `jdbc-todo-cli` | java | 간단한 JDBC-backed todo app |
| 14 | `rate-limiter` | java | rate limiter |
| 15 | `coroutine-scheduler` | kotlin | 코루틴 기반 작업 스케줄러 |
| 16 | `notes-app-jvm` | kotlin | 간단한 Kotlin/JVM 메모 앱 |
| 17 | `dsl-config-parser` | kotlin | DSL 스타일 설정 파서 |
| 18 | `dataset-profiler` | rust, python | dataset profiler |
| 19 | `mini-groupby-engine` | rust, python, sql | mini group-by engine |
| 20 | `batch-etl-pipeline` | rust, python, shell | batch ETL pipeline |
| 21 | `parallel-log-analyzer` | rust, python, shell | parallel log analyzer |
| 22 | `external-sort-merge` | rust, python | external sort + merge |
| 23 | `windowed-timeseries-analyzer` | rust, python, sql | windowed timeseries analyzer |
| 24 | `heavy-hitter-stream` | rust, python | heavy hitter stream |
| 25 | `mini-mapreduce` | rust, python, shell | mini map-reduce on one machine |
