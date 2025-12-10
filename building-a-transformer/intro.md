# Building a Transformer from Scratch

**An educational journey through the architecture that powers modern AI**

In the previous section, we traced every calculation by hand—forward pass, backward pass, weight updates. You now understand the *math* of transformers at a level most practitioners never reach.

But there's a difference between calculating by hand and building something that runs. In this section, we shift from pencil and paper to PyTorch. We'll build a complete, working transformer from scratch—one you could actually train on real data.

---

In 2017, a team at Google published a paper with an unusually bold title: *"Attention Is All You Need."* The paper introduced the transformer architecture, and it's no exaggeration to say it changed the trajectory of artificial intelligence.

Before transformers, the dominant approach for language tasks was **recurrent neural networks (RNNs)**. RNNs process text sequentially—one word at a time, left to right—maintaining a hidden state that carries information forward. It's intuitive: that's how we read, after all.

But sequential processing has a fatal flaw: **it's slow**. You can't start processing word 5 until you've finished word 4. On modern GPUs—which excel at parallel computation—this is a massive waste.

The transformer's key insight was to replace recurrence with **attention**: a mechanism that lets every position look at every other position simultaneously. Instead of processing sequentially, transformers process all positions in parallel, using learned attention patterns to capture relationships.

This parallelism unlocked scale. Suddenly you could train on billions of tokens. GPT-2, GPT-3, GPT-4, Claude, LLaMA, Gemini—all transformers.

## What We're Building

In this section, we'll build a complete transformer from scratch in PyTorch. Not a toy model that skips the hard parts—the real thing, with every component implemented and explained.

We're building a **decoder-only transformer** (the architecture used by GPT, Claude, and LLaMA). "Decoder-only" means it generates text autoregressively—predicting one token at a time, each prediction conditioned on all previous tokens.

```
Input tokens: [The, cat, sat, on, the]
                    ↓
┌─────────────────────────────────────┐
│     Token Embedding + Position      │
└─────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────┐
│       Transformer Block × N         │
│  ┌────────────────────────────────┐ │
│  │   Multi-Head Self-Attention    │ │
│  │   + Residual + LayerNorm       │ │
│  └────────────────────────────────┘ │
│  ┌────────────────────────────────┐ │
│  │   Feed-Forward Network         │ │
│  │   + Residual + LayerNorm       │ │
│  └────────────────────────────────┘ │
└─────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────┐
│     Final LayerNorm + Linear        │
└─────────────────────────────────────┘
                    ↓
Output logits: [0.1, 0.3, 8.2, ...]
```

## The Learning Path

| Notebook | Topic | What You'll Learn |
|----------|-------|-------------------|
| **Embeddings** | Token Embeddings | How text becomes vectors; positional encoding approaches |
| **Attention** | Scaled Dot-Product | The Q, K, V mechanism; causal masking |
| **Multi-Head** | Multi-Head Attention | Running parallel attention heads |
| **Feed-Forward** | Feed-Forward Networks | The "thinking" layer; GELU activation |
| **Block** | Transformer Block | Combining attention + FFN with residuals |
| **Model** | Complete Model | Stacking blocks; the full forward pass |
| **Training** | Training at Scale | Gradient accumulation; the training loop |
| **KV-Cache** | Efficient Inference | Trading memory for speed |
| **Interpretability** | Looking Inside | Attention patterns, logit lens |

## A Note on Scale

Our model is tiny—about 5-6 million parameters. For context:

| Model | Parameters |
|-------|------------|
| **Our model** | ~5M |
| GPT-2 Small | 117M |
| GPT-3 | 175B |

But here's the beautiful thing: **the architecture is identical**. The same attention mechanism, the same feed-forward structure, the same residual connections. Understanding our 5M parameter model means understanding GPT-3. The math scales; the concepts don't change.

---

By the end of this section, you'll have a working language model that can generate text. But it won't be very *useful*—it predicts tokens, but it doesn't follow instructions. That's the gap we'll close in the next section: fine-tuning.
