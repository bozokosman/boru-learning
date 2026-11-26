# Roadmap

> **Kısaca (TR):** Tek plan bu dosya. Önce CS50P, tamamı ve sadece o. Bitince boru-learning'e yüklenme dönemi: Mini Library CS50P'de öğrendiklerimle V4'ten V9'a büyür. Sonra SQL, backend, AI ve iş başvurusu. Mini Library her aşamada büyüyen ana proje. İlk işten sonra "Old School" derinlik aşaması başlar. Yeni bir roadmap görürsen bu dosyayı değiştirmeden önce bir hafta bekle ve mentorunla konuş.

**Goal:** Junior backend developer (Python + AI integration), job-ready by early 2028.
**Focus rule:** one thing at a time. CS50P first, completely. Everything else waits.
**Time budget:** ~3-5 hours a week next to a full-time job, usually 2-4 sessions of 60-120 minutes. 10 minutes still counts.
**One project that grows with every stage:** [Mini Library](02-projects/06-mini-library/), from a dictionary menu (July 2026) to a deployed API with AI search. It is the spine, not a cage: one small side project per stage is welcome.
**Where am I?** [NEXT.md](NEXT.md) always holds the single next step.

## Stage 1: Job-ready

| # | When (estimate) | Learn | Mini Library | Output |
|---|---|---|---|---|
| 1 | now → Mar 2027 | **CS50P** (Harvard), weeks 3-9 + final project. Only CS50P. | waits | CS50P certificate, final project repo |
| 2 | Apr → May 2027 | **Python sprint in this repo**: every CS50P topic applied to my own code, notes in `01-python/04-09` | V3 → V9 (see below) | Mini Library V9, topic notes in my own words |
| 3 | Jun → Jul 2027 | **SQL**: SQLite, then CS50 SQL lectures | V10: SQLite storage | Queries written by hand, no ORM yet |
| 4 | Aug → Oct 2027 | **Backend**: FastAPI, PostgreSQL, pytest, Docker, deploy | V11: REST API, own repo, deployed | A live API with tests and a README |
| 5 | Nov → Dec 2027 | **AI integration**: LLM APIs directly (structured output, tool calling, embeddings) | V12: natural-language search / recommendations | A small AI feature that really works |
| 6 | Jan 2028 | **Portfolio**: CV, LinkedIn, GitHub profile, interview practice, applications | - | Applications sent |

Applications can start earlier (from autumn 2027) with what is already deployed.

### Mini Library after CS50P (stage 2 sprint)

| CS50P week I learned it in | Topic | Mini Library version |
|---|---|---|
| 3 | Exceptions | V3: finish `search_book()`. V4: handle bad input with `try/except` |
| 4 | Libraries | V5: use a library (e.g. `random` "book of the day", or a public book API with `requests`) |
| 5 | Unit tests | V6: first `pytest` tests |
| 6 | File I/O | V7: save and load books (JSON or CSV) |
| 7 | Regular expressions | V8: validate ISBN and e-mail |
| 8 | Object-oriented programming | V9: `Librarian`, `Member`, `Loan` classes |
| 9 | Et cetera | refactor, clean up, write the V1 → V9 story in `PROJECT_EVOLUTION.md` |

CS50P problem sets stay in a separate private repo (CS50's academic honesty rules). Only my own projects and notes are here.

## Stage 2: Old School (after the first job)

The deep foundations, no rush, a lifetime project:
computer architecture, operating systems and Linux, networking, data structures and algorithms, system design, a systems language (C or Rust), open source contributions.
My notes from Stage 1 (what I misunderstood and how I fixed it) are the raw material for a future book: *"written by someone starting over from zero."*

## Rules

1. I write the code. AI is a teacher and a reviewer, not an author: hints and questions, no code. Stuck for 15 minutes? Ask for a hint, not for the answer.
2. Every topic ends with something I built, not something I watched. A new topic means rewriting a project I already know with the new tool (that is how Calculator v1-v4 happened).
3. A missed day is fine; try not to miss two in a row. After a longer break, come back small: run the last code, read `NEXT.md`, no guilt.
4. The folder skeleton is ready in advance (my mentor builds it in seconds), so my time goes to learning, not to structure.
5. Old versions are never deleted: v1, v2, v3... show how I learned.
6. Each version gets a short `NOTES.md` entry in my own words: what I got wrong, how I fixed it.
7. This is the only roadmap. A new roadmap or video waits one week before it can change anything here.
8. Work, sleep and family come first. A plan that breaks them is a bad plan.
9. Every session ends with one line in `NEXT.md`.
10. New tools and setups get a one-hour box. They never eat a learning day; if it does not work in an hour, drop it.
11. Before every push: no e-mail, password or API key in the files. Keys are never pasted into a chat; a leaked key is revoked.

## Checkpoints

- **31 Dec 2026:** CS50P week 5 started?
- **31 Mar 2027:** CS50P certificate (hard deadline from CS50: 30 Jun 2027).
- **31 May 2027:** Mini Library V9.
- **31 Oct 2027:** Mini Library V11 deployed.
- **31 Jan 2028:** Applications out.
