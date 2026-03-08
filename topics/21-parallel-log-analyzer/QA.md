# QA: 21. parallel log analyzer

## Template Baseline

- `make run`이 `hello log-analyzer`를 출력해야 한다.
- `make smoke`는 이 baseline만 확인한다.
- fresh template 상태에서 `make e2e`는 실패해도 정상이다.

## Unit

- 핵심 함수가 비어 있지 않고 직접 호출 가능하다.
- 최소 hello 경로 또는 작은 보조 함수가 테스트로 고정돼 있다.
- 미션 구현 중에는 경계조건 테스트를 여기에 추가한다.

## Integration

- `make run` 또는 서버 기동이 baseline 수준에서 동작한다.
- `make test`는 최소 구조 검증 또는 보조 단위 테스트를 제공한다.
- `make e2e`가 최종 미션 acceptance test를 수행한다.

## Mission Success

- `e2e/*.sh`가 `fixtures/mission-expected.txt`와 실제 출력을 비교한다.

## Failure Cases

- 존재하지 않는 입력 파일 경로를 전달했을 때 오류를 반환한다.
- 잘못된 포맷 또는 잘못된 명령이 테스트 또는 e2e에서 고정돼 있다.
- 출력 순서가 불안정해지지 않도록 정렬 또는 안정화 규칙을 가진다.
- single-thread 기준 결과와 병렬 결과를 비교하는 체크가 있다.

## Manual Smoke

- fixture를 기준으로 결과가 deterministic 한지 확인한다.
- README 명령을 그대로 실행해도 동일한 결과가 나오는지 확인한다.
- 출력 파일 또는 서버 응답이 expected fixture와 같은지 확인한다.
