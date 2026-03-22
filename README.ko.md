# karpathy-auto-research-apply-for-codex

Codex로 목적 기반 auto-research 루프를 굴리기 위한 컨셉 저장소입니다.

## 크레딧

이 저장소는 Andrej Karpathy의 공개 실험 저장소인 [karpathy/autoresearch](https://github.com/karpathy/autoresearch)에서 아이디어를 얻었습니다.

다만 이 레포는 원본 코드를 그대로 옮긴 것이 아니라, 그 핵심 운영 아이디어를 Codex 중심의 scaffold로 재해석한 것입니다. 구체적으로는 아래에 초점을 둡니다.

- 목표를 담는 `purpose.txt`
- 1회성 rubric 생성
- 실행 중 rubric 고정
- 반복 가능한 개선/실행/채점/유지 루프

핵심 아이디어는 단순합니다.

- 명확한 `purpose.txt`를 작성한다
- 에이전트가 목적에 맞는 `rubric.txt`를 생성한다
- 생성된 rubric을 고정한다
- `project/`를 대상으로 개선 -> 실행 -> 채점 -> 유지/폐기를 반복한다

이 저장소는 완성된 제품이라기보다, 위 워크플로를 실험하고 포크하기 쉬운 형태로 정리한 출발점입니다.

## 저장소 구성

- `research-scaffold/`: 한 번의 auto-research run을 위한 재사용 가능한 템플릿
- `purpose.txt`: 이 저장소 자체의 목적
- `rubric.txt`: 이 저장소를 컨셉 스캐폴드로서 평가하는 기준
- `docs/plans/`: 설계 및 구현 계획 문서

## 왜 이렇게 나눴나

많은 auto-research 프롬프트는 아래 세 가지가 섞여 있습니다.

1. 프로젝트가 달성하려는 목표
2. 성공을 평가하는 기준
3. 에이전트가 반복 개선하는 방식

이 저장소는 그 셋을 의도적으로 분리합니다.

- `purpose.txt`는 목표를 정의합니다.
- `rubric.txt`는 평가 계약을 정의합니다.
- `AGENTS.md`는 실행 루프를 정의합니다.

중요한 제약은 rubric이 목적에서 한 번 생성될 수는 있어도, 실행 중 점수를 쉽게 만들기 위해 수정되면 안 된다는 점입니다.

## Scaffold 동작 방식

`research-scaffold/`는 복사해서 바로 쓰는 템플릿을 목표로 합니다.

예상 흐름은 다음과 같습니다.

1. `research-scaffold/project/`에 실제 대상 코드나 자산을 넣는다.
2. `research-scaffold/purpose.txt`를 실제 목표로 바꾼다.
3. `research-scaffold/rubric.txt`가 없다면 `research-scaffold/rubric-generation-prompt.md`를 이용해 생성한다.
4. 그 순간부터 `research-scaffold/rubric.txt`는 불변으로 취급한다.
5. 에이전트는 `research-scaffold/project/`를 반복적으로 수정하고, 실행하고, 채점하고, 검증된 개선만 유지한다.

## 현재 상태

이 저장소는 현재 아래를 제공합니다.

- 컨셉 수준의 README
- 루트 운영 지침
- 재사용 가능한 scaffold 디렉터리
- rubric 생성 프롬프트
- 실행 로그 템플릿
- downstream run을 위한 scaffold 수준 `AGENTS.md`

아직 전용 bootstrap 스크립트나 자동 채점 엔진은 없습니다. 현재 버전은 숨겨진 자동화보다 명시적인 텍스트 계약을 우선합니다.

## 다음에 더 보강할 만한 것

- `purpose.txt`에서 `rubric.txt`를 실제로 생성하는 작은 bootstrap 스크립트 추가
- frontend, CLI, research workflow용 rubric 확장 예시 추가
- baseline부터 개선까지 한 번의 전체 run 예제 추가
- `results.tsv` 옆에 기계가 읽기 쉬운 결과 요약 포맷 추가
