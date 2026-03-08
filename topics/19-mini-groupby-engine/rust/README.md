# 19. mini group-by engine / rust

## 어디에 작성하나

- 핵심 로직: `src/lib.rs`
- CLI 진입점: `src/main.rs`
- 기본 테스트: `tests/smoke.rs`
- 프로젝트 명령: `Makefile`
- 입력 fixture: `../fixtures/`
- e2e 스크립트: `../e2e/rust-smoke.sh`

## 템플릿 기본 상태

- 기본 출력: `hello groupby`
- CLI 스캐폴드: `main` 또는 `cli`가 `argv` 위치 계약만 이미 처리합니다.
- 이 상태는 시작점일 뿐이며, 실제 미션 성공 기준은 `make e2e`와 `../SPEC.md`에 있습니다.
- fresh scaffold 상태에서 `make e2e`는 실패해도 정상입니다.

## 인자 위치 계약

- `argv[1]`: `input` (`예: ../fixtures/sales.csv`)

## 어떻게 작성하나

- 핵심 로직은 `lib.rs`에 두고 `main.rs`는 인자 파싱과 출력만 담당하게 두는 편이 좋다.
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

- `source scripts/env.sh && cargo build --manifest-path topics/19-mini-groupby-engine/rust/Cargo.toml`
- `source scripts/env.sh && cargo run --manifest-path topics/19-mini-groupby-engine/rust/Cargo.toml -- topics/19-mini-groupby-engine/fixtures/sales.csv`
- `./target/debug/t19_mini_groupby_engine_rust topics/19-mini-groupby-engine/fixtures/sales.csv`

## 권장 구현 순서

1. `../SPEC.md`에서 최종 미션 요구사항을 읽습니다.
2. `../fixtures/expected.txt`로 hello baseline을 확인합니다.
3. `../fixtures/mission-expected.txt` 또는 대응 fixture를 보고 e2e 성공 기준을 확인합니다.
4. 먼저 `make build`와 `make run`이 유지되도록 구현한 뒤, `make test`와 `make e2e`를 맞춥니다.
