# karpathy-auto-research-apply-for-codex

고정된 `purpose.txt`와 `rubric.txt`를 기준으로 planner -> executor -> evaluator 루프를 반복하면서 애플리케이션을 완성해 가기 위한 Codex 중심 스캐폴드 저장소입니다.

## 크레딧

이 저장소는 [karpathy/autoresearch](https://github.com/karpathy/autoresearch)에서 영감을 받았지만, 원본을 옮긴 것은 아닙니다. 핵심 루프 규율은 유지하되, 그 구조를 실제 애플리케이션 개발까지 확장하는 방향으로 재구성했습니다.

## 핵심 아이디어

모든 downstream 프로젝트는 결국 한 가지를 최적화해야 합니다. `purpose.txt`를 가능한 한 잘 수행하는 것입니다.

이를 위해 scaffold는 아래를 분리합니다.

- `purpose.txt`: 프로젝트가 달성해야 하는 목표
- `rubric.txt`: run 시작 후 고정되는 평가 계약
- control-plane 상태 파일: 현재 계획, 루프 상태, iteration 기록, 승격 결정
- `project/`: 실제 코드와 자산을 수정하는 작업면

루프는 다음처럼 명시적으로 굴러갑니다.

1. `purpose.txt`에 가장 도움이 되는 다음 bounded slice를 정한다
2. 그 slice를 계획한다
3. `project/` 안에서만 실행한다
4. 잠긴 rubric과 fresh evidence로 평가한다
5. iteration을 승격하거나 폐기한다
6. 메모리를 남기고 release gate에 도달할 때까지 반복한다

## 저장소 구성

- `CANON/`: 로컬 스킬 시스템과 운영 법전
- `CANON/skillsmith/packages/research-scaffold/`: downstream 운영 셸의 Canon-owned package source
- `purpose.txt`: 이 저장소 자체의 목표
- `rubric.txt`: 이 저장소를 scaffold로 평가하는 기준
- `docs/plans/`: 이 저장소의 설계 및 구현 기록

## Control Plane + Worktree 모델

실제 프로젝트는 `CANON/skillsmith/packages/research-scaffold/`와 루트 `CANON/` 트리를 함께 materialize해서 시작합니다. materialized scaffold 안에서는:

- scaffold 루트가 control plane 역할을 하고
- `project/`가 실제 제품 변경면이 되며
- `CANON/`이 intake, 설계, 계획, 자율 delivery, 리뷰, release를 라우팅합니다

이 분리는 중요합니다. planner, executor, evaluator가 하나의 흐릿한 행위로 섞이면 루프가 목적에 수렴하는지 검증할 수 없기 때문입니다.

## Autonomous Delivery Loop

목표가 정해지고 rubric이 고정되면 downstream 프로젝트는 다음 루프를 사용합니다.

1. `planner`가 `purpose.txt`를 가장 잘 전진시키는 다음 작은 slice를 정함
2. `executor`가 `project/` 안에서만 그 slice를 구현함
3. `evaluator`가 fresh proof를 실행하고 rubric 기준으로 점검함
4. `memory`가 반복할 것, 피할 것, 승격할 것을 기록함
5. `release`가 계속 반복할지, 멈추고 배포할지 결정함

이 운영 구간을 위해 새 Canon 스킬 `autonomous-app-loop`를 추가했습니다.

## Canon-Owned Scaffold Package에 들어 있는 것

- `purpose.txt`: downstream 프로젝트의 목표
- `rubric-generation-prompt.md`: `rubric.txt`를 1회 생성하기 위한 계약
- `plan.md`: 현재 승인된 실행 계획
- `loop-status.md`: 현재 단계, active iteration, 다음 owner
- `iterations/`: iteration별 상세 기록
- `results.tsv`: baseline과 이후 iteration의 요약 표
- `run.log`: 실행 증거
- `score.log`: 평가 증거
- `notes.md`: iteration 간 메모와 다음 아이디어
- `project/`: 실제 애플리케이션

downstream 쪽에서는 이 package surface를 루트로 펼친 뒤, 같은 위치에 루트 `CANON/` 트리를 함께 복사해 local operating law를 구성합니다. 저장소 루트에는 더 이상 별도 `research-scaffold/` 디렉토리가 필요하지 않습니다.

## 현재 버전의 정직한 한계

이 저장소는 아직 숨겨진 실행 엔진이 있다고 주장하지 않습니다.

현재 제공하는 것은:

- 명시적인 운영 계약
- 재사용 가능한 scaffold 구조
- 라우팅과 루프 제어를 위한 Canon 스킬과 자산
- 계획, 실행, 평가, release를 기록하는 상태 파일

아직 제공하지 않는 것은:

- 완전 무인으로 루프를 돌리는 전용 daemon
- 자동 채점 엔진
- 무조건 self-driving인 빌드 파이프라인

현재 버전은 불투명한 자동화보다 명시적인 운영 법칙을 우선합니다.

## 왜 이렇게 바꿨나

기존 research-loop 구조는 실험에는 적합했지만, 애플리케이션을 끝까지 완성하는 데는 부족했습니다. 새 구조는 purpose/rubric locking의 장점을 유지하면서 아래를 추가합니다.

- 명시적인 planning 및 architecture gate
- planner/executor/evaluator 역할 분리
- fresh evidence 기반 승격 결정
- 실제 종료 조건으로서의 release lane

## 다음에 더 보강할 만한 것

- `rubric.txt`와 control-plane 파일을 초기화하는 bootstrap 도구 추가
- frontend, backend, agentic tooling용 rubric 생성 변형 추가
- planner/executor/evaluator 루프 전체를 보여주는 예제 프로젝트 추가
- `results.tsv` 옆에 기계가 읽기 쉬운 iteration 요약 포맷 추가
