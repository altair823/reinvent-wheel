# SPEC: 01. `grep` 비슷한 미니 텍스트 검색기

## 템플릿 baseline

- fresh template의 `make run` 출력은 `hello grep`입니다.
- 이 baseline은 시작점일 뿐이며, 아래 요구사항 전체를 만족하지는 않습니다.
- `make smoke`는 baseline 실행 가능 여부를 확인하고, `make e2e`는 아래 미션 성공 기준을 검증합니다.

## 요구사항

1. 프로그램은 `mini-grep` 토픽의 mission fixture를 처리하고 결정적인 결과를 출력해야 합니다.
2. 프로젝트는 `make run`, `make test`, `make e2e`, `make smoke`를 지원해야 합니다.
3. Rust, C++, Java, Kotlin 프로젝트는 `make build`도 지원해야 합니다.
4. 핵심 로직은 `src` 아래 라이브러리/모듈로 분리하고 테스트에서 직접 호출 가능해야 합니다.
5. 예외 입력 또는 실패 시나리오를 최소 하나 이상 테스트로 검증해야 합니다.
6. 입력 파일 경로와 쿼리를 받을 수 있어야 합니다.
7. 파일 내용에서 일치하는 줄과 줄 번호를 출력해야 합니다.

## 비목표

- 지금 단계에서 production 완성본을 만들지 않습니다.
- fresh template은 최소 실행 골격만 제공하며, 최종 미션 구현은 사용자가 채워 넣습니다.

## Stretch Goal

- 간단한 정규식 지원; 디렉터리 재귀 탐색; 매치된 부분 컬러 출력
