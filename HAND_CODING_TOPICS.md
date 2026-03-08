# 손코딩 연습 주제 모음

        AI 보조 없이 감을 되찾고, 이후 데이터 분석과 병렬처리 업무까지 대비하기 위한 연습용 주제들이다. 기준은 다음과 같다.

        - 구현 범위가 손으로 끝까지 밀어붙이기 좋을 것
        - Rust를 메인으로 삼되, C++, Java, Kotlin, Python, SQL, 셸로도 확장 가능할 것
        - 문법 암기보다 설계, 디버깅, 자료구조 선택, 경계조건 처리, 데이터 검증 능력을 되살리는 데 도움이 될 것

        ## 추천 방식

        - 1차 구현: 검색 없이 60~90분 동안 밀어붙이기
        - 2차 구현: 테스트 추가, 리팩터링, 에러 처리 보강
        - 3차 구현: 다른 언어로 다시 옮기기
        - AI 사용은 마지막 회고 단계에서만 허용

        ## 우선순위 높은 주제

        ### 1. `grep` 비슷한 미니 텍스트 검색기

- 추천 언어: Rust, C++
- 핵심 훈련: 파일 I/O, 문자열 처리, CLI 인자 파싱, 에러 처리
- 최소 목표:
  - 파일 또는 stdin 입력 받기
  - 부분 문자열 검색
  - 줄 번호 출력
  - 대소문자 무시 옵션 추가
- 확장 목표:
  - 간단한 정규식 지원
  - 디렉터리 재귀 탐색
  - 매치된 부분 컬러 출력
- 손코딩 가치: 자잘한 경계조건이 많아서 디버깅 감각을 다시 끌어올리기 좋다.

        ### 2. 인메모리 `key-value store`

- 추천 언어: Rust, Java, Kotlin
- 핵심 훈련: 자료구조 설계, 명령 처리, 직렬화, 테스트 작성
- 최소 목표:
  - `SET`, `GET`, `DELETE`
  - TTL 또는 만료 시간
  - 스냅샷 저장/복원
- 확장 목표:
  - LRU 캐시 정책
  - append-only log
  - TCP 서버 모드
- 손코딩 가치: 작은 시스템 설계와 상태 전이를 연습하기 좋다.

        ### 3. HTTP 서버와 라우터 직접 만들기

- 추천 언어: Rust, Java, Kotlin
- 핵심 훈련: 네트워크, 바이트 파싱, 상태 관리, API 설계
- 최소 목표:
  - TCP 소켓으로 요청 받기
  - `GET /health`
  - `POST /echo`
  - 상태 코드와 헤더 처리
- 확장 목표:
  - 멀티스레드 처리
  - JSON body 파싱
  - 미들웨어 개념 추가
- 손코딩 가치: 프레임워크 없이 웹의 기본을 체득하기 좋다.

        ### 4. 간단한 `JSON parser`

- 추천 언어: Rust, C++, Java
- 핵심 훈련: 재귀 하강 파서, 토크나이징, 에러 메시지 설계
- 최소 목표:
  - 객체, 배열, 문자열, 숫자, 불리언, null 파싱
  - AST 또는 값 구조체 생성
- 확장 목표:
  - pretty printer
  - JSON path 조회
  - streaming parser
- 손코딩 가치: 파서 구현은 집중력과 구현 체력을 함께 끌어올린다.

        ### 5. 스레드 풀과 작업 큐

- 추천 언어: Rust, C++, Java
- 핵심 훈련: 동시성, 락, 작업 분배, 종료 처리
- 최소 목표:
  - 고정 크기 worker thread pool
  - 작업 제출 API
  - graceful shutdown
- 확장 목표:
  - future/promise 스타일 결과 반환
  - 우선순위 큐
  - work stealing 흉내내기
- 손코딩 가치: 언어별 동시성 모델 차이를 바로 체감할 수 있다.

        ## 언어별 추천 주제

        ### Rust 중심

        #### A. 미니 `git` 객체 저장소

- 추천 언어: Rust
- 핵심 훈련: 해시, 파일 포맷, 소유권, 바이너리 데이터 처리
- 최소 목표:
  - `init`
  - `hash-object`
  - `cat-file` 최소 흐름
  - blob 저장
- 확장 목표:
  - tree 비슷한 구조
  - commit 객체
  - 간단한 참조 관리
- 손코딩 가치: 파일 포맷과 저장소 설계 감각을 동시에 익히기 좋다.

        #### B. `arena allocator`

- 추천 언어: Rust
- 핵심 훈련: 메모리 모델 이해, 안전한 API 설계, 라이프타임 감각
- 최소 목표:
  - arena 타입
  - 객체 할당
  - clear/reset
  - 할당량 집계
- 확장 목표:
  - typed arena
  - bump allocator
  - unsafe 최적화
- 손코딩 가치: 메모리 관리 감각을 직접 되살리는 데 좋다.

        #### C. `tiny async executor`

- 추천 언어: Rust
- 핵심 훈련: poll, wake, task scheduling, future 상태 모델
- 최소 목표:
  - 단일 스레드 executor
  - `spawn`
  - `block_on` 데모
- 확장 목표:
  - timer future
  - wake queue
  - 작은 task scheduler
- 손코딩 가치: async의 내부 모델을 손으로 이해하기 좋다.

        ### C++ 중심

        #### A. 작은 벡터/문자열 클래스 구현

- 추천 언어: C++
- 핵심 훈련: RAII, move semantics, allocator 감각, 예외 안전성
- 최소 목표:
  - 생성자/복사/이동
  - push/pop
  - capacity 관리
- 확장 목표:
  - iterator
  - small buffer optimization
  - allocator 분리
- 손코딩 가치: C++ 기본기와 메모리 규율을 빠르게 점검할 수 있다.

        #### B. expression evaluator

- 추천 언어: C++
- 핵심 훈련: 토큰화, 파싱, 연산자 우선순위
- 최소 목표:
  - 괄호
  - `+ - * /`
  - 정수 계산
  - 에러 처리
- 확장 목표:
  - 단항 연산자
  - 변수
  - 함수 호출
- 손코딩 가치: 작은 파서와 평가기 구조를 손에 익히기 좋다.

        #### C. 파일 기반 로그 라이브러리

- 추천 언어: C++
- 핵심 훈련: 포맷팅, 버퍼링, 스레드 안전성, 회전 정책
- 최소 목표:
  - 로그 파일 출력
  - 회전 기준
  - 레벨 표시
  - flush
- 확장 목표:
  - 비동기 로깅
  - JSON 로그
  - 보존 정책
- 손코딩 가치: 실무에서 자주 만나는 I/O와 상태 전이를 연습할 수 있다.

        ### Java 중심

        #### A. 작은 dependency injection container

- 추천 언어: Java
- 핵심 훈련: reflection, annotation, 객체 생명주기
- 최소 목표:
  - 생성자 주입
  - singleton 지원
  - 순환 의존 감지
- 확장 목표:
  - named binding
  - lifecycle hook
  - scope 분리
- 손코딩 가치: 런타임 메타데이터와 객체 그래프 구성을 이해하기 좋다.

        #### B. 간단한 JDBC-backed todo app

- 추천 언어: Java
- 핵심 훈련: 계층 분리, 트랜잭션, 예외 처리
- 최소 목표:
  - CLI
  - CRUD
  - embedded DB 연결
  - 기본 쿼리
- 확장 목표:
  - 필터 검색
  - 간단한 REST API
  - migration
- 손코딩 가치: 실무형 데이터 접근 패턴을 손으로 정리하기 좋다.

        #### C. rate limiter

- 추천 언어: Java
- 핵심 훈련: 동시성, 시간 계산, API 설계
- 최소 목표:
  - token bucket
  - 허용/거절 판정
  - 버스트 처리
- 확장 목표:
  - sliding window
  - metrics
  - 분산 키별 limiter
- 손코딩 가치: 실무 API 보호 로직을 작은 범위로 연습하기 좋다.

        ### Kotlin 중심

        #### A. 코루틴 기반 작업 스케줄러

- 추천 언어: Kotlin
- 핵심 훈련: coroutine, channel, cancellation, structured concurrency
- 최소 목표:
  - 작업 등록
  - 지연 실행
  - 취소
  - 결과 수집
- 확장 목표:
  - priority
  - retry
  - backpressure
- 손코딩 가치: 현대 Kotlin 동시성 감각을 빠르게 되살릴 수 있다.

        #### B. 간단한 Kotlin/JVM 메모 앱

- 추천 언어: Kotlin
- 핵심 훈련: 상태 관리, 로컬 저장소, CLI UX
- 최소 목표:
  - 메모 추가
  - 목록 조회
  - 본문 보기
  - 검색
- 확장 목표:
  - 태그
  - 수정
  - 백업/복원
- 손코딩 가치: 파일 저장과 작은 도메인 모델을 손으로 다루기 좋다.

        #### C. DSL 스타일 설정 파서

- 추천 언어: Kotlin
- 핵심 훈련: Kotlin DSL 감각, parser combinator 사고, builder 패턴
- 최소 목표:
  - 블록
  - 키/값
  - 리스트
  - 정규화 출력
- 확장 목표:
  - 에러 위치
  - include
  - 환경변수 치환
- 손코딩 가치: 설정 언어 설계와 파싱 감각을 동시에 익히기 좋다.

        ## 데이터 분석 & 병렬처리 준비용 주제

        ### 18. dataset profiler

- 추천 언어: Rust, Python
- 핵심 훈련: CSV 처리, schema 추론, 기초 통계, 리포트 출력
- 최소 목표:
  - row 수
  - 컬럼 타입 후보
  - null count
  - min/max 또는 mean
- 확장 목표:
  - 분위수
  - 중복 탐지
  - 프로파일 JSON 출력
- 손코딩 가치: 데이터 입력을 빠르게 파악하는 실무 감각을 기르기 좋다.

### 19. mini group-by engine

- 추천 언어: Rust, Python, SQL
- 핵심 훈련: 집계, 정렬, key partitioning, 검증 기준선 만들기
- 최소 목표:
  - filter
  - group by
  - sum/count
  - 정렬된 출력
- 확장 목표:
  - 다중 key
  - 평균
  - top-N
- 손코딩 가치: 데이터 엔지니어링 업무의 가장 빈번한 흐름을 직접 만든다.

### 20. batch ETL pipeline

- 추천 언어: Rust, Python, Shell
- 핵심 훈련: 정제 규칙, reject 분리, 요약 리포트, 파이프라인 구성
- 최소 목표:
  - raw -> cleaned
  - invalid row reject
  - summary report
  - 종료 코드
- 확장 목표:
  - partition output
  - retry
  - 메트릭 파일
- 손코딩 가치: 업무형 배치 데이터 처리의 골격을 연습하기 좋다.

### 21. parallel log analyzer

- 추천 언어: Rust, Python, Shell
- 핵심 훈련: 병렬 파일 스캔, reduce, I/O 병목, speedup 비교
- 최소 목표:
  - status count
  - error count
  - top endpoint
  - single vs multi worker 비교
- 확장 목표:
  - 시간대별 집계
  - slow request 탐지
  - JSON 로그
- 손코딩 가치: 병렬 처리와 로그 분석을 동시에 체험하기 좋다.

### 22. external sort + merge

- 추천 언어: Rust, Python
- 핵심 훈련: chunking, 메모리 예산, merge, 스트리밍 I/O
- 최소 목표:
  - chunk sort
  - 임시 파일
  - k-way merge
  - 정렬 검증
- 확장 목표:
  - 복합 키
  - 압축
  - 메모리 사용량 로깅
- 손코딩 가치: 대용량 데이터 처리의 기본 패턴을 직접 익힐 수 있다.

### 23. windowed timeseries analyzer

- 추천 언어: Rust, Python, SQL
- 핵심 훈련: window aggregation, resample, 시계열 정렬, 검증 기준선
- 최소 목표:
  - tumbling window
  - rolling average
  - 정렬된 출력
  - 빈 구간 처리
- 확장 목표:
  - time zone
  - lag/lead
  - 이상치 탐지
- 손코딩 가치: 시계열 집계와 업무성 검증 루프를 손으로 익히기 좋다.

### 24. heavy hitter stream

- 추천 언어: Rust, Python
- 핵심 훈련: streaming aggregation, 근사 알고리즘, 오차 평가, top-k
- 최소 목표:
  - exact count
  - approximate heavy hitter
  - top-N 출력
  - 오차 요약
- 확장 목표:
  - Count-Min Sketch
  - 메모리 상한
  - 슬라이딩 윈도우
- 손코딩 가치: 스트리밍 사고방식과 근사 기법을 연습할 수 있다.

### 25. mini map-reduce on one machine

- 추천 언어: Rust, Python, Shell
- 핵심 훈련: map/shuffle/reduce, partitioning, worker orchestration, fault tolerance 흉내
- 최소 목표:
  - coordinator
  - worker
  - shuffle
  - baseline 결과 일치
- 확장 목표:
  - worker restart
  - skewed key
  - intermediate spill
- 손코딩 가치: 분산 처리 모델을 단일 머신에서 감각적으로 익히기 좋다.

        ## 난이도별 추천

        ### 가볍게 시작

        - 미니 텍스트 검색기
        - expression evaluator
        - JSON parser
        - dataset profiler
        - mini group-by engine

        ### 반나절 이상 붙잡기 좋은 주제

        - 인메모리 key-value store
        - HTTP 서버와 라우터
        - 스레드 풀과 작업 큐
        - JDBC-backed todo app
        - batch ETL pipeline
        - parallel log analyzer

        ### 깊게 파기 좋은 주제

        - 미니 git 객체 저장소
        - arena allocator
        - tiny async executor
        - coroutine 기반 스케줄러
        - external sort + merge
        - mini map-reduce

        ## 추천 조합

        ### 조합 1. 감 회복용 1주

        - Day 1: expression evaluator in C++
        - Day 2: JSON parser in Rust
        - Day 3: mini-grep in Rust
        - Day 4: rate limiter in Java
        - Day 5: 회고 및 재구현

        ### 조합 2. 시스템 감각 회복

        - Rust로 thread pool
        - Rust로 key-value store
        - C++로 tiny vector 또는 allocator

        ### 조합 3. 백엔드 감각 회복

        - Java 또는 Kotlin으로 HTTP 서버
        - Java로 DI container
        - Rust로 TCP 기반 key-value store

        ### 조합 4. 데이터 업무 입문 2주

        - Week 1: dataset profiler, mini group-by engine, batch ETL pipeline
        - Week 2: windowed timeseries analyzer, parallel log analyzer, heavy hitter stream

        ### 조합 5. 병렬처리 집중 1주

        - Day 1: thread pool and work queue
        - Day 2: coroutine scheduler
        - Day 3: parallel log analyzer
        - Day 4: external sort + merge
        - Day 5: mini map-reduce

        ### 조합 6. 분산 처리 맛보기 1주

        - Day 1: mini map-reduce baseline 구현
        - Day 2: worker partitioning
        - Day 3: shuffle / reduce 검증
        - Day 4: skewed key와 failure case
        - Day 5: 회고 및 성능 비교

        ## 개인적으로 특히 추천하는 5개

        1. Rust로 mini-grep
        2. Rust로 JSON parser
        3. Rust로 thread pool
        4. C++로 expression evaluator
        5. Java 또는 Kotlin으로 작은 HTTP 서버

        ## 데이터 업무용으로 특히 추천하는 6개

        1. Python 또는 Rust로 dataset profiler
        2. Python 또는 Rust로 mini group-by engine
        3. Rust로 parallel log analyzer
        4. Python으로 batch ETL pipeline
        5. Rust 또는 Python으로 windowed timeseries analyzer
        6. Rust 또는 Python으로 mini map-reduce

        ## 연습할 때 일부러 넣으면 좋은 제약

        - 라이브러리 최소화
        - 자동완성 없이 시작
        - 테스트를 먼저 3개 이상 작성
        - 예외 상황 10개를 직접 적고 구현
        - 구현 후 다른 언어로 한 번 더 옮기기
        - 성능 측정 포인트를 최소 1개 넣기
        - 메모리 예산을 미리 정하고 지키기
        - single-thread 기준선과 multi-worker 결과를 반드시 비교하기
        - 데이터 skew와 파티셔닝 전략을 회고에 남기기

        ## 회고 질문

        - 어디서 가장 오래 막혔는가
        - 자료구조 선택이 적절했는가
        - 테스트가 버그를 실제로 잡았는가
        - 언어 특성이 설계에 어떤 영향을 줬는가
        - 메모리 예산과 I/O 병목은 어땠는가
        - single-thread 대비 speedup은 의미 있었는가
        - 다시 구현하면 무엇을 먼저 바꿀 것인가

        ## 다음 단계

        1. Rust: mini-grep
        2. Rust: JSON parser
        3. C++: expression evaluator
        4. Java 또는 Kotlin: HTTP 서버
        5. Python: dataset profiler
        6. Rust 또는 Python: mini group-by engine
        7. Rust: key-value store
        8. Rust 또는 Python: parallel log analyzer
