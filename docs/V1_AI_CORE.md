# AI AGENT PROJECT — V1 AI CORE

## 1. V1 OBJECTIVE

V1 adalah otak dasar Rizda.

Tujuan V1:

- menerima goal dari Risky
- memahami goal
- memecah goal menjadi task
- membuat execution plan
- mengelola task
- mengumpulkan evidence
- melakukan reasoning
- membuat decision
- menjelaskan WHY
- menjalankan action sesuai permission
- mengamati hasil
- mengevaluasi hasil
- menyimpan memory
- belajar dari hasil
- menjaga safety
- menolak action berisiko yang belum memiliki permission

V1 harus menjadi foundation untuk seluruh engine berikutnya.

V1 belum merupakan autonomous financial agent penuh.


## 2. MASTER FLOW

USER
↓
ORCHESTRATOR
↓
GOAL UNDERSTANDING
↓
PLANNER
↓
TASK MANAGER
↓
RESEARCH / EVIDENCE
↓
ANALYZER
↓
CRITIC
↓
DECISION
↓
PERMISSION CHECK
↓
ACTION
↓
OBSERVATION
↓
EVALUATION
↓
MEMORY
↓
LEARNING
↓
RESULT


## 3. ORCHESTRATOR

Orchestrator adalah pusat koordinasi Rizda.

Tugas:

- menerima request
- membuat task ID
- menentukan tujuan
- menentukan prioritas
- memanggil module yang diperlukan
- menjaga urutan proses
- memastikan task memiliki state
- meneruskan hasil antar-module
- menghentikan proses jika safety gagal

Orchestrator tidak boleh langsung melakukan tindakan berisiko.


## 4. GOAL UNDERSTANDING

Setiap request harus diubah menjadi struktur goal.

Minimal:

- goal
- objective
- constraints
- resources
- deadline
- success criteria
- risk level
- permission requirement

Contoh:

GOAL:
Mencari peluang menghasilkan Rp1.000.000.

CONSTRAINTS:
- free-first
- tanpa modal awal
- legal
- menggunakan resources yang tersedia

SUCCESS CRITERIA:
- menghasilkan revenue nyata
- memiliki net profit
- dapat diulang


## 5. PLANNER

Planner mengubah goal menjadi plan.

Format:

GOAL
→ OBJECTIVES
→ TASKS
→ DEPENDENCIES
→ EXECUTION
→ MEASUREMENT
→ EVALUATION

Planner harus:

- memecah pekerjaan
- menentukan prioritas
- menentukan dependency
- menentukan expected outcome
- menentukan evidence yang diperlukan
- menentukan risiko

Planner tidak boleh menganggap assumption sebagai fact.


## 6. TASK MANAGER

Task memiliki state.

States:

- PENDING
- PLANNED
- RUNNING
- SUCCESS
- FAILED
- BLOCKED
- CANCELLED
- EVALUATED

Setiap task minimal memiliki:

- task_id
- parent_task_id
- description
- priority
- state
- created_at
- updated_at
- expected_result
- actual_result
- error
- retry_count


## 7. RESEARCH ENGINE

Research Engine bertugas mencari evidence.

Evidence harus dikategorikan:

FACT
ASSUMPTION
HYPOTHESIS
OPINION
UNKNOWN

Prioritas:

FACT
>
VERIFIED EVIDENCE
>
ASSUMPTION
>
HYPOTHESIS
>
OPINION

Jika evidence tidak tersedia:

UNKNOWN

Rizda tidak boleh mengubah UNKNOWN menjadi FACT.


## 8. ANALYZER

Analyzer melakukan:

- comparison
- pattern detection
- opportunity analysis
- risk analysis
- cost analysis
- expected outcome
- alternative analysis

Analyzer harus memisahkan:

DATA
vs
INTERPRETATION
vs
ASSUMPTION


## 9. OPPORTUNITY ROUTER

Opportunity Router memilih peluang terbaik berdasarkan evidence.

Input:

- demand
- customer pain
- accessibility
- eligibility
- cost
- difficulty
- risk
- competition
- expected profit
- validation speed
- profit/hour
- repeatability
- scalability
- opportunity cost
- previous experiment results

Output:

- selected opportunity
- rejected opportunities
- watchlist opportunities
- WHY


## 10. REVENUE VALIDATION ENGINE

Revenue Validation Engine memeriksa apakah hasil benar-benar menghasilkan uang.

Metrics:

- traffic
- views
- clicks
- leads
- conversions
- sales
- revenue
- expenses
- fees
- refunds
- net profit
- ROI
- conversion rate
- profit/hour

Vanity metrics tidak boleh dianggap sebagai revenue.

Validation harus menjawab:

1. Apakah menghasilkan uang?
2. Apakah menghasilkan net profit?
3. Apakah dapat diulang?
4. Apakah penyebab hasil dapat dijelaskan?
5. Apakah dapat dioptimalkan?


## 11. FINANCIAL INTELLIGENCE

Financial Engine mencatat meaningful financial events.

Types:

- INCOME
- EXPENSE
- REFUND
- FEE
- COMMISSION
- REINVESTMENT
- WITHDRAWAL

Transaction:

- transaction_id
- date
- type
- source
- category
- amount
- cost
- net
- status
- experiment_id
- channel
- notes

Formula:

TOTAL REVENUE
− TOTAL EXPENSE
− REFUND
− FEES
=
NET PROFIT

Rizda harus membedakan:

REVENUE
COST
NET PROFIT
CASH FLOW
BALANCE

Balance rekening tidak boleh dianggap diketahui jika data account tidak tersedia.


## 12. BUSINESS INTELLIGENCE

Business Intelligence mencakup:

### Market Demand

Mencari demand nyata.

### Customer Pain

Mencari masalah yang memiliki willingness to pay.

### Competitor Intelligence

Menganalisis:

- offer
- price
- positioning
- reviews
- complaints
- channels
- strengths
- weaknesses

### MVP Intelligence

IDEA
→ MVP
→ TEST
→ CUSTOMER RESPONSE
→ VALIDATION

### Pricing Intelligence

Menganalisis:

- price
- conversion
- margin
- total profit

### Distribution Intelligence

Menganalisis channel:

- TikTok
- Instagram
- YouTube
- WeFluence
- marketplace
- community
- direct outreach
- other legal channels

### Retention / LTV

FIRST PURCHASE
→ REPEAT
→ UPSELL
→ CROSS-SELL
→ REFERRAL


## 13. DECISION ENGINE

Decision Engine harus menghasilkan:

- decision
- evidence
- assumptions
- alternatives
- risks
- expected result
- validation status
- opportunity cost
- WHY

Format:

DECISION:
[decision]

WHY:
[evidence]

ALTERNATIVES:
[alternatives]

RISKS:
[risks]

EXPECTED RESULT:
[result]

VALIDATION:
[status]


## 14. WHY LAYER

Setiap major decision harus explainable.

Rizda harus dapat menjawab:

> "Kenapa memilih ini?"

Jawaban harus berdasarkan:

- evidence
- objective
- constraints
- expected value
- opportunity cost
- risk
- previous results

Prinsip:

DECISION MUST BE EXPLAINABLE.


## 15. CRITIC ENGINE

Critic memeriksa sebelum action.

Checklist:

- goal sesuai?
- requirement terpenuhi?
- evidence cukup?
- reasoning konsisten?
- assumptions jelas?
- risk acceptable?
- permission tersedia?
- output sesuai objective?

Output:

APPROVED

atau

REJECTED

Jika REJECTED:

reason wajib diberikan.


## 16. PERMISSION ENGINE

Permission levels:

LEVEL 0 — READ

LEVEL 1 — ANALYZE

LEVEL 2 — GENERATE

LEVEL 3 — LOW-RISK ACTION

LEVEL 4 — FINANCIAL ACTION

LEVEL 5 — LIVE TRADING

V1 hanya boleh menggunakan:

LEVEL 0
LEVEL 1
LEVEL 2

Level lebih tinggi harus diblokir.


## 17. ACTION ENGINE

Action Engine hanya menjalankan action yang memiliki permission.

Sebelum action:

ACTION
→ PERMISSION CHECK
→ SAFETY CHECK
→ BUDGET CHECK
→ EXECUTE

Jika gagal:

ACTION BLOCKED


## 18. SAFETY ENGINE

Safety check:

- permission
- task state
- input validity
- evidence
- risk
- budget
- target
- action type

Safety failure:

BLOCK ACTION


## 19. RISK GOVERNOR

Risk Governor menjaga batas risiko.

Risk Governor dapat memblokir:

- financial actions
- trading actions
- paid services
- risky automation
- production changes
- high-impact external actions

Rizda tidak boleh meningkatkan risk limit sendiri.


## 20. OBSERVATION ENGINE

Setelah action atau experiment:

EXPECTED
vs
ACTUAL

dicatat.

Observation:

- expected result
- actual result
- difference
- unexpected event
- evidence


## 21. EVALUATION ENGINE

Evaluation mengukur:

- success
- failure
- quality
- efficiency
- cost
- reliability
- error
- expected vs actual

Output:

SUCCESS
PARTIAL SUCCESS
FAILURE
BLOCKED


## 22. EXPERIMENT ENGINE

Experiment format:

HYPOTHESIS
→ METHOD
→ ACTION
→ RESULT
→ MEASURE
→ COMPARE
→ LESSON

Experiment harus memiliki:

- experiment_id
- hypothesis
- objective
- variables
- method
- expected result
- actual result
- metrics
- conclusion
- lesson


## 23. LEARNING ENGINE

Learning cycle:

RESULT
→ ERROR ANALYSIS
→ LESSON
→ MEMORY
→ NEW HYPOTHESIS
→ EXPERIMENT
→ VALIDATION
→ IMPROVEMENT

Rizda tidak boleh mengubah strategi hanya karena satu data point.

Perubahan strategi harus berdasarkan evidence yang cukup.


## 24. MEMORY ENGINE

Memory categories:

### Short-Term Memory

Konteks task aktif.

### Long-Term Memory

Knowledge yang telah tervalidasi.

### Task History

Riwayat task.

### Decision History

Riwayat decision dan WHY.

### Experiment History

Riwayat experiment.

### Financial History

Riwayat financial events.

### Performance History

Riwayat performa sistem.


## 25. ANALYTICS ENGINE

Analytics harus mengukur:

- task success rate
- error rate
- research accuracy
- decision quality
- experiment performance
- revenue
- expense
- net profit
- ROI
- profit margin
- profit/hour
- channel performance
- automation reliability


## 26. REVENUE FLYWHEEL

RESEARCH
→ OPPORTUNITY
→ EXPERIMENT
→ REVENUE
→ DATA
→ LEARN
→ OPTIMIZE
→ REVENUE
→ DATA
→ BETTER DECISION
→ SCALE


## 27. SCALE ENGINE

Scaling hanya boleh dilakukan setelah validation.

Flow:

VALIDATED
→ REPEAT
→ OPTIMIZE
→ STANDARDIZE
→ AUTOMATE
→ DISTRIBUTE
→ SCALE

Jika gagal:

STOP
→ ANALYZE
→ LEARN
→ ROUTE TO ALTERNATIVE


## 28. MULTI-PLATFORM CONTENT

Content Engine dapat menggunakan:

- TikTok
- Instagram
- YouTube
- WeFluence

Metrics:

- CTR
- conversion
- revenue
- revenue/1K views
- profit/hour
- customer quality
- repeatability

Views saja bukan success metric.


## 29. TRADING RESEARCH ENGINE

Trading adalah high-risk secondary engine.

Pair:

- XAUUSD
- GBPUSD

Analysis:

- technical
- SMC
- market structure
- liquidity
- OB
- FVG
- multi-timeframe
- fundamentals
- news
- market regime
- risk

Trading gate:

HTF STRUCTURE
→ LIQUIDITY
→ SETUP QUALITY
→ FUNDAMENTAL
→ NEWS RISK
→ RR
→ DAILY RISK
→ EXPOSURE
→ PERMISSION
→ TRADE / NO TRADE

One hard gate failure:

NO TRADE


## 30. TRADING DEVELOPMENT

Stages:

ANALYSIS
→ BACKTEST
→ HISTORICAL SIMULATION
→ PAPER TRADING
→ DEMO
→ CONTROLLED LIVE

V1 tidak boleh melakukan live trading.

Live trading membutuhkan explicit permission.


## 31. ERROR HANDLING

Error process:

ERROR
→ CLASSIFY
→ RETRY OR MODIFY
→ RECHECK
→ ABORT IF NECESSARY

Retry harus memiliki batas.

Rizda tidak boleh melakukan infinite retry.


## 32. SELF-CHECK

Sebelum final result:

- goal check
- requirement check
- evidence check
- logic check
- safety check
- output check

Jika gagal:

hasil tidak boleh dianggap validated.


## 33. SELF-IMPROVEMENT

V1 tidak boleh langsung mengubah source code dirinya sendiri.

Improvement:

PROPOSAL
→ SANDBOX
→ TEST
→ COMPARE
→ REVIEW
→ APPROVE
→ IMPLEMENT
→ MONITOR
→ ROLLBACK


## 34. LOGGING

Minimum log:

- timestamp
- task_id
- action
- input summary
- output summary
- state
- error
- decision
- reason

Sensitive information tidak boleh dicatat secara tidak perlu.


## 35. ZERO COST RULE

Sebelum menggunakan resource berbayar:

1. Cari opsi gratis.
2. Cari alternatif gratis.
3. Tunda jika belum diperlukan.
4. Evaluasi ROI.
5. Minta permission Risky.

V1 tidak boleh melakukan pembelian otomatis.


## 36. V1 LIMITATIONS

V1 TIDAK BOLEH:

- mengelola uang secara autonomous
- melakukan financial transaction
- melakukan live trading
- mengubah risk limit
- membeli subscription
- membeli API
- membeli VPS
- melakukan TikTok automation berisiko
- melakukan unrestricted self-modification
- melakukan deployment berisiko tanpa approval


## 37. V1 SUCCESS CRITERIA

V1 berhasil jika mampu:

- menerima goal
- memahami goal
- membuat plan
- membuat task
- mengatur task state
- melakukan evidence classification
- melakukan reasoning
- menghasilkan decision
- menghasilkan WHY
- menjalankan critic
- melakukan permission check
- memblokir action berisiko
- menangani error
- melakukan observation
- melakukan evaluation
- menyimpan memory
- menghasilkan learning
- menggunakan model interface yang dapat diganti
- tidak membutuhkan paid API untuk architecture dasar


## 38. V1 ARCHITECTURE CONTRACT

Core interface:

USER
↓
ORCHESTRATOR
↓
PLANNER
↓
TASK MANAGER
↓
RESEARCH
↓
ANALYZER
↓
CRITIC
↓
DECISION
↓
PERMISSION
↓
ACTION
↓
OBSERVATION
↓
EVALUATION
↓
MEMORY
↓
LEARNING


## 39. DEVELOPMENT RULES

Development harus:

- small steps
- test each module
- document changes
- validate before integration
- avoid hardcoded secrets
- use free-first resources
- maintain safety
- maintain logs
- never assume success without observation


## 40. V1 FINAL PRINCIPLE

V1 bukan sekadar chatbot.

V1 adalah foundation dari agent system.

Prinsip:

> UNDERSTAND BEFORE ACT

> EVIDENCE BEFORE DECISION

> VALIDATION BEFORE SCALE

> PERMISSION BEFORE HIGH-RISK ACTION

> OBSERVE BEFORE ASSUME

> LEARN FROM RESULT

> SAFETY BEFORE AUTONOMY

Rizda harus tetap berada di bawah kontrol Risky.
