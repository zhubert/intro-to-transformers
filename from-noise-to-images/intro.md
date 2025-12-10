# From Noise to Images

So far, everything we've built has been about language—predicting tokens, following instructions, reasoning through problems. But transformers aren't limited to text.

The same attention mechanism that revolutionized NLP has transformed computer vision. And nowhere is this more visible than in image generation.

---

Every image you've ever seen from Stable Diffusion, Midjourney, or DALL-E started as pure random noise. The magic happens through a **generative model** that learned to transform that noise into coherent images.

In this section, we'll build one from scratch.

## The Problem We're Solving

Here's the setup:

- We have training data (real images)
- We want to sample *new* images from the same distribution
- But we don't know the distribution explicitly—we only have examples

The strategy: learn a **transformation** from a simple distribution (Gaussian noise) to our complex data distribution. If we can learn this transformation, we can generate new samples by:

1. Sample noise
2. Apply our learned transformation
3. Out comes a realistic image

## Why Flow Matching?

Several approaches exist for generative modeling:

| Approach | Core Idea | Challenge |
|----------|-----------|----------|
| **GANs** | Generator fools discriminator | Training instability |
| **VAEs** | Encode/decode through latent space | Blurry outputs |
| **DDPM** | Gradually denoise over many steps | Slow sampling |
| **Flow Matching** | Learn straight paths from noise to data | Simple and fast |

Flow matching has become the preferred choice because:

1. **Simpler mathematics** — no stochastic differential equations
2. **Faster sampling** — straight paths require fewer steps
3. **State-of-the-art results** — used in Stable Diffusion 3, Flux, and more

## The Core Idea

Flow matching constructs a continuous path between noise and data:

$$x_t = (1-t) \cdot x_{\text{data}} + t \cdot x_{\text{noise}}$$

We train a neural network to predict the velocity along this path. Then to generate:

1. Start with pure noise at $t=1$
2. Follow the velocity field backward to $t=0$
3. Arrive at a realistic image

The velocity is constant (straight lines!), which makes everything clean and efficient.

## What We'll Build

| Notebook | Topic | What You'll Learn |
|----------|-------|-------------------|
| **Flow Matching** | The basics | Linear interpolation, velocity fields, Euler sampling |
| **Diffusion Transformer** | DiT architecture | Patchify, adaLN, transformers for images |
| **Class Conditioning** | Controlled generation | Classifier-free guidance |
| **Text Conditioning** | Text-to-image | CLIP encoder, cross-attention |
| **Latent Diffusion** | Scaling up | VAE compression, the Stable Diffusion approach |

By the end, you'll understand how modern image generation works—from the mathematical foundations to the architectural choices that make it practical.

## Prerequisites

This section assumes familiarity with:

- **PyTorch** — tensors, modules, training loops
- **Transformers** — attention, the basics from earlier sections
- **Basic probability** — distributions, sampling

The math gets a bit more involved than the language modeling sections (ODEs, flow equations), but we'll build intuition step by step.

---

This is the final section of the book. By the end, you'll have built transformers for both language and vision—understanding not just *how* they work, but *why* the same architecture succeeds across such different domains.
