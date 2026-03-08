from __future__ import annotations

import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

LANG_LABELS = {
    "rust": "Rust",
    "cpp": "C++",
    "java": "Java",
    "kotlin": "Kotlin",
    "python": "Python",
}

TOPICS = [
    {
        "num": 1,
        "slug": "mini-grep",
        "title": "`grep` 비슷한 미니 텍스트 검색기",
        "category": "general",
        "languages": ["rust", "cpp"],
        "kind": "mini_grep",
        "recommended": ["Rust", "C++"],
        "training": ["파일 I/O", "문자열 처리", "CLI 인자 파싱", "에러 처리"],
        "minimum": ["파일 또는 stdin 입력 받기", "부분 문자열 검색", "줄 번호 출력", "대소문자 무시 옵션 추가"],
        "stretch": ["간단한 정규식 지원", "디렉터리 재귀 탐색", "매치된 부분 컬러 출력"],
        "value": "자잘한 경계조건이 많아서 디버깅 감각을 다시 끌어올리기 좋다.",
    },
    {
        "num": 2,
        "slug": "key-value-store",
        "title": "인메모리 `key-value store`",
        "category": "general",
        "languages": ["rust", "java", "kotlin"],
        "kind": "key_value_store",
        "recommended": ["Rust", "Java", "Kotlin"],
        "training": ["자료구조 설계", "명령 처리", "직렬화", "테스트 작성"],
        "minimum": ["`SET`, `GET`, `DELETE`", "TTL 또는 만료 시간", "스냅샷 저장/복원"],
        "stretch": ["LRU 캐시 정책", "append-only log", "TCP 서버 모드"],
        "value": "작은 시스템 설계와 상태 전이를 연습하기 좋다.",
    },
    {
        "num": 3,
        "slug": "http-server-router",
        "title": "HTTP 서버와 라우터 직접 만들기",
        "category": "general",
        "languages": ["rust", "java", "kotlin"],
        "kind": "http_server_router",
        "recommended": ["Rust", "Java", "Kotlin"],
        "training": ["네트워크", "바이트 파싱", "상태 관리", "API 설계"],
        "minimum": ["TCP 소켓으로 요청 받기", "`GET /health`", "`POST /echo`", "상태 코드와 헤더 처리"],
        "stretch": ["멀티스레드 처리", "JSON body 파싱", "미들웨어 개념 추가"],
        "value": "프레임워크 없이 웹의 기본을 체득하기 좋다.",
    },
    {
        "num": 4,
        "slug": "json-parser",
        "title": "간단한 `JSON parser`",
        "category": "general",
        "languages": ["rust", "cpp", "java"],
        "kind": "json_parser",
        "recommended": ["Rust", "C++", "Java"],
        "training": ["재귀 하강 파서", "토크나이징", "에러 메시지 설계"],
        "minimum": ["객체, 배열, 문자열, 숫자, 불리언, null 파싱", "AST 또는 값 구조체 생성"],
        "stretch": ["pretty printer", "JSON path 조회", "streaming parser"],
        "value": "파서 구현은 집중력과 구현 체력을 함께 끌어올린다.",
    },
    {
        "num": 5,
        "slug": "thread-pool-queue",
        "title": "스레드 풀과 작업 큐",
        "category": "general",
        "languages": ["rust", "cpp", "java"],
        "kind": "thread_pool_queue",
        "recommended": ["Rust", "C++", "Java"],
        "training": ["동시성", "락", "작업 분배", "종료 처리"],
        "minimum": ["고정 크기 worker thread pool", "작업 제출 API", "graceful shutdown"],
        "stretch": ["future/promise 스타일 결과 반환", "우선순위 큐", "work stealing 흉내내기"],
        "value": "언어별 동시성 모델 차이를 바로 체감할 수 있다.",
    },
    {
        "num": 6,
        "slug": "mini-git-object-store",
        "title": "미니 `git` 객체 저장소",
        "category": "rust",
        "languages": ["rust"],
        "kind": "mini_git_object_store",
        "recommended": ["Rust"],
        "training": ["해시", "파일 포맷", "소유권", "바이너리 데이터 처리"],
        "minimum": ["`init`", "`hash-object`", "`cat-file` 최소 흐름", "blob 저장"],
        "stretch": ["tree 비슷한 구조", "commit 객체", "간단한 참조 관리"],
        "value": "파일 포맷과 저장소 설계 감각을 동시에 익히기 좋다.",
    },
    {
        "num": 7,
        "slug": "arena-allocator",
        "title": "`arena allocator`",
        "category": "rust",
        "languages": ["rust"],
        "kind": "arena_allocator",
        "recommended": ["Rust"],
        "training": ["메모리 모델 이해", "안전한 API 설계", "라이프타임 감각"],
        "minimum": ["arena 타입", "객체 할당", "clear/reset", "할당량 집계"],
        "stretch": ["typed arena", "bump allocator", "unsafe 최적화"],
        "value": "메모리 관리 감각을 직접 되살리는 데 좋다.",
    },
    {
        "num": 8,
        "slug": "tiny-async-executor",
        "title": "`tiny async executor`",
        "category": "rust",
        "languages": ["rust"],
        "kind": "tiny_async_executor",
        "recommended": ["Rust"],
        "training": ["poll", "wake", "task scheduling", "future 상태 모델"],
        "minimum": ["단일 스레드 executor", "`spawn`", "`block_on` 데모"],
        "stretch": ["timer future", "wake queue", "작은 task scheduler"],
        "value": "async의 내부 모델을 손으로 이해하기 좋다.",
    },
    {
        "num": 9,
        "slug": "tiny-vector",
        "title": "작은 벡터/문자열 클래스 구현",
        "category": "cpp",
        "languages": ["cpp"],
        "kind": "tiny_vector",
        "recommended": ["C++"],
        "training": ["RAII", "move semantics", "allocator 감각", "예외 안전성"],
        "minimum": ["생성자/복사/이동", "push/pop", "capacity 관리"],
        "stretch": ["iterator", "small buffer optimization", "allocator 분리"],
        "value": "C++ 기본기와 메모리 규율을 빠르게 점검할 수 있다.",
    },
    {
        "num": 10,
        "slug": "expression-evaluator",
        "title": "expression evaluator",
        "category": "cpp",
        "languages": ["cpp"],
        "kind": "expression_evaluator",
        "recommended": ["C++"],
        "training": ["토큰화", "파싱", "연산자 우선순위"],
        "minimum": ["괄호", "`+ - * /`", "정수 계산", "에러 처리"],
        "stretch": ["단항 연산자", "변수", "함수 호출"],
        "value": "작은 파서와 평가기 구조를 손에 익히기 좋다.",
    },
    {
        "num": 11,
        "slug": "file-log-library",
        "title": "파일 기반 로그 라이브러리",
        "category": "cpp",
        "languages": ["cpp"],
        "kind": "file_log_library",
        "recommended": ["C++"],
        "training": ["포맷팅", "버퍼링", "스레드 안전성", "회전 정책"],
        "minimum": ["로그 파일 출력", "회전 기준", "레벨 표시", "flush"],
        "stretch": ["비동기 로깅", "JSON 로그", "보존 정책"],
        "value": "실무에서 자주 만나는 I/O와 상태 전이를 연습할 수 있다.",
    },
    {
        "num": 12,
        "slug": "di-container",
        "title": "작은 dependency injection container",
        "category": "java",
        "languages": ["java"],
        "kind": "di_container",
        "recommended": ["Java"],
        "training": ["reflection", "annotation", "객체 생명주기"],
        "minimum": ["생성자 주입", "singleton 지원", "순환 의존 감지"],
        "stretch": ["named binding", "lifecycle hook", "scope 분리"],
        "value": "런타임 메타데이터와 객체 그래프 구성을 이해하기 좋다.",
    },
    {
        "num": 13,
        "slug": "jdbc-todo-cli",
        "title": "간단한 JDBC-backed todo app",
        "category": "java",
        "languages": ["java"],
        "kind": "jdbc_todo_cli",
        "recommended": ["Java"],
        "training": ["계층 분리", "트랜잭션", "예외 처리"],
        "minimum": ["CLI", "CRUD", "embedded DB 연결", "기본 쿼리"],
        "stretch": ["필터 검색", "간단한 REST API", "migration"],
        "value": "실무형 데이터 접근 패턴을 손으로 정리하기 좋다.",
    },
    {
        "num": 14,
        "slug": "rate-limiter",
        "title": "rate limiter",
        "category": "java",
        "languages": ["java"],
        "kind": "rate_limiter",
        "recommended": ["Java"],
        "training": ["동시성", "시간 계산", "API 설계"],
        "minimum": ["token bucket", "허용/거절 판정", "버스트 처리"],
        "stretch": ["sliding window", "metrics", "분산 키별 limiter"],
        "value": "실무 API 보호 로직을 작은 범위로 연습하기 좋다.",
    },
    {
        "num": 15,
        "slug": "coroutine-scheduler",
        "title": "코루틴 기반 작업 스케줄러",
        "category": "kotlin",
        "languages": ["kotlin"],
        "kind": "coroutine_scheduler",
        "recommended": ["Kotlin"],
        "training": ["coroutine", "channel", "cancellation", "structured concurrency"],
        "minimum": ["작업 등록", "지연 실행", "취소", "결과 수집"],
        "stretch": ["priority", "retry", "backpressure"],
        "value": "현대 Kotlin 동시성 감각을 빠르게 되살릴 수 있다.",
    },
    {
        "num": 16,
        "slug": "notes-app-jvm",
        "title": "간단한 Kotlin/JVM 메모 앱",
        "category": "kotlin",
        "languages": ["kotlin"],
        "kind": "notes_app_jvm",
        "recommended": ["Kotlin"],
        "training": ["상태 관리", "로컬 저장소", "CLI UX"],
        "minimum": ["메모 추가", "목록 조회", "본문 보기", "검색"],
        "stretch": ["태그", "수정", "백업/복원"],
        "value": "파일 저장과 작은 도메인 모델을 손으로 다루기 좋다.",
    },
    {
        "num": 17,
        "slug": "dsl-config-parser",
        "title": "DSL 스타일 설정 파서",
        "category": "kotlin",
        "languages": ["kotlin"],
        "kind": "dsl_config_parser",
        "recommended": ["Kotlin"],
        "training": ["Kotlin DSL 감각", "parser combinator 사고", "builder 패턴"],
        "minimum": ["블록", "키/값", "리스트", "정규화 출력"],
        "stretch": ["에러 위치", "include", "환경변수 치환"],
        "value": "설정 언어 설계와 파싱 감각을 동시에 익히기 좋다.",
    },
    {
        "num": 18,
        "slug": "dataset-profiler",
        "title": "dataset profiler",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "dataset_profiler",
        "recommended": ["Rust", "Python"],
        "training": ["CSV 처리", "schema 추론", "기초 통계", "리포트 출력"],
        "minimum": ["row 수", "컬럼 타입 후보", "null count", "min/max 또는 mean"],
        "stretch": ["분위수", "중복 탐지", "프로파일 JSON 출력"],
        "value": "데이터 입력을 빠르게 파악하는 실무 감각을 기르기 좋다.",
    },
    {
        "num": 19,
        "slug": "mini-groupby-engine",
        "title": "mini group-by engine",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "mini_groupby_engine",
        "recommended": ["Rust", "Python", "SQL"],
        "training": ["집계", "정렬", "key partitioning", "검증 기준선 만들기"],
        "minimum": ["filter", "group by", "sum/count", "정렬된 출력"],
        "stretch": ["다중 key", "평균", "top-N"],
        "value": "데이터 엔지니어링 업무의 가장 빈번한 흐름을 직접 만든다.",
    },
    {
        "num": 20,
        "slug": "batch-etl-pipeline",
        "title": "batch ETL pipeline",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "batch_etl_pipeline",
        "recommended": ["Rust", "Python", "Shell"],
        "training": ["정제 규칙", "reject 분리", "요약 리포트", "파이프라인 구성"],
        "minimum": ["raw -> cleaned", "invalid row reject", "summary report", "종료 코드"],
        "stretch": ["partition output", "retry", "메트릭 파일"],
        "value": "업무형 배치 데이터 처리의 골격을 연습하기 좋다.",
    },
    {
        "num": 21,
        "slug": "parallel-log-analyzer",
        "title": "parallel log analyzer",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "parallel_log_analyzer",
        "recommended": ["Rust", "Python", "Shell"],
        "training": ["병렬 파일 스캔", "reduce", "I/O 병목", "speedup 비교"],
        "minimum": ["status count", "error count", "top endpoint", "single vs multi worker 비교"],
        "stretch": ["시간대별 집계", "slow request 탐지", "JSON 로그"],
        "value": "병렬 처리와 로그 분석을 동시에 체험하기 좋다.",
    },
    {
        "num": 22,
        "slug": "external-sort-merge",
        "title": "external sort + merge",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "external_sort_merge",
        "recommended": ["Rust", "Python"],
        "training": ["chunking", "메모리 예산", "merge", "스트리밍 I/O"],
        "minimum": ["chunk sort", "임시 파일", "k-way merge", "정렬 검증"],
        "stretch": ["복합 키", "압축", "메모리 사용량 로깅"],
        "value": "대용량 데이터 처리의 기본 패턴을 직접 익힐 수 있다.",
    },
    {
        "num": 23,
        "slug": "windowed-timeseries-analyzer",
        "title": "windowed timeseries analyzer",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "windowed_timeseries_analyzer",
        "recommended": ["Rust", "Python", "SQL"],
        "training": ["window aggregation", "resample", "시계열 정렬", "검증 기준선"],
        "minimum": ["tumbling window", "rolling average", "정렬된 출력", "빈 구간 처리"],
        "stretch": ["time zone", "lag/lead", "이상치 탐지"],
        "value": "시계열 집계와 업무성 검증 루프를 손으로 익히기 좋다.",
    },
    {
        "num": 24,
        "slug": "heavy-hitter-stream",
        "title": "heavy hitter stream",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "heavy_hitter_stream",
        "recommended": ["Rust", "Python"],
        "training": ["streaming aggregation", "근사 알고리즘", "오차 평가", "top-k"],
        "minimum": ["exact count", "approximate heavy hitter", "top-N 출력", "오차 요약"],
        "stretch": ["Count-Min Sketch", "메모리 상한", "슬라이딩 윈도우"],
        "value": "스트리밍 사고방식과 근사 기법을 연습할 수 있다.",
    },
    {
        "num": 25,
        "slug": "mini-mapreduce",
        "title": "mini map-reduce on one machine",
        "category": "data",
        "languages": ["rust", "python"],
        "kind": "mini_mapreduce",
        "recommended": ["Rust", "Python", "Shell"],
        "training": ["map/shuffle/reduce", "partitioning", "worker orchestration", "fault tolerance 흉내"],
        "minimum": ["coordinator", "worker", "shuffle", "baseline 결과 일치"],
        "stretch": ["worker restart", "skewed key", "intermediate spill"],
        "value": "분산 처리 모델을 단일 머신에서 감각적으로 익히기 좋다.",
    },
]


def text(value: str) -> str:
    return textwrap.dedent(value).strip() + "\n"


def slug_to_identifier(slug: str) -> str:
    return slug.replace("-", "_")


def project_name(topic: dict, language: str) -> str:
    return f"t{topic['num']:02d}_{slug_to_identifier(topic['slug'])}_{language}"


def gradle_path(topic: dict, language: str) -> str:
    return f"t{topic['num']:02d}-{topic['slug']}-{language}"


def topic_dir(topic: dict) -> Path:
    return ROOT / "topics" / f"{topic['num']:02d}-{topic['slug']}"


def class_name(topic: dict) -> str:
    return "".join(part.capitalize() for part in topic["slug"].split("-")) + "App"


def java_package(topic: dict) -> str:
    return f"dev.reinvent.wheel.t{topic['num']:02d}"


def language_write_hint(language: str) -> str:
    hints = {
        "rust": "핵심 로직은 `lib.rs`에 두고 `main.rs`는 인자 파싱과 출력만 담당하게 두는 편이 좋다.",
        "cpp": "`include/topic.hpp`에 인터페이스를 고정하고 `src/lib.cpp`에 구현을 모아두면 정리하기 쉽다.",
        "java": "`src/main/java`의 `*App.java`를 시작점으로 두고, 구현이 커지면 같은 패키지 아래 클래스를 추가하는 방식이 무난하다.",
        "kotlin": "`src/main/kotlin`의 `*App.kt`를 시작점으로 두고, 로직이 커지면 같은 패키지에 파일을 나눠 추가하면 된다.",
        "python": "순수 로직은 `core.py`, 파일 I/O와 인자 위치 정리는 `cli.py`에 두면 테스트하기 쉽다.",
    }
    return hints[language]


def hello_output(topic: dict) -> str:
    mapping = {
        "mini_grep": "hello grep\n",
        "key_value_store": "hello kv-store\n",
        "json_parser": "hello json\n",
        "thread_pool_queue": "hello thread-pool\n",
        "mini_git_object_store": "hello git-object\n",
        "arena_allocator": "hello arena\n",
        "tiny_async_executor": "hello async\n",
        "tiny_vector": "hello vector\n",
        "expression_evaluator": "hello expr\n",
        "file_log_library": "hello log\n",
        "di_container": "hello di\n",
        "jdbc_todo_cli": "hello todo\n",
        "rate_limiter": "hello rate-limiter\n",
        "coroutine_scheduler": "hello coroutine\n",
        "notes_app_jvm": "hello notes\n",
        "dsl_config_parser": "hello dsl\n",
        "dataset_profiler": "hello profiler\n",
        "mini_groupby_engine": "hello groupby\n",
        "batch_etl_pipeline": "hello etl\n",
        "parallel_log_analyzer": "hello log-analyzer\n",
        "external_sort_merge": "hello sort\n",
        "windowed_timeseries_analyzer": "hello timeseries\n",
        "heavy_hitter_stream": "hello heavy-hitter\n",
        "mini_mapreduce": "hello mapreduce\n",
    }
    if topic["kind"] == "http_server_router":
        raise ValueError("HTTP topic uses a minimal server instead of a text hello output.")
    return mapping[topic["kind"]]


def mission_output(topic: dict) -> str:
    mapping = {
        "mini_grep": "1: Rust makes it easy to build tools.\n3: Rust and C++ can coexist.\n",
        "key_value_store": "language=Rust\nsnapshot=language=Rust\n",
        "json_parser": "tokens=26\nkeys=name,count,active,items\n",
        "thread_pool_queue": "workers=2\nresults=1,4,9,16\n",
        "mini_git_object_store": "id=77309518b87a501c\nhello-git-object\n",
        "arena_allocator": "allocations=3\nbytes=14\n",
        "tiny_async_executor": "completed=fetch-metrics,flush-cache\n",
        "tiny_vector": "size=3 capacity=4 last=13\n",
        "expression_evaluator": "result=5\n",
        "file_log_library": "written=3 rotated=1\n",
        "di_container": "resolved=Controller->Service->Database\n",
        "jdbc_todo_cli": "todos=2 done=0\n",
        "rate_limiter": "allowed=3 denied=1\n",
        "coroutine_scheduler": "completed=collect,transform,publish\n",
        "notes_app_jvm": "notes=2 first=Rust ideas\n",
        "dsl_config_parser": "server.port=8080\nfeatures=search,metrics\n",
        "dataset_profiler": "rows=3\ncount_nulls=1\nratio_mean=0.433\n",
        "mini_groupby_engine": "blue,13,2\nred,10,1\n",
        "batch_etl_pipeline": "cleaned=2 rejected=2 total_score=19\n",
        "parallel_log_analyzer": "200=2\n404=1\n500=2\ntop=/echo\n",
        "external_sort_merge": "1\n2\n3\n5\n7\n9\n",
        "windowed_timeseries_analyzer": "2026-03-01T10:00,30,15.000\n2026-03-01T11:00,5,11.667\n",
        "heavy_hitter_stream": "exact=red:3,blue:2\napprox=red,blue\n",
        "mini_mapreduce": "data=1\npython=2\nrust=3\n",
    }
    if topic["kind"] == "http_server_router":
        raise ValueError("HTTP topic uses curl-based mission checks instead of mission-expected.txt.")
    return mapping[topic["kind"]]


def fixture_path(topic: dict, name: str, scope: str) -> str:
    if scope == "project":
        return f"../fixtures/{name}"
    if scope == "root":
        return f"topics/{topic['num']:02d}-{topic['slug']}/fixtures/{name}"
    raise ValueError(scope)


def cli_options(topic: dict, scope: str = "project") -> list[dict[str, object]]:
    fixture = fixture_path
    if topic["kind"] == "http_server_router":
        return [{"name": "port", "type": "int", "default": 18080, "required": False}]
    if topic["kind"] == "mini_grep":
        return [
            {"name": "input", "type": "path", "value": fixture(topic, "sample.txt", scope), "required": True},
            {"name": "query", "type": "string", "value": "Rust", "required": True},
        ]
    if topic["kind"] == "parallel_log_analyzer":
        return [
            {"name": "input", "type": "path", "value": fixture(topic, "app.log", scope), "required": True},
            {"name": "workers", "type": "int", "default": 2, "required": False},
        ]
    if topic["kind"] == "key_value_store":
        return [{"name": "input", "type": "path", "value": fixture(topic, "commands.txt", scope), "required": True}]
    if topic["kind"] == "thread_pool_queue":
        return [{"name": "input", "type": "path", "value": fixture(topic, "tasks.txt", scope), "required": True}]

    fixture_by_kind = {
        "json_parser": "sample.json",
        "mini_git_object_store": "blob.txt",
        "arena_allocator": "words.txt",
        "tiny_async_executor": "tasks.txt",
        "tiny_vector": "values.txt",
        "expression_evaluator": "expressions.txt",
        "file_log_library": "events.txt",
        "jdbc_todo_cli": "todos.txt",
        "rate_limiter": "requests.txt",
        "coroutine_scheduler": "jobs.txt",
        "notes_app_jvm": "notes.txt",
        "dsl_config_parser": "sample.dsl",
        "dataset_profiler": "sample.csv",
        "mini_groupby_engine": "sales.csv",
        "batch_etl_pipeline": "raw.csv",
        "external_sort_merge": "numbers.txt",
        "windowed_timeseries_analyzer": "series.csv",
        "heavy_hitter_stream": "events.txt",
        "mini_mapreduce": "documents.txt",
    }
    fixture_name = fixture_by_kind.get(topic["kind"])
    if fixture_name is None:
        return []
    return [{"name": "input", "type": "path", "value": fixture(topic, fixture_name, scope), "required": True}]


def argv_contract(topic: dict, scope: str = "project") -> list[str]:
    lines: list[str] = []
    for index, option in enumerate(cli_options(topic, scope), start=1):
        sample = option.get("value", option.get("default"))
        if option.get("required", True):
            lines.append(f"`argv[{index}]`: `{option['name']}` (`예: {sample}`)")
        else:
            lines.append(f"`argv[{index}]`: 선택 사항 `{option['name']}` (`기본값: {sample}`)")
    if not lines:
        lines.append("이 템플릿은 커맨드라인 인자를 받지 않습니다.")
    return lines


def run_args_for(topic: dict, language: str, scope: str = "project") -> str:
    parts: list[str] = []
    for option in cli_options(topic, scope):
        if option["type"] == "int":
            if option["name"] == "port":
                continue
            parts.append(str(option["default"]))
        else:
            parts.append(str(option["value"]))
    return " ".join(parts)


def make_targets_for(language: str, in_topic: bool) -> list[str]:
    prefix = f"make -C {language}" if in_topic else "make"
    commands = []
    if language != "python":
        commands.append(f"`{prefix} build`")
    commands.extend(
        [
            f"`{prefix} run`",
            f"`{prefix} test`",
            f"`{prefix} e2e`",
            f"`{prefix} smoke`",
        ]
    )
    return commands


def direct_commands_for(topic: dict, language: str) -> list[str]:
    root_topic = f"topics/{topic['num']:02d}-{topic['slug']}"
    args = run_args_for(topic, language, scope="root")
    if language == "rust":
        commands = [
            f"`source scripts/env.sh && cargo build --manifest-path {root_topic}/rust/Cargo.toml`",
            f"`source scripts/env.sh && cargo run --manifest-path {root_topic}/rust/Cargo.toml"
            + (f" -- {args}`" if args else "`"),
            f"`./target/debug/{project_name(topic, 'rust')}"
            + (f" {args}`" if args else "`"),
        ]
        return commands
    if language == "cpp":
        commands = [
            f"`make -C {root_topic}/cpp build`",
            f"`{root_topic}/cpp/bin/{project_name(topic, 'cpp')}"
            + (f" {args}`" if args else "`"),
        ]
        return commands
    if language == "java":
        run = f"`source scripts/env.sh && ./gradlew -q :{gradle_path(topic, 'java')}:run"
        if args:
            run += f" --args='{args}'"
        run += "`"
        return [
            f"`source scripts/env.sh && ./gradlew :{gradle_path(topic, 'java')}:installDist`",
            run,
            f"`source scripts/env.sh && {root_topic}/java/build/install/{gradle_path(topic, 'java')}/bin/{gradle_path(topic, 'java')}"
            + (f" {args}`" if args else "`"),
        ]
    if language == "kotlin":
        run = f"`source scripts/env.sh && ./gradlew -q :{gradle_path(topic, 'kotlin')}:run"
        if args:
            run += f" --args='{args}'"
        run += "`"
        return [
            f"`source scripts/env.sh && ./gradlew :{gradle_path(topic, 'kotlin')}:installDist`",
            run,
            f"`source scripts/env.sh && {root_topic}/kotlin/build/install/{gradle_path(topic, 'kotlin')}/bin/{gradle_path(topic, 'kotlin')}"
            + (f" {args}`" if args else "`"),
        ]
    if language == "python":
        return [
            f"`source scripts/env.sh && PYTHONPATH={root_topic}/python/src \"$PYTHON_BIN\" -m {project_name(topic, 'python')}.cli {args}`"
        ]
    raise ValueError(language)


def topic_language_files(topic: dict, language: str) -> list[tuple[str, str]]:
    if language == "rust":
        return [
            ("핵심 로직", "rust/src/lib.rs"),
            ("CLI 진입점", "rust/src/main.rs"),
            ("기본 테스트", "rust/tests/smoke.rs"),
            ("프로젝트 명령", "rust/Makefile"),
        ]
    if language == "cpp":
        return [
            ("공개 인터페이스", "cpp/include/topic.hpp"),
            ("핵심 로직", "cpp/src/lib.cpp"),
            ("CLI 진입점", "cpp/src/main.cpp"),
            ("기본 테스트", "cpp/tests/test_main.cpp"),
            ("프로젝트 명령", "cpp/Makefile"),
        ]
    if language == "java":
        package_path = java_package(topic).replace(".", "/")
        app = class_name(topic)
        return [
            ("핵심 로직/앱", f"java/src/main/java/{package_path}/{app}.java"),
            ("기본 테스트", f"java/src/test/java/{package_path}/{app}Test.java"),
            ("프로젝트 설정", "java/build.gradle.kts"),
            ("프로젝트 명령", "java/Makefile"),
        ]
    if language == "kotlin":
        package_path = java_package(topic).replace(".", "/")
        app = class_name(topic)
        return [
            ("핵심 로직/앱", f"kotlin/src/main/kotlin/{package_path}/{app}.kt"),
            ("기본 테스트", f"kotlin/src/test/kotlin/{package_path}/{app}Test.kt"),
            ("프로젝트 설정", "kotlin/build.gradle.kts"),
            ("프로젝트 명령", "kotlin/Makefile"),
        ]
    if language == "python":
        package_name = project_name(topic, "python")
        return [
            ("핵심 로직", f"python/src/{package_name}/core.py"),
            ("CLI 진입점", f"python/src/{package_name}/cli.py"),
            ("기본 테스트", "python/tests/test_topic.py"),
            ("패키지 설정", "python/pyproject.toml"),
            ("프로젝트 명령", "python/Makefile"),
        ]
    raise ValueError(language)


def topic_language_commands(language: str, in_topic: bool) -> list[str]:
    return make_targets_for(language, in_topic)


def render_topic_language_section(topic: dict, language: str) -> list[str]:
    lines = [f"### {LANG_LABELS[language]}", ""]
    for label, path in topic_language_files(topic, language):
        lines.append(f"- {label}: `{path}`")
    lines.append(f"- 작성 방식: {language_write_hint(language)}")
    if topic["kind"] == "http_server_router":
        lines.append("- 템플릿 기본 상태: 작은 실제 HTTP 서버가 `GET /health`와 `POST /echo`만 처리합니다.")
    else:
        lines.append(f"- 템플릿 기본 상태: `make -C {language} run`은 `{hello_output(topic).strip()}`를 출력합니다.")
    lines.append("- CLI 스캐폴드: 템플릿 진입점이 `argv` 위치 계약만 이미 고정해 두므로, 보통은 라이브러리/코어 로직 구현에만 집중하면 됩니다.")
    lines.append("- 인자 위치 계약:")
    for contract in argv_contract(topic, scope="project"):
        lines.append(f"  - {contract}")
    lines.append(f"- Make 명령: {', '.join(topic_language_commands(language, in_topic=True))}")
    lines.append("- 직접 실행 예시:")
    for command in direct_commands_for(topic, language):
        lines.append(f"  - {command}")
    lines.append(f"- e2e 스크립트: `e2e/{language}-smoke.sh`")
    return lines


def render_support_sections(topic: dict) -> list[str]:
    lines: list[str] = []
    if topic["kind"] in {"mini_groupby_engine", "windowed_timeseries_analyzer"}:
        lines.extend(
            [
                "",
                "## SQL 기준선",
                "",
                "- 비교용 쿼리: `sql/query.sql`",
                "- Rust/Python 결과가 맞는지 확인할 때 기준선으로 사용한다.",
            ]
        )
    if topic["kind"] in {"batch_etl_pipeline", "parallel_log_analyzer", "mini_mapreduce"}:
        lines.extend(
            [
                "",
                "## Shell 보조 스크립트",
                "",
                "- 시작 문서: `shell/README.md`",
                "- 파이프라인 오케스트레이션이나 one-liner 검증 스크립트는 `shell/` 아래에 추가해서 관리하면 된다.",
            ]
        )
    return lines


def render_topic_section(topic: dict, heading: str) -> str:
    lines = [heading, "", f"- 추천 언어: {', '.join(topic['recommended'])}", f"- 핵심 훈련: {', '.join(topic['training'])}", "- 최소 목표:"]
    lines.extend([f"  - {item}" for item in topic["minimum"]])
    lines.append("- 확장 목표:")
    lines.extend([f"  - {item}" for item in topic["stretch"]])
    lines.append(f"- 손코딩 가치: {topic['value']}")
    return "\n".join(lines)


def render_hand_coding_topics() -> str:
    general = [t for t in TOPICS if t["category"] == "general"]
    rust_only = [t for t in TOPICS if t["category"] == "rust"]
    cpp_only = [t for t in TOPICS if t["category"] == "cpp"]
    java_only = [t for t in TOPICS if t["category"] == "java"]
    kotlin_only = [t for t in TOPICS if t["category"] == "kotlin"]
    data = [t for t in TOPICS if t["category"] == "data"]
    data_section = "\n\n".join(render_topic_section(topic, f"### {topic['num']}. {topic['title']}") for topic in data)
    return text(
        f"""
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

        {render_topic_section(general[0], "### 1. `grep` 비슷한 미니 텍스트 검색기")}

        {render_topic_section(general[1], "### 2. 인메모리 `key-value store`")}

        {render_topic_section(general[2], "### 3. HTTP 서버와 라우터 직접 만들기")}

        {render_topic_section(general[3], "### 4. 간단한 `JSON parser`")}

        {render_topic_section(general[4], "### 5. 스레드 풀과 작업 큐")}

        ## 언어별 추천 주제

        ### Rust 중심

        {render_topic_section(rust_only[0], "#### A. 미니 `git` 객체 저장소")}

        {render_topic_section(rust_only[1], "#### B. `arena allocator`")}

        {render_topic_section(rust_only[2], "#### C. `tiny async executor`")}

        ### C++ 중심

        {render_topic_section(cpp_only[0], "#### A. 작은 벡터/문자열 클래스 구현")}

        {render_topic_section(cpp_only[1], "#### B. expression evaluator")}

        {render_topic_section(cpp_only[2], "#### C. 파일 기반 로그 라이브러리")}

        ### Java 중심

        {render_topic_section(java_only[0], "#### A. 작은 dependency injection container")}

        {render_topic_section(java_only[1], "#### B. 간단한 JDBC-backed todo app")}

        {render_topic_section(java_only[2], "#### C. rate limiter")}

        ### Kotlin 중심

        {render_topic_section(kotlin_only[0], "#### A. 코루틴 기반 작업 스케줄러")}

        {render_topic_section(kotlin_only[1], "#### B. 간단한 Kotlin/JVM 메모 앱")}

        {render_topic_section(kotlin_only[2], "#### C. DSL 스타일 설정 파서")}

        ## 데이터 분석 & 병렬처리 준비용 주제

        {data_section}

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
        """
    )


def render_root_readme() -> str:
    rows = []
    for topic in TOPICS:
        extras = []
        if topic["kind"] in {"mini_groupby_engine", "windowed_timeseries_analyzer"}:
            extras.append("sql")
        if topic["kind"] in {"batch_etl_pipeline", "parallel_log_analyzer", "mini_mapreduce"}:
            extras.append("shell")
        rows.append(f"| {topic['num']:02d} | `{topic['slug']}` | {', '.join(topic['languages'] + extras)} | {topic['title']} |")
    body = text(
        f"""
        # Hand-Coding Monorepo

        손코딩 연습용 모노레포입니다. `HAND_CODING_TOPICS.md`에 있는 25개 토픽과 42개 실제 프로젝트를 함께 관리합니다.
        이 저장소의 기본 템플릿은 의도적으로 아주 얇습니다. 대부분의 프로젝트는 `make run`에서 최소 hello 동작만 보장하고, 실제 미션 성공 기준은 `make e2e`에 들어 있습니다.

        ## 빠른 시작

        1. `make bootstrap`
        2. `make smoke`
        3. `make verify`

        `bootstrap`은 로컬 툴체인을 준비합니다. `smoke`는 42개 프로젝트의 hello 템플릿 실행 경로를 실제로 돌립니다. `verify`는 테스트와 e2e를 끝까지 순회하며, 실패가 있어도 요약을 남기고 마지막에만 실패 코드로 종료합니다.

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
        sudo apt install -y build-essential curl ca-certificates pkg-config \\
          zlib1g-dev libssl-dev libbz2-dev libffi-dev liblzma-dev \\
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
        __PROJECT_ROWS__
        """
    )
    return body.replace("__PROJECT_ROWS__", "\n".join(rows))


def render_topic_readme(topic: dict) -> str:
    lines = [
        f"# {topic['num']:02d}. {topic['title']}",
        "",
        topic["value"],
        "",
        "## 언어",
        "",
        f"- {', '.join(LANG_LABELS[lang] for lang in topic['languages'])}",
    ]
    if topic["kind"] in {"mini_groupby_engine", "windowed_timeseries_analyzer"}:
        lines.append("- SQL 기준선 포함")
    if topic["kind"] in {"batch_etl_pipeline", "parallel_log_analyzer", "mini_mapreduce"}:
        lines.append("- 셸 기반 보조 스모크 스크립트 포함")
    lines.extend(
        [
            "",
            "## 먼저 볼 것",
            "",
            "- `SPEC.md`: 최종 미션 요구사항과 템플릿 baseline을 함께 설명합니다.",
            "- `QA.md`: 어떤 테스트를 통과해야 하는지와 e2e 성공 기준을 정리합니다.",
            "- `fixtures/`: hello 출력용 fixture와 mission 출력용 fixture를 함께 둡니다.",
            "- `e2e/`: 언어별 미션 acceptance test 스크립트가 있습니다.",
            "",
            "## 템플릿 기본 상태",
            "",
            ("- 이 토픽의 fresh template은 작은 실제 HTTP 서버를 띄웁니다. "
             "기본 계약은 `GET /health -> ok`, `POST /echo -> body 그대로`입니다.")
            if topic["kind"] == "http_server_router"
            else f"- 이 토픽의 fresh template은 `make run`에서 `{hello_output(topic).strip()}`를 출력합니다.",
            "- `make smoke`는 이 최소 실행 경로만 확인합니다.",
            "- `make e2e`는 최종 미션 성공 기준을 검증합니다. 처음에는 실패해도 정상입니다.",
            "",
            "## 어떻게 진행하나",
            "",
            "1. `SPEC.md`와 `QA.md`를 먼저 읽습니다.",
            "2. `fixtures/expected.txt`와 `fixtures/mission-expected.txt` 또는 대응 fixture를 함께 확인합니다." if topic["kind"] != "http_server_router" else "2. `fixtures/expected-health.txt`, `fixtures/expected-echo.txt`, `e2e/*.sh`를 함께 열어 baseline과 mission 기준을 확인합니다.",
            "3. 원하는 언어 폴더에서 가능하면 `make -C <language> build`와 `make -C <language> run`을 먼저 실행합니다.",
            "4. 아래 언어별 구현 파일을 직접 수정합니다.",
            "5. 작업 중에는 `make -C <language> test`를 자주 돌리고, 마무리 단계에서 `make -C <language> e2e`로 미션 성공 여부를 확인합니다.",
            "6. 가능하면 현재 인자 개수/위치와 stdout 형식은 유지한 채 내부 구현만 교체하는 방식으로 진행합니다.",
            "",
            "## 언어별 구현 위치",
            "",
        ]
    )
    for idx, language in enumerate(topic["languages"]):
        if idx > 0:
            lines.append("")
        lines.extend(render_topic_language_section(topic, language))
    lines.extend(render_support_sections(topic))
    lines.extend(["", "## 빠른 실행", ""])
    for language in topic["languages"]:
        targets = ["build", "run", "test", "e2e", "smoke"] if language != "python" else ["run", "test", "e2e", "smoke"]
        lines.append(f"- {LANG_LABELS[language]}: {', '.join(f'`make -C {language} {target}`' for target in targets)}")
    lines.extend(
        [
            "",
            "## 문서",
            "",
            "- `SPEC.md`",
            "- `QA.md`",
            "",
            "언어별 상세 직접 실행 예시는 각 언어 폴더의 `README.md`에도 정리되어 있습니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def spec_items(topic: dict) -> list[str]:
    common = [
        f"프로그램은 `{topic['slug']}` 토픽의 mission fixture를 처리하고 결정적인 결과를 출력해야 합니다.",
        "프로젝트는 `make run`, `make test`, `make e2e`, `make smoke`를 지원해야 합니다.",
        "Rust, C++, Java, Kotlin 프로젝트는 `make build`도 지원해야 합니다.",
        "핵심 로직은 `src` 아래 라이브러리/모듈로 분리하고 테스트에서 직접 호출 가능해야 합니다.",
        "예외 입력 또는 실패 시나리오를 최소 하나 이상 테스트로 검증해야 합니다.",
    ]
    extra = {
        "mini_grep": ["입력 파일 경로와 쿼리를 받을 수 있어야 합니다.", "파일 내용에서 일치하는 줄과 줄 번호를 출력해야 합니다."],
        "key_value_store": ["`SET`, `GET`, `DELETE`, `SNAPSHOT` 흐름이 동작해야 합니다.", "snapshot 출력은 key 정렬 기준으로 안정적이어야 합니다."],
        "http_server_router": ["기본 포트는 `18080`이어야 합니다.", "`GET /health`는 `ok`, `POST /echo`는 요청 바디를 그대로 반환해야 합니다.", "지원하지 않는 경로나 메서드는 오류 상태 코드로 응답해야 합니다."],
        "json_parser": ["객체와 배열을 포함한 기본 JSON 값 파싱이 가능해야 합니다.", "top-level key 순서는 fixture 기준으로 안정적이어야 합니다."],
        "thread_pool_queue": ["고정된 worker 수로 작업을 실행해야 합니다.", "결과 출력 순서는 입력 순서를 유지해야 합니다."],
        "mini_git_object_store": ["blob 파일을 읽고 `.git-lite/objects` 아래에 저장해야 합니다.", "저장 후 객체 id와 원문 복원을 확인할 수 있어야 합니다."],
        "arena_allocator": ["arena는 문자열 slice 또는 index 기반 핸들을 돌려줘야 합니다.", "clear 후 재사용 가능해야 합니다."],
        "tiny_async_executor": ["즉시 완료되는 future 두 개 이상을 실행해야 합니다.", "`block_on` 결과가 안정적이어야 합니다."],
        "tiny_vector": ["push/pop과 capacity 증가가 동작해야 합니다.", "복사/이동 의미론을 깨지 않는 테스트를 포함해야 합니다."],
        "expression_evaluator": ["연산자 우선순위와 괄호 처리가 가능해야 합니다.", "잘못된 수식은 실패로 처리해야 합니다."],
        "file_log_library": ["회전 조건을 강제로 한 번 발생시켜야 합니다.", "회전된 파일과 현재 파일이 모두 남아야 합니다."],
        "di_container": ["annotation 또는 marker 타입 기반 주입을 제공해야 합니다.", "순환 의존 감지 테스트를 포함해야 합니다."],
        "jdbc_todo_cli": ["embedded DB를 만들고 todo 2개를 삽입해야 합니다.", "list 결과가 fixture와 일치해야 합니다."],
        "rate_limiter": ["token bucket 기준 허용/거절 판정을 보여야 합니다.", "버스트 후 회복 시나리오 테스트를 포함해야 합니다."],
        "coroutine_scheduler": ["지연 실행과 취소 가능한 작업 흐름을 보여야 합니다.", "세 작업을 완료 상태로 출력해야 합니다."],
        "notes_app_jvm": ["메모 추가, 목록 조회, 검색 중 최소 두 흐름을 보여야 합니다.", "로컬 파일 저장 형식은 줄 단위로 안정적이어야 합니다."],
        "dsl_config_parser": ["블록과 리스트 문법을 파싱해 정규화된 키/값으로 출력해야 합니다.", "문법 오류는 위치 정보를 포함해 실패해야 합니다."],
        "dataset_profiler": ["row 수, null count, 평균을 계산해야 합니다.", "숫자 컬럼이 아닌 경우 통계 계산을 건너뛰어야 합니다."],
        "mini_groupby_engine": ["status=ok 필터 뒤 team 기준 sum/count를 계산해야 합니다.", "SQL 기준 query와 동일한 결과를 만들어야 합니다."],
        "batch_etl_pipeline": ["잘못된 row는 reject로 분리해야 합니다.", "cleaned 수와 rejected 수를 함께 보고해야 합니다."],
        "parallel_log_analyzer": ["single-thread와 multi-worker 결과가 동일해야 합니다.", "status code 집계와 top endpoint를 출력해야 합니다."],
        "external_sort_merge": ["chunk sort와 merge가 동작해야 합니다.", "최종 출력은 전역 정렬 상태여야 합니다."],
        "windowed_timeseries_analyzer": ["시간 단위 버킷 합계와 rolling average를 계산해야 합니다.", "SQL 기준 bucket 결과와 일치해야 합니다."],
        "heavy_hitter_stream": ["exact top-N과 approximate top-N을 모두 출력해야 합니다.", "approx 결과에는 최소 exact 상위 key가 포함돼야 합니다."],
        "mini_mapreduce": ["map, shuffle, reduce 단계가 분리되어 있어야 합니다.", "baseline word count와 결과가 일치해야 합니다."],
    }
    return common + extra[topic["kind"]]


def render_topic_spec(topic: dict) -> str:
    numbered = "\n".join(f"{idx}. {item}" for idx, item in enumerate(spec_items(topic), 1))
    baseline = (
        "- fresh template은 `GET /health`, `POST /echo`만 처리하는 작은 실제 HTTP 서버를 제공합니다."
        if topic["kind"] == "http_server_router"
        else f"- fresh template의 `make run` 출력은 `{hello_output(topic).strip()}`입니다."
    )
    lines = [
        f"# SPEC: {topic['num']:02d}. {topic['title']}",
        "",
        "## 템플릿 baseline",
        "",
        baseline,
        "- 이 baseline은 시작점일 뿐이며, 아래 요구사항 전체를 만족하지는 않습니다.",
        "- `make smoke`는 baseline 실행 가능 여부를 확인하고, `make e2e`는 아래 미션 성공 기준을 검증합니다.",
        "",
        "## 요구사항",
        "",
        numbered,
        "",
        "## 비목표",
        "",
        "- 지금 단계에서 production 완성본을 만들지 않습니다.",
        "- fresh template은 최소 실행 골격만 제공하며, 최종 미션 구현은 사용자가 채워 넣습니다.",
        "",
        "## Stretch Goal",
        "",
        f"- {'; '.join(topic['stretch'])}",
    ]
    return "\n".join(lines) + "\n"


def render_topic_qa(topic: dict) -> str:
    integration = ["`make run` 또는 서버 기동이 baseline 수준에서 동작한다.", "`make test`는 최소 구조 검증 또는 보조 단위 테스트를 제공한다.", "`make e2e`가 최종 미션 acceptance test를 수행한다."]
    if topic["kind"] in {"mini_groupby_engine", "windowed_timeseries_analyzer"}:
        integration.append("SQL 기준선과 Rust/Python 결과를 비교한다.")
    if topic["kind"] == "http_server_router":
        integration.append("health, echo, 잘못된 경로/메서드 응답을 실제 HTTP 호출로 검증한다.")
    failure = [
        "존재하지 않는 입력 파일 경로를 전달했을 때 오류를 반환한다.",
        "잘못된 포맷 또는 잘못된 명령이 테스트 또는 e2e에서 고정돼 있다.",
        "출력 순서가 불안정해지지 않도록 정렬 또는 안정화 규칙을 가진다.",
    ]
    if topic["kind"] in {"parallel_log_analyzer", "mini_mapreduce", "thread_pool_queue", "coroutine_scheduler", "tiny_async_executor"}:
        failure.append("single-thread 기준 결과와 병렬 결과를 비교하는 체크가 있다.")
    baseline = (
        "- `make run`으로 작은 실제 HTTP 서버가 떠야 한다."
        if topic["kind"] == "http_server_router"
        else f"- `make run`이 `{hello_output(topic).strip()}`를 출력해야 한다."
    )
    mission_lines = [
        "- `e2e/*.sh`가 `curl`로 health, echo, 오류 응답 기준을 모두 검증한다."
        if topic["kind"] == "http_server_router"
        else "- `e2e/*.sh`가 `fixtures/mission-expected.txt`와 실제 출력을 비교한다."
    ]
    if topic["kind"] in {"mini_groupby_engine", "windowed_timeseries_analyzer"}:
        mission_lines.append("- 성공 시 Rust/Python 출력이 `sql/query.sql` 기준선과도 모순되지 않아야 한다.")
    lines = [
        f"# QA: {topic['num']:02d}. {topic['title']}",
        "",
        "## Template Baseline",
        "",
        baseline,
        "- `make smoke`는 이 baseline만 확인한다.",
        "- fresh template 상태에서 `make e2e`는 실패해도 정상이다.",
        "",
        "## Unit",
        "",
        "- 핵심 함수가 비어 있지 않고 직접 호출 가능하다.",
        "- 최소 hello 경로 또는 작은 보조 함수가 테스트로 고정돼 있다.",
        "- 미션 구현 중에는 경계조건 테스트를 여기에 추가한다.",
        "",
        "## Integration",
        "",
        *[f"- {item}" for item in integration],
        "",
        "## Mission Success",
        "",
        *mission_lines,
        "",
        "## Failure Cases",
        "",
        *[f"- {item}" for item in failure],
        "",
        "## Manual Smoke",
        "",
        "- fixture를 기준으로 결과가 deterministic 한지 확인한다.",
        "- README 명령을 그대로 실행해도 동일한 결과가 나오는지 확인한다.",
        "- 출력 파일 또는 서버 응답이 expected fixture와 같은지 확인한다.",
    ]
    return "\n".join(lines) + "\n"


def fixtures_for(topic: dict) -> dict[str, str]:
    mapping = {
        "mini_grep": {
            "sample.txt": "Rust makes it easy to build tools.\nC++ still teaches discipline.\nRust and C++ can coexist.\n",
        },
        "key_value_store": {
            "commands.txt": "SET language Rust\nSET mood focused\nGET language\nDELETE mood\nSNAPSHOT\n",
        },
        "http_server_router": {
            "echo-body.txt": "hello-http",
            "expected-health.txt": "ok\n",
            "expected-echo.txt": "hello-http",
        },
        "json_parser": {
            "sample.json": '{ "name": "wheel", "count": 3, "active": true, "items": [1, 2] }\n',
        },
        "thread_pool_queue": {
            "tasks.txt": "1\n2\n3\n4\n",
        },
        "mini_git_object_store": {
            "blob.txt": "hello-git-object\n",
        },
        "arena_allocator": {
            "words.txt": "alpha\nbeta\ngamma\n",
        },
        "tiny_async_executor": {
            "tasks.txt": "fetch-metrics\nflush-cache\n",
        },
        "tiny_vector": {
            "values.txt": "5\n8\n13\n",
        },
        "expression_evaluator": {
            "expressions.txt": "1 + 2 * (3 - 1)\n",
        },
        "file_log_library": {
            "events.txt": "INFO started\nWARN low-disk\nERROR retry\n",
        },
        "di_container": {
            "components.txt": "Database\nService\nController\n",
        },
        "jdbc_todo_cli": {
            "todos.txt": "buy-milk\nwrite-tests\n",
        },
        "rate_limiter": {
            "requests.txt": "0\n100\n200\n900\n",
        },
        "coroutine_scheduler": {
            "jobs.txt": "collect\ntransform\npublish\n",
        },
        "notes_app_jvm": {
            "notes.txt": "1|Rust ideas|Build a parser\n2|Parallel notes|Measure speedup\n",
        },
        "dsl_config_parser": {
            "sample.dsl": "server { port = 8080 host = localhost }\nfeatures = [search,metrics]\n",
        },
        "dataset_profiler": {
            "sample.csv": "city,count,ratio\nSeoul,10,0.5\nBusan,20,0.7\nJeju,,0.1\n",
        },
        "mini_groupby_engine": {
            "sales.csv": "team,amount,status\nred,10,ok\nblue,5,ok\nred,2,fail\nblue,8,ok\n",
            "query.sql": "select team, sum(amount) as total, count(*) as row_count from sales where status = 'ok' group by team order by team;\n",
        },
        "batch_etl_pipeline": {
            "raw.csv": "id,name,score\n1,Alice,10\n2,,12\n3,Bob,9\nbad,row\n",
        },
        "parallel_log_analyzer": {
            "app.log": "200 /health\n500 /echo\n200 /health\n404 /missing\n500 /echo\n",
        },
        "external_sort_merge": {
            "numbers.txt": "9\n1\n5\n3\n7\n2\n",
        },
        "windowed_timeseries_analyzer": {
            "series.csv": "ts,value\n2026-03-01T10:00:00,10\n2026-03-01T10:10:00,20\n2026-03-01T11:05:00,5\n",
            "query.sql": "select strftime(ts, '%Y-%m-%dT%H:00') as bucket, sum(value) as bucket_sum from series group by 1 order by 1;\n",
        },
        "heavy_hitter_stream": {
            "events.txt": "red\nblue\nred\ngreen\nred\nblue\n",
        },
        "mini_mapreduce": {
            "documents.txt": "rust rust python\npython data rust\n",
        },
    }
    files = dict(mapping[topic["kind"]])
    if topic["kind"] != "http_server_router":
        files["expected.txt"] = hello_output(topic)
        files["mission-expected.txt"] = mission_output(topic)
    return files
