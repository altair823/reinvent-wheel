# 07. `arena allocator`

메모리 관리 감각을 직접 되살리는 데 좋다.

## 언어

- Rust

## 먼저 볼 것

- `SPEC.md`: 최종 미션 요구사항과 템플릿 baseline을 함께 설명합니다.
- `QA.md`: 어떤 테스트를 통과해야 하는지와 e2e 성공 기준을 정리합니다.
- `fixtures/`: hello 출력용 fixture와 mission 출력용 fixture를 함께 둡니다.
- `e2e/`: 언어별 미션 acceptance test 스크립트가 있습니다.

## 템플릿 기본 상태

- 이 토픽의 fresh template은 `make run`에서 `hello arena`를 출력합니다.
- `make smoke`는 이 최소 실행 경로만 확인합니다.
- `make e2e`는 최종 미션 성공 기준을 검증합니다. 처음에는 실패해도 정상입니다.

## 어떻게 진행하나

1. `SPEC.md`와 `QA.md`를 먼저 읽습니다.
2. `fixtures/expected.txt`와 `fixtures/mission-expected.txt` 또는 대응 fixture를 함께 확인합니다.
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
- 템플릿 기본 상태: `make -C rust run`은 `hello arena`를 출력합니다.
- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.
- 인자 위치 계약:
  - `argv[1]`: `input` (`예: ../fixtures/words.txt`)
- Make 명령: `make -C rust build`, `make -C rust run`, `make -C rust test`, `make -C rust e2e`, `make -C rust smoke`
- 직접 실행 예시:
  - `source scripts/env.sh && cargo build --manifest-path topics/07-arena-allocator/rust/Cargo.toml`
  - `source scripts/env.sh && cargo run --manifest-path topics/07-arena-allocator/rust/Cargo.toml -- topics/07-arena-allocator/fixtures/words.txt`
  - `./target/debug/t07_arena_allocator_rust topics/07-arena-allocator/fixtures/words.txt`
- e2e 스크립트: `e2e/rust-smoke.sh`

## 빠른 실행

- Rust: `make -C rust build`, `make -C rust run`, `make -C rust test`, `make -C rust e2e`, `make -C rust smoke`

## 문서

- `SPEC.md`
- `QA.md`

언어별 상세 직접 실행 예시는 각 언어 폴더의 `README.md`에도 정리되어 있습니다.
