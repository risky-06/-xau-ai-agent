# AI AGENT PROJECT — V1 AI CORE

## 1. V1 OBJECTIVE

V1 membangun otak dasar AI Agent.

V1 harus mampu:

- menerima goal
- memahami goal
- memecah goal menjadi task
- membuat plan
- menjalankan task sederhana
- menyimpan state
- mengevaluasi hasil
- menggunakan critic
- menghasilkan keputusan yang dapat dijelaskan

V1 belum menjalankan aktivitas berisiko tinggi.

V1 belum menggunakan uang nyata.

V1 belum melakukan trading live.

---

## 2. FREE-FIRST PRINCIPLE

Sistem harus dirancang agar tidak bergantung pada API berbayar.

Model layer harus bersifat provider-independent.

Arsitektur:

AI CORE
↓
MODEL INTERFACE
↓
LOCAL MODEL / FREE MODEL / OPTIONAL PROVIDER
↓
RESPONSE

Pergantian model tidak boleh membutuhkan perubahan besar pada AI Core.

Tidak boleh menyimpan API key di source code.

---

## 3. CORE ARCHITECTURE

USER
↓
ORCHESTRATOR
↓
PLANNER
↓
TASK MANAGER
↓
MEMORY
↓
CRITIC
↓
ACTION
↓
OBSERVATION
↓
EVALUATION
↓
RESULT

---

## 4. ORCHESTRATOR

Orchestrator adalah pengatur utama sistem.

Tugas:

1. menerima goal
2. menentukan task
3. menentukan urutan task
4. memanggil component yang diperlukan
5. memeriksa status task
6. menangani kegagalan
7. mengirim hasil ke evaluator

Orchestrator tidak boleh menjalankan tindakan berisiko tanpa permission.

---

## 5. PLANNER

Planner mengubah goal menjadi rencana.

Input:

GOAL

Output:

PLAN

Format:

GOAL
↓
TASK 1
↓
TASK 2
↓
TASK 3
↓
VALIDATION
↓
RESULT

Planner harus:

- menjelaskan tujuan task
- menentukan dependency
- menentukan expected output
- menentukan validation method
- menentukan risiko

---

## 6. TASK MANAGER

Setiap task mempunyai state.

Allowed states:

PENDING
PLANNED
RUNNING
SUCCESS
FAILED
BLOCKED
CANCELLED
EVALUATED

State tidak boleh dilompati tanpa alasan yang tercatat.

---

## 7. MEMORY

V1 menggunakan beberapa kategori memory.

### Short-Term Memory

Menyimpan konteks task aktif.

### Long-Term Memory

Menyimpan informasi yang relevan untuk penggunaan berikutnya.

### Task History

Menyimpan:

- task
- timestamp
- status
- result
- error

### Decision History

Menyimpan:

- decision
- reason
- evidence
- result

### Experiment History

Menyimpan:

- hypothesis
- experiment
- result
- conclusion

---

## 8. MEMORY RULES

Memory tidak boleh menyimpan data secara sembarangan.

Setiap memory entry minimal memiliki:

- id
- type
- timestamp
- content
- source
- importance
- status

Memory harus dapat diperbarui.

Memory tidak boleh dianggap benar hanya karena pernah disimpan.

---

## 9. CRITIC ENGINE

Critic memeriksa keputusan sebelum tindakan.

Pipeline:

DECISION
↓
EVIDENCE CHECK
↓
CONSISTENCY CHECK
↓
GOAL CHECK
↓
RISK CHECK
↓
APPROVE / REJECT

Critic harus dapat mengatakan:

APPROVED

atau

REJECTED

beserta alasan.

---

## 10. EVIDENCE RULE

AI harus membedakan:

FACT
ASSUMPTION
HYPOTHESIS
OPINION
UNKNOWN

Jika informasi tidak cukup:

UNKNOWN

harus lebih dipilih daripada membuat fakta palsu.

---

## 11. ACTION PERMISSION

Setiap tindakan memiliki permission level.

LEVEL 0
READ

LEVEL 1
ANALYZE

LEVEL 2
GENERATE

LEVEL 3
LOW-RISK ACTION

LEVEL 4
FINANCIAL ACTION

LEVEL 5
LIVE TRADING

V1 hanya menggunakan:

LEVEL 0
LEVEL 1
LEVEL 2

Level lebih tinggi belum aktif.

---

## 12. SAFETY ENGINE

Safety Engine harus memeriksa:

- permission
- task state
- input validity
- risk
- budget
- target
- action type

Jika pemeriksaan gagal:

ACTION BLOCKED

---

## 13. ERROR HANDLING

Jika task gagal:

TASK
↓
ERROR
↓
CLASSIFY ERROR
↓
RETRY / MODIFY / ABORT

Maximum retry harus memiliki batas.

AI tidak boleh melakukan infinite retry.

---

## 14. SELF-CHECK

Sebelum menghasilkan final result:

AI harus melakukan:

1. Goal check
2. Requirement check
3. Evidence check
4. Logic check
5. Safety check
6. Output check

---

## 15. OBSERVATION

Setelah action:

ACTION
↓
OBSERVE RESULT
↓
COMPARE EXPECTED VS ACTUAL
↓
STORE RESULT

Observation harus dicatat.

---

## 16. EVALUATION

Evaluator menghitung:

- success
- failure
- error
- efficiency
- quality
- cost
- reliability

V1 tidak melakukan self-modification otomatis.

---

## 17. SELF-IMPROVEMENT POLICY

V1 hanya dapat:

- menemukan masalah
- mengusulkan improvement
- membuat improvement proposal
- menyimpan proposal

V1 belum boleh mengubah source code production secara otomatis.

Improvement harus melalui:

PROPOSAL
↓
TEST
↓
REVIEW
↓
APPROVAL
↓
IMPLEMENTATION

---

## 18. MODEL INTERFACE

AI Core tidak boleh bergantung langsung pada satu model.

Gunakan interface:

MODEL INPUT
↓
MODEL ADAPTER
↓
MODEL
↓
MODEL RESPONSE
↓
AI CORE

Model adapter dapat diganti.

Contoh provider:

LOCAL
FREE
OPTIONAL EXTERNAL

Tidak ada provider yang menjadi dependency wajib pada V1.

---

## 19. LOGGING

Setiap proses penting dicatat.

Minimal:

- timestamp
- task id
- action
- input summary
- output summary
- status
- error
- decision
- reason

Sensitive data tidak boleh dimasukkan ke log tanpa alasan.

---

## 20. V1 SUCCESS CRITERIA

V1 dianggap selesai jika:

[ ] Goal dapat diterima

[ ] Goal dapat diubah menjadi plan

[ ] Plan dapat menjadi task

[ ] Task mempunyai state

[ ] Memory dapat menyimpan hasil

[ ] Critic dapat memeriksa keputusan

[ ] Safety Engine dapat memblokir tindakan

[ ] Error handling bekerja

[ ] Evaluation bekerja

[ ] Model dapat diganti tanpa mengubah AI Core

[ ] Tidak ada API key di source code

[ ] Tidak ada live financial action

---

## 21. V1 LIMITATIONS

V1 belum memiliki:

- autonomous money management
- affiliate automation
- TikTok automation
- live trading
- autonomous financial transactions
- automatic source-code deployment
- unrestricted self-modification

Fitur tersebut hanya dapat ditambahkan pada versi berikutnya setelah validation.

---

## 22. V1 DEVELOPMENT RULE

Build small.

Test every component.

Document every change.

Never skip validation.

Never bypass safety.

Never hardcode secrets.

Never assume an action succeeded without observation.

---

## STATUS

V1 = AI CORE SPECIFICATION

NEXT:

V1 IMPLEMENTATION
