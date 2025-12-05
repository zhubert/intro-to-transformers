# An Introduction to Transformers

**Understanding Modern AI from the Inside Out**

This book teaches you how modern AI systems work by building them yourself. No black boxes—just the actual math and code that powers language models and image generators.

## What You'll Find Here

### Understanding Gradients

Calculate a complete transformer forward and backward pass **by hand**. Using only basic Python (no NumPy, no PyTorch), you'll compute every matrix multiplication, every activation function, every gradient. By the end, you'll understand transformers not because someone explained them in abstract terms, but because you calculated every operation yourself.

| Chapter | What You'll Learn |
|---------|-------------------|
| Tokenization & Embeddings | How text becomes vectors |
| QKV Projections | What Query, Key, Value actually mean |
| Attention | The softmax-weighted sum that made transformers possible |
| Multi-Head Attention | Running parallel attention operations |
| Feed-Forward Network | The MLP that processes attended information |
| Layer Normalization | Stabilizing activations for training |
| Loss & Gradients | Cross-entropy and the backward pass |
| AdamW Optimizer | How weights actually get updated |

### Building a Transformer

Build a complete GPT-style transformer in PyTorch. This section covers the architecture that powers modern language models, from embeddings to interpretability tools.

| Chapter | What You'll Learn |
|---------|-------------------|
| Embeddings & Positions | Token embeddings, ALiBi, RoPE |
| Attention | Scaled dot-product attention with causal masking |
| Multi-Head Attention | Parallel attention heads |
| Transformer Block | Pre-LN, residuals, and all components combined |
| Training | Gradient accumulation, validation splits |
| KV-Cache | Fast inference through caching |
| Interpretability | Logit lens, attention analysis, induction heads |

### From Noise to Images

Learn how AI generates images from text prompts. This section builds from flow matching fundamentals to a working latent diffusion model.

| Phase | What You'll Learn |
|-------|-------------------|
| Flow Matching | Velocity fields, noise-to-data paths |
| Diffusion Transformer | Patchifying images, attention for generation |
| Class Conditioning | Classifier-free guidance (CFG) |
| Text Conditioning | CLIP embeddings, cross-attention |
| Latent Diffusion | VAE compression, scaling to larger images |

## Philosophy

These materials follow a simple principle: **the best way to understand something is to build it yourself**.

- No hand-waving. Every operation is explicit.
- No magic. You see exactly what the computer sees.
- No shortcuts. Understanding comes from doing the work.

The architecture that powers GPT, Claude, Stable Diffusion, and other frontier models isn't beyond comprehension. It's just matrix multiplications, attention mechanisms, and optimization—repeated at scale.

Let's see how it works.
