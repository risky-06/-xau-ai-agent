"""
Rizda AI Agent
V1 Core Foundation

Purpose:
- Goal handling
- Task management
- Evidence classification
- Decision + WHY
- Permission and safety gates
- Observation
- Evaluation
- Memory
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List
from datetime import datetime


# ============================================================
# 1. TASK STATE
# ============================================================

class TaskState(Enum):
    PENDING = "PENDING"
    PLANNED = "PLANNED"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    BLOCKED = "BLOCKED"
    CANCELLED = "CANCELLED"
    EVALUATED = "EVALUATED"


# ============================================================
# 2. EVIDENCE TYPE
# ============================================================

class EvidenceType(Enum):
    FACT = "FACT"
    ASSUMPTION = "ASSUMPTION"
    HYPOTHESIS = "HYPOTHESIS"
    OPINION = "OPINION"
    UNKNOWN = "UNKNOWN"


# ============================================================
# 3. PERMISSION LEVEL
# ============================================================

class PermissionLevel(Enum):
    READ = 0
    ANALYZE = 1
    GENERATE = 2
    LOW_RISK_ACTION = 3
    FINANCIAL_ACTION = 4
    LIVE_TRADING = 5


# ============================================================
# 4. TASK
# ============================================================

@dataclass
class Task:
    task_id: str
    description: str
    state: TaskState = TaskState.PENDING
    priority: int = 1
    expected_result: str = ""
    actual_result: str = ""
    error: str = ""
    retry_count: int = 0
    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )


# ============================================================
# 5. MEMORY
# ============================================================

class Memory:
    def __init__(self):
        self.short_term: List[Dict[str, Any]] = []
        self.long_term: List[Dict[str, Any]] = []
        self.task_history: List[Dict[str, Any]] = []
        self.decision_history: List[Dict[str, Any]] = []
        self.experiment_history: List[Dict[str, Any]] = []
        self.financial_history: List[Dict[str, Any]] = []
        self.performance_history: List[Dict[str, Any]] = []

    def remember(self, category: str, data: Dict[str, Any]):
        memory_map = {
            "short_term": self.short_term,
            "long_term": self.long_term,
            "task": self.task_history,
            "decision": self.decision_history,
            "experiment": self.experiment_history,
            "financial": self.financial_history,
            "performance": self.performance_history,
        }

        target = memory_map.get(category)

        if target is None:
            raise ValueError(f"Unknown memory category: {category}")

        target.append(data)


# ============================================================
# 6. EVIDENCE
# ============================================================

@dataclass
class Evidence:
    content: str
    evidence_type: EvidenceType
    source: str = ""

    def is_reliable(self) -> bool:
        return self.evidence_type == EvidenceType.FACT


# ============================================================
# 7. DECISION
# ============================================================

@dataclass
class Decision:
    decision: str
    why: str
    evidence: List[Evidence] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    alternatives: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    expected_result: str = ""
    validation_status: str = "UNVALIDATED"


# ============================================================
# 8. CRITIC
# ============================================================

class Critic:

    def review(
        self,
        goal: str,
        decision: Decision,
        required_permission: PermissionLevel,
        current_permission: PermissionLevel,
    ) -> Dict[str, Any]:

        reasons = []

        if not goal.strip():
            reasons.append("Goal is empty.")

        if not decision.decision.strip():
            reasons.append("Decision is empty.")

        if not decision.why.strip():
            reasons.append("Decision WHY is missing.")

        if current_permission.value < required_permission.value:
            reasons.append("Insufficient permission.")

        if reasons:
            return {
                "status": "REJECTED",
                "reasons": reasons,
            }

        return {
            "status": "APPROVED",
            "reasons": [],
        }


# ============================================================
# 9. SAFETY ENGINE
# ============================================================

class SafetyEngine:

    def check(
        self,
        required_permission: PermissionLevel,
        current_permission: PermissionLevel,
    ) -> Dict[str, Any]:

        if current_permission.value < required_permission.value:
            return {
                "allowed": False,
                "reason": "ACTION BLOCKED: insufficient permission.",
            }

        return {
            "allowed": True,
            "reason": "Safety permission check passed.",
        }


# ============================================================
# 10. EVALUATION
# ============================================================

class EvaluationEngine:

    def evaluate(
        self,
        expected: str,
        actual: str,
    ) -> Dict[str, Any]:

        if not actual:
            status = "FAILURE"
        elif expected.strip().lower() == actual.strip().lower():
            status = "SUCCESS"
        else:
            status = "PARTIAL_SUCCESS"

        return {
            "status": status,
            "expected": expected,
            "actual": actual,
        }


# ============================================================
# 11. RIZDA CORE
# ============================================================

class RizdaAgent:

    def __init__(self):
        self.name = "Rizda"
        self.owner = "Risky"

        # V1 hanya sampai GENERATE.
        self.permission = PermissionLevel.GENERATE

        self.memory = Memory()
        self.critic = Critic()
        self.safety = SafetyEngine()
        self.evaluator = EvaluationEngine()

    def understand_goal(self, goal: str) -> Dict[str, Any]:

        return {
            "goal": goal,
            "constraints": [
                "free-first",
                "evidence-first",
                "safety-first",
            ],
            "success_criteria": [
                "goal understood",
                "plan created",
                "decision explainable",
                "risk controlled",
            ],
        }

    def create_task(
        self,
        task_id: str,
        description: str,
        expected_result: str = "",
    ) -> Task:

        task = Task(
            task_id=task_id,
            description=description,
            state=TaskState.PLANNED,
            expected_result=expected_result,
        )

        self.memory.remember(
            "task",
            {
                "task_id": task.task_id,
                "description": task.description,
                "state": task.state.value,
            },
        )

        return task

    def decide(
        self,
        decision_text: str,
        why: str,
        evidence: List[Evidence] = None,
    ) -> Decision:

        return Decision(
            decision=decision_text,
            why=why,
            evidence=evidence or [],
        )

    def review_decision(
        self,
        goal: str,
        decision: Decision,
        required_permission: PermissionLevel,
    ) -> Dict[str, Any]:

        result = self.critic.review(
            goal=goal,
            decision=decision,
            required_permission=required_permission,
            current_permission=self.permission,
        )

        self.memory.remember(
            "decision",
            {
                "decision": decision.decision,
                "why": decision.why,
                "critic": result,
            },
        )

        return result

    def observe(
        self,
        expected: str,
        actual: str,
    ) -> Dict[str, Any]:

        result = self.evaluator.evaluate(
            expected,
            actual,
        )

        self.memory.remember(
            "performance",
            result,
        )

        return result

    def status(self) -> Dict[str, Any]:

        return {
            "agent": self.name,
            "owner": self.owner,
            "permission": self.permission.name,
            "status": "READY",
        }


# ============================================================
# 12. BASIC SELF TEST
# ============================================================

def self_test():

    rizda = RizdaAgent()

    print("=== RIZDA V1 SELF TEST ===")

    print("\nSTATUS:")
    print(rizda.status())

    goal = "Mempelajari peluang menghasilkan revenue secara legal."

    print("\nGOAL:")
    print(rizda.understand_goal(goal))

    task = rizda.create_task(
        task_id="V1-001",
        description="Menganalisis peluang pertama.",
        expected_result="Peluang teridentifikasi.",
    )

    print("\nTASK:")
    print(task)

    evidence = Evidence(
        content="Evidence belum tersedia pada tahap awal.",
        evidence_type=EvidenceType.UNKNOWN,
        source="system",
    )

    decision = rizda.decide(
        decision_text="Belum memilih peluang.",
        why="Evidence belum cukup untuk mengambil keputusan.",
        evidence=[evidence],
    )

    print("\nDECISION:")
    print(decision)

    review = rizda.review_decision(
        goal=goal,
        decision=decision,
        required_permission=PermissionLevel.GENERATE,
    )

    print("\nCRITIC:")
    print(review)

    observation = rizda.observe(
        expected="Peluang teridentifikasi.",
        actual="Belum ada peluang tervalidasi.",
    )

    print("\nEVALUATION:")
    print(observation)

    print("\n=== SELF TEST COMPLETE ===")


if __name__ == "__main__":
    self_test()
