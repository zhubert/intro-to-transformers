# Fine-Tuning a Transformer

**Or: How to teach a parrot to be a helpful assistant**

You've built a transformer from scratch. It can predict the next token, generate text, even learn patterns in training data. But try asking it a question—it'll just ramble on, continuing your text rather than answering.

That's because our model learned to *predict*, not to *help*. The gap between a capable language model and a useful assistant? That's what this section is about.

---

You know how GPT-4 and Claude can follow your instructions, answer questions, and refuse to help you build a bomb? That's not magic. That's post-training.

And we're going to build it from scratch.

## What is Post-Training, Really?

Imagine you've trained a really smart parrot to predict what word comes next in any sentence. You feed it the entire internet, and boom — it can complete any text you throw at it. Impressive!

But here's the thing: that parrot doesn't know it's supposed to *help* you. Ask it "What's the capital of France?" and it might just continue with "What's the capital of Germany? What's the capital of Italy?" Because that's what text on the internet looks like — lists of similar questions.

This is the problem with **pre-trained models**. They're brilliant at language, but they don't know they're supposed to be assistants.

**Post-training** is how we fix this. It's the process of teaching a pre-trained language model to:

- **Follow instructions** — When you ask a question, answer it
- **Align with human preferences** — Generate responses humans actually like
- **Refuse harmful requests** — Say "no" to dangerous tasks
- **Be truthful** — Admit when it doesn't know something

Think of it like this: pre-training teaches you grammar and vocabulary by reading every book in the library. Post-training is like going to charm school to learn *how to have a conversation*.

## The Post-Training Pipeline

Modern AI assistants all go through the same basic journey:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        STAGE 1: PRE-TRAINING                        │
│  Train on massive text corpus                                       │
│  Result: A really good autocomplete                                 │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│              STAGE 2: SUPERVISED FINE-TUNING (SFT)                  │
│  Train on (instruction → response) examples                         │
│  Result: A model that acts like an assistant                        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│              STAGE 3: PREFERENCE ALIGNMENT                          │
│  RLHF or DPO to match human preferences                             │
│  Result: A model that's helpful, harmless, and honest               │
└─────────────────────────────────────────────────────────────────────┘
```

## What You'll Learn

We're going to implement the complete post-training pipeline:

| Section | What It Does |
|---------|--------------|
| **SFT** | Train a model to follow instructions using example conversations |
| **Reward Modeling** | Teach a model to predict which responses humans prefer |
| **RLHF with PPO** | Use reinforcement learning to optimize for human preferences |
| **DPO** | A simpler, more stable alternative to RLHF |
| **Advanced Topics** | Memory optimization, hyperparameters, evaluation |

## The Three Training Methods

### Supervised Fine-Tuning (SFT)

Show the model good examples and train it to imitate them. Simple, effective, but limited by your examples.

### Reinforcement Learning from Human Feedback (RLHF)

Train a reward model to predict human preferences, then use PPO to optimize for high reward. Powerful but complex—you need two models and careful tuning.

### Direct Preference Optimization (DPO)

Skip the reward model entirely. Directly optimize on preference pairs. Same results as RLHF, much simpler implementation.

By the end, you'll understand exactly how models like GPT-4 and Claude are built. Not just conceptually—you'll have working code.

---

A fine-tuned model can follow instructions and align with preferences. But what about *hard* problems—math, logic, multi-step planning? For that, we need to teach models to reason. That's coming up next.
