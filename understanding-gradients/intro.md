# Understanding Gradients

**A mathematically meticulous forward and backward pass through a transformer**

There's a gap between *using* something and *understanding* it. You can drive a car without knowing how combustion engines work. You can use PyTorch without knowing what `loss.backward()` actually computes.

But if you want to *design* cars, you need thermodynamics. And if you want to design new architectures, debug training instabilities, or just satisfy your own curiosity about how these models actually learn... you need to understand the math.

This section closes that gap.

## What We're Going to Do

We're going to calculate—by hand, step by step—a complete training iteration through a transformer.

Not a simplified version. Not pseudocode. The actual math, with actual numbers, showing every matrix multiplication, every activation function, every gradient.

We'll take the sentence "I like transformers" through a tiny language model:

1. **Forward pass**: Convert text to numbers, flow through attention and feed-forward layers, compute how wrong our predictions are
2. **Backward pass**: Calculate gradients—how much each parameter contributed to the error
3. **Optimization**: Update all ~2,600 parameters to make the model slightly less wrong

By the end, you'll understand exactly what happens inside a transformer. Not abstractly. Concretely, with numbers you can verify yourself.

## A Tiny Model (Same Math, Smaller Numbers)

Real transformers are huge. GPT-3 has 175 billion parameters. You can't write out a 12,288-dimensional vector by hand.

So we're building a tiny transformer with the exact same architecture, just scaled down to human-tractable dimensions:

| What | Our Model | GPT-3 |
|------|-----------|-------|
| **Embedding dimension** | 16 | 12,288 |
| **Attention heads** | 2 | 96 |
| **Feed-forward hidden size** | 64 | 49,152 |
| **Vocabulary** | 6 tokens | 50,257 tokens |
| **Layers** | 1 | 96 |
| **Total parameters** | ~2,600 | 175 billion |

The math is identical. When you multiply a 5×16 matrix by a 16×8 matrix, the operation is the same whether those 16s are 16 or 12,288. We're just keeping the numbers small enough that you can see what's happening.

## What You'll Need

**Math background**: Basic calculus (derivatives, chain rule, partial derivatives) and linear algebra (matrix multiplication, vectors). If you remember what a dot product is and can take a derivative, you're good.

**Programming**: We use pure Python—no NumPy, no PyTorch. Everything is explicit lists and loops so you can see exactly what's happening.

**Patience**: Some notebooks have a lot of numbers. That's the point. You don't have to verify every calculation, but knowing you *could* is what makes this different from a high-level explanation.

## The Notebooks

### Forward Pass

| Notebook | What We Calculate |
|----------|-------------------|
| Tokenization & Embeddings | Convert "I like transformers" to vectors |
| QKV Projections | Create Query, Key, Value representations |
| Attention | Compute how much each token attends to others |
| Multi-Head Attention | Combine multiple attention "perspectives" |
| Feed-Forward Network | Apply non-linear transformations |
| Layer Normalization | Stabilize activations with residual connections |
| Cross-Entropy Loss | Measure prediction error |

### Backward Pass

| Notebook | What We Calculate |
|----------|-------------------|
| Loss Gradients | Gradient of loss with respect to output logits |
| Backpropagation | Gradients for every layer via chain rule |

### Optimization

| Notebook | What We Calculate |
|----------|-------------------|
| AdamW Optimizer | Update all parameters using adaptive learning rates |

---

Once you've traced every calculation by hand, you'll be ready to build a real, working transformer in PyTorch—which is exactly what we'll do in the next section.
