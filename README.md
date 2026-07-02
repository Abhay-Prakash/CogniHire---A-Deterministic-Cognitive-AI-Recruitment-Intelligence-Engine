# CogniHire---A-Deterministic-Cognitive-AI-Recruitment-Intelligence-Engine

# CogniHire
### Deterministic Cognitive Intelligence for Explainable Hiring

> An enterprise-grade, graph-driven recruitment intelligence engine that transforms resumes into explainable hiring decisions through deterministic cognitive reasoning instead of black-box AI.


# 📖 Executive Summary

**Veritas Recruit** is a deterministic, explainable AI recruitment engine developed for the **India Runs Data & AI Challenge**.

Unlike traditional Applicant Tracking Systems (ATS) that depend on keyword matching or opaque machine learning models, Veritas Recruit models the hiring process as a structured cognitive reasoning pipeline. Every recommendation is derived through evidence-based inference and can be traced back to the exact resume content that produced it.

The architecture emphasizes:

- Deterministic decision making
- Explainable AI
- Graph-based reasoning
- Streaming scalability
- Zero runtime LLM dependency
- Complete provenance and auditability

---

# 🚀 Key Features

- ✅ Deterministic cognitive reasoning pipeline
- ✅ Evidence-driven candidate evaluation
- ✅ Graph-based recruiter cognition
- ✅ Complete provenance tracking
- ✅ O(1) streaming architecture
- ✅ Zero runtime hallucinations
- ✅ Modular and extensible design
- ✅ Competition-ready submission generation

---

# 🎯 Problem Statement

Modern ATS systems primarily rely on keyword matching, resulting in poor explainability, susceptibility to keyword stuffing, and limited understanding of candidate context.

Veritas Recruit addresses these limitations through deterministic evidence extraction and cognitive reasoning.

| Traditional ATS | Veritas Recruit |
|-----------------|----------------|
| Keyword Matching | Evidence-Based Reasoning |
| Black Box Scoring | Fully Explainable Decisions |
| Duplicate Keywords Increase Score | Confidence Saturation |
| No Provenance | Complete Evidence Trace |
| Static Ranking | Cognitive Inference Pipeline |
| Difficult to Audit | Fully Deterministic |

---

# 💡 Solution Overview

The system models recruiter reasoning as a sequence of deterministic transformations:

```text
Resume
   │
Validation
   │
Knowledge Base
   │
Evidence Extraction
   │
Evidence Graph
   │
Belief Engine
   │
Contradiction Engine
   │
Belief Ecology
   │
Trait Engine
   │
Reflection Engine
   │
Probability Engine
   │
Ranking Engine
   │
Final Recommendation
```

Every stage is immutable, deterministic, and independently testable.

---

# 🏗 Architecture Overview

| Layer | Responsibility |
|--------|----------------|
| Foundation | Validation & Streaming |
| Knowledge | Canonical Ontologies |
| Evidence | Atomic Observation Extraction |
| Graph | Structural Relationships |
| Beliefs | Recruiter Interpretation |
| Contradictions | Logical Consistency |
| Ecology | Belief Competition & Decay |
| Traits | Candidate Abstraction |
| Reflection | Confidence Audit |
| Scoring | Hiring Probability |
| Ranking | Top-K Candidate Selection |

---

# 🧠 Cognitive Pipeline

| Stage | Input | Output |
|---------|--------|---------|
| Validation | Raw JSON | Validated Candidate |
| Knowledge Base | Raw Strings | Canonical Enums |
| Evidence Extraction | Candidate | Evidence Objects |
| Evidence Graph | Evidence | Directed Graph |
| Belief Engine | Graph | Belief Graph |
| Contradiction Engine | Beliefs | Revised Beliefs |
| Belief Ecology | Beliefs | Stable Beliefs |
| Trait Engine | Stable Beliefs | Trait Graph |
| Reflection Engine | Traits | Reflection State |
| Probability Engine | Reflection | Hiring Score |
| Ranking Engine | Scores | Ranked Candidates |

---

# 📂 Repository Structure

```text
code/
├── core/
├── common/
├── stream_io/
├── validation/
├── knowledge/
├── inference/
│   ├── evidence/
│   ├── evidence_graph/
│   ├── beliefs/
│   ├── contradictions/
│   ├── ecology/
│   ├── traits/
│   └── reflection/
├── scoring/
├── cli/
└── tests/
```

---

# 📦 Core Components

| Module | Purpose |
|----------|---------|
| Validation | Schema verification & honeypot detection |
| Knowledge | Ontologies & registries |
| Evidence | Resume signal extraction |
| Evidence Graph | Relationship modeling |
| Beliefs | Cognitive interpretation |
| Contradictions | Logical consistency |
| Ecology | Belief competition |
| Traits | Candidate synthesis |
| Reflection | Explainability audit |
| Probability | Hiring likelihood |
| Ranking | Top candidate selection |

---

# 📐 Mathematical Foundations

The system uses deterministic mathematical models throughout the pipeline.

### Confidence Saturation

```
C = 1 - e^(-kW)
```

Duplicate evidence increases confidence while preventing keyword stuffing.

### Hiring Probability

```
Hiring Score

=

Fit
×

Integrity
×

Availability
×

Evidence Sufficiency
```

---

# 🔍 Explainability

Every recommendation is fully traceable.

```text
Recommendation
      │
Trait
      │
Belief
      │
Evidence
      │
JSON Path
      │
Original Resume
```

No recommendation can exist without supporting evidence.

---

# ⚙️ Complexity Analysis

| Module | Time | Space |
|----------|------|-------|
| Streaming | O(N) | O(1) |
| Validation | O(K) | O(1) |
| Registry Lookup | O(1) | O(1) |
| Evidence Extraction | O(E) | O(1) |
| Evidence Graph | O(E) | O(1) |
| Belief Engine | O(B) | O(1) |
| Contradiction Engine | O(B²) | O(1) |
| Belief Ecology | O(B log B) | O(1) |
| Trait Engine | O(T) | O(1) |
| Reflection | O(T+B+C) | O(1) |
| Ranking | O(log K) | O(K) |

---

# 📈 Performance

The architecture is designed for large-scale recruitment workloads.

| Property | Value |
|-----------|-------|
| Processing Mode | Streaming |
| Memory Complexity | O(1) |
| Ranking Strategy | Min Heap |
| Explainability | 100% |
| Runtime LLM | None |
| Provenance | Complete |

Generated runtime metrics and profiling artifacts are available in the `reports/` and `assets/` directories.

---

# 🛠 Technologies

| Category | Technology |
|------------|------------|
| Language | Python |
| Graph Processing | NetworkX |
| Visualization | Matplotlib |
| Data Format | JSONL |
| Testing | PyTest |
| Profiling | Tracemalloc |
| Static Typing | MyPy |
| Formatting | Black |

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/<username>/veritas-recruit.git
cd veritas-recruit
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Pipeline

```bash
python code/cli/main.py \
    --input candidates.jsonl \
    --output outputs/submission.csv
```

---

# 📊 Outputs

```
outputs/
├── submission.csv
├── runtime_metrics.json
├── validation_summary.json
├── profiling.json
└── reports/
```

---

# 🧪 Testing

Run the complete test suite:

```bash
pytest code/tests/
```

Type checking:

```bash
mypy code/
```

Formatting:

```bash
black code/
```

Linting:

```bash
flake8 code/
```

---

# 🏆 Competition Deliverables

- ✅ Deterministic AI Recruitment Engine
- ✅ Explainable Cognitive Pipeline
- ✅ Streaming Resume Processing
- ✅ Candidate Ranking
- ✅ Submission CSV
- ✅ Engineering Documentation
- ✅ Presentation Assets
- ✅ Technical Pitch Deck

---

# 🔮 Future Roadmap

- Embedding-assisted ontology expansion
- YAML-driven rule configuration
- Interactive recruiter dashboard
- REST API deployment
- Docker & Kubernetes support
- Multi-domain hiring models

---

# 👨‍💻 Author

**Abhay Prakash**

B.Tech, Computer Science & Engineering  
ITER, Siksha 'O' Anusandhan University

---

# 🙏 Acknowledgements

Developed for the **India Runs Data & AI Challenge**.

Special thanks to the organizers for providing the recruitment dataset and challenge framework.

---

# 📄 License

This repository was developed as part of the India Runs Data & AI Challenge and is intended for academic, research, and demonstration purposes.

---

## ⭐ If you found this project interesting, consider giving it a star!
