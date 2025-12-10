# Reasoning with Transformers

We've fine-tuned our model to follow instructions. It answers questions, follows formats, even refuses harmful requests. But there's a ceiling.

Ask it to solve a math problem, plan a complex task, or reason through a logic puzzle—and it struggles. Not because it lacks knowledge, but because it lacks *thinking time*.

---

Language models generate one token at a time, left to right, with no scratch paper. For simple factual recall, this works fine. But for multi-step problems—math, logic, planning—the model needs to *compute* the answer, not just recall it.

The breakthrough: if models generate intermediate reasoning steps before the final answer, their accuracy on hard problems improves dramatically. A model that "thinks out loud" can solve problems that stump models forced to answer immediately.

This section covers the techniques that make this possible.

## The Problem with Instant Answers

When asked a question, the model must *commit* to its answer immediately. There's no scratch paper. No thinking time. Just token after token.

For simple questions, this works. But for anything requiring multiple steps, performance degrades quickly.

Consider: "If a train leaves Chicago at 9am going 60mph, and another train leaves New York at 10am going 80mph, when do they meet?"

The model can't just *know* the answer. It needs to figure out the distance, account for the time offset, set up equations, solve them. If it tries to output the answer immediately, it's guessing.

## The Solution: Think Out Loud

The key insight that changed the field:

**The model's reasoning ability is bottlenecked by output length, not parameter count.**

A smaller model that "thinks" for 1,000 tokens can outperform a larger model that answers in 10 tokens.

```
Without Chain-of-Thought:
Q: What's 17 × 24?
A: 408  ← Just guessing. Often wrong.

With Chain-of-Thought:
Q: What's 17 × 24?
A: Let me work through this.
   17 × 24 = 17 × (20 + 4)
           = 340 + 68
           = 408  ← Actually correct!
```

Same model. Same parameters. But by generating intermediate steps, it can actually *compute* the answer instead of guessing.

## The Paradigm Shift: Test-Time Compute

For years, the recipe for better AI was simple: train bigger models on more data.

A new idea has emerged: **test-time compute scaling**. Instead of making the model bigger, let it **think longer**.

The math is compelling. Researchers found that on reasoning problems, using extra compute at inference time can outperform a model that's 14x larger.

This is the approach powering models like OpenAI's o1, DeepSeek-R1, and Google's Gemini Flash Thinking. They don't just generate answers—they *reason* first.

## What We'll Build

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PROMPTING-BASED REASONING                        │
├─────────────────────────────────────────────────────────────────────┤
│  Chain-of-Thought      │ "Let's think step by step"                 │
│  Self-Consistency      │ Sample many chains, vote on the answer     │
│  Tree of Thoughts      │ Explore multiple paths, backtrack          │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    VERIFICATION & SEARCH                            │
├─────────────────────────────────────────────────────────────────────┤
│  Process Reward Model  │ Score each reasoning step                  │
│  Best-of-N Sampling    │ Generate N solutions, pick the best        │
│  Monte Carlo Search    │ Tree search with learned heuristics        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    TRAINING REASONING MODELS                        │
├─────────────────────────────────────────────────────────────────────┤
│  Budget Forcing        │ Force longer thinking with "Wait" tokens   │
│  GRPO                  │ RL without a critic (DeepSeek's approach)  │
│  Distillation          │ Transfer reasoning to smaller models       │
└─────────────────────────────────────────────────────────────────────┘
```

## The Roadmap

| Notebook | Topic | Key Idea |
|----------|-------|----------|
| Chain-of-Thought | Prompting models to show their work |
| Self-Consistency | Sampling multiple chains, majority voting |
| Tree of Thoughts | Exploring and pruning reasoning paths |
| Process Reward Models | Scoring individual reasoning steps |
| Best-of-N | Using PRMs to select best solutions |
| Monte Carlo Tree Search | Search algorithms for reasoning |
| Budget Forcing | Controlling reasoning length |
| GRPO Training | RL without a critic |
| Reasoning Distillation | Transferring reasoning to smaller models |

Each notebook is self-contained, but they build on each other conceptually.

---

With reasoning complete, we've covered everything transformers can do with language. But the architecture isn't limited to text—in the final section, we'll see how the same attention mechanism powers image generation.
