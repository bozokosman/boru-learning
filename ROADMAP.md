# Roadmap

> **Kısaca (TR):** Tek plan bu dosya. Önce CS50P sertifikası, sonra SQL, backend, AI ve iş başvurusu. Mini Library her aşamada büyüyen ana proje. İlk işten sonra "Old School" derinlik aşaması başlar. Yeni bir roadmap görürsen bu dosyayı değiştirmeden önce bir hafta bekle ve mentorunla konuş.

**Goal:** Junior backend developer (Python + AI integration), job-ready by autumn 2027.
**Time budget:** ~3-5 hours a week next to a full-time job, usually 2-4 sessions of 60-120 minutes. 10 minutes still counts.
**One project that grows with every stage:** [Mini Library](02-projects/06-mini-library/), from a dictionary menu (July 2026) to a deployed API with AI search. It is the spine, not a cage: one small side project per stage is welcome.
**Where am I?** [NEXT.md](NEXT.md) always holds the single next step.

## Stage 1: Job-ready

| # | When (estimate) | Learn | Mini Library | Output |
|---|---|---|---|---|
| 1 | now → Mar 2027 | **CS50P** (Harvard), weeks 3-9 + final project | V3 → V9 (see below) | CS50P certificate, final project repo |
| 2 | Apr → May 2027 | **SQL**: SQLite, then CS50 SQL lectures | V10: SQLite storage | Queries written by hand, no ORM yet |
| 3 | Jun → Aug 2027 | **Backend**: FastAPI, PostgreSQL, pytest, Docker, deploy | V11: REST API, own repo, deployed | A live API with tests and a README |
| 4 | Sep → Oct 2027 | **AI integration**: LLM APIs directly (structured output, tool calling, embeddings) | V12: natural-language search / recommendations | A small AI feature that really works |
| 5 | Oct → Nov 2027 | **Portfolio**: CV, LinkedIn, GitHub profile, interview practice, applications | - | Applications sent |

Applications can start earlier (from September 2027) with what is already deployed.

### Mini Library through CS50P

| CS50P week | Topic | Mini Library version |
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
4. The folder skeleton is ready in advance (my mentor builds it in seconds), so my time goes to code, not to structure.
5. Old versions are never deleted: v1, v2, v3... show how I learned.
6. Each version gets a short `NOTES.md` entry in my own words: what I got wrong, how I fixed it.
7. This is the only roadmap. A new roadmap or video waits one week before it can change anything here.
8. Work, sleep and family come first. A plan that breaks them is a bad plan.
9. Every session ends with one line in `NEXT.md`.
10. New tools and setups get a one-hour box. They never eat a learning day; if it does not work in an hour, drop it.
11. Before every push: no e-mail, password or API key in the files. Keys are never pasted into a chat; a leaked key is revoked.

## Checkpoints

- **31 Dec 2026:** CS50P week 5 started? Mini Library V5 done?
- **31 Mar 2027:** CS50P certificate.
- **31 Aug 2027:** Mini Library V11 deployed.
- **30 Nov 2027:** Applications out.
