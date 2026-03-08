# 20. batch ETL pipeline

업무형 배치 데이터 처리의 골격을 연습하기 좋다.

## 언어

- Rust, Python
- 셸 기반 보조 스모크 스크립트 포함

## 먼저 볼 것

- `SPEC.md`: 최종 미션 요구사항과 템플릿 baseline을 함께 설명합니다.
- `QA.md`: 어떤 테스트를 통과해야 하는지와 e2e 성공 기준을 정리합니다.
- `fixtures/`: hello 출력용 fixture와 mission 출력용 fixture를 함께 둡니다.
- `e2e/`: 언어별 미션 acceptance test 스크립트가 있습니다.

## 템플릿 기본 상태

- 이 토픽의 fresh template은 `make run`에서 `hello etl`를 출력합니다.
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
- 템플릿 기본 상태: `make -C rust run`은 `hello etl`를 출력합니다.
- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.
- 인자 위치 계약:
  - `argv[1]`: `input` (`예: ../fixtures/raw.csv`)
- Make 명령: `make -C rust build`, `make -C rust run`, `make -C rust test`, `make -C rust e2e`, `make -C rust smoke`
- 직접 실행 예시:
  - `source scripts/env.sh && cargo build --manifest-path topics/20-batch-etl-pipeline/rust/Cargo.toml`
  - `source scripts/env.sh && cargo run --manifest-path topics/20-batch-etl-pipeline/rust/Cargo.toml -- topics/20-batch-etl-pipeline/fixtures/raw.csv`
  - `./target/debug/t20_batch_etl_pipeline_rust topics/20-batch-etl-pipeline/fixtures/raw.csv`
- e2e 스크립트: `e2e/rust-smoke.sh`

### Python

- 핵심 로직: `python/src/t20_batch_etl_pipeline_python/core.py`
- CLI 진입점: `python/src/t20_batch_etl_pipeline_python/cli.py`
- 기본 테스트: `python/tests/test_topic.py`
- 패키지 설정: `python/pyproject.toml`
- 프로젝트 명령: `python/Makefile`
- 작성 방식: 순수 로직은 `core.py`, 파일 I/O와 인자 위치 정리는 `cli.py`에 두면 테스트하기 쉽다.
- 템플릿 기본 상태: `make -C python run`은 `hello etl`를 출력합니다.
- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.
- 인자 위치 계약:
  - `argv[1]`: `input` (`예: ../fixtures/raw.csv`)
- Make 명령: `make -C python run`, `make -C python test`, `make -C python e2e`, `make -C python smoke`
- 직접 실행 예시:
  - `source scripts/env.sh && PYTHONPATH=topics/20-batch-etl-pipeline/python/src "$PYTHON_BIN" -m t20_batch_etl_pipeline_python.cli topics/20-batch-etl-pipeline/fixtures/raw.csv`
- e2e 스크립트: `e2e/python-smoke.sh`

## Shell 보조 스크립트

- 시작 문서: `shell/README.md`
- 파이프라인 오케스트레이션이나 one-liner 검증 스크립트는 `shell/` 아래에 추가해서 관리하면 된다.

## 빠른 실행

- Rust: `make -C rust build`, `make -C rust run`, `make -C rust test`, `make -C rust e2e`, `make -C rust smoke`
- Python: `make -C python run`, `make -C python test`, `make -C python e2e`, `make -C python smoke`

## 문서

- `SPEC.md`
- `QA.md`

언어별 상세 직접 실행 예시는 각 언어 폴더의 `README.md`에도 정리되어 있습니다.
