# An Introduction to Transformers

:::{pull-quote}
**Understanding Modern AI from the Inside Out**

This book teaches you how modern AI systems work by building them yourself. No black boxes—just the actual math and code that powers language models and image generators.
:::

## What You'll Find Here

---

### Understanding Gradients

Calculate a complete transformer forward and backward pass **by hand**. Using only basic Python (no NumPy, no PyTorch), you'll compute every matrix multiplication, every activation function, every gradient. By the end, you'll understand transformers not because someone explained them in abstract terms, but because you calculated every operation yourself. Feel free to skip this one if you want to be pragmatic.

::::{grid} 1 1 2 2

:::{grid-item-card} Tokenization & Embeddings
:link: understanding-gradients/01_tokenization_embeddings.ipynb
How text becomes vectors
:::

:::{grid-item-card} QKV Projections
:link: understanding-gradients/02_qkv_projections.ipynb
What Query, Key, Value actually mean
:::

:::{grid-item-card} Attention
:link: understanding-gradients/03_attention.ipynb
The softmax-weighted sum that made transformers possible
:::

:::{grid-item-card} Multi-Head Attention
:link: understanding-gradients/04_multi_head.ipynb
Running parallel attention operations
:::

:::{grid-item-card} Feed-Forward Network
:link: understanding-gradients/05_feedforward.ipynb
The MLP that processes attended information
:::

:::{grid-item-card} Layer Normalization
:link: understanding-gradients/06_layer_norm.ipynb
Stabilizing activations for training
:::

:::{grid-item-card} Loss & Gradients
:link: understanding-gradients/07_loss.ipynb
Cross-entropy and the backward pass
:::

:::{grid-item-card} AdamW Optimizer
:link: understanding-gradients/10_optimizer.ipynb
How weights actually get updated
:::
::::

---

### Building a Transformer

Not exactly unique, but this section shows you how to build a complete GPT-style transformer in PyTorch. It covers the architecture that powers modern language models (circa 2023), from embeddings to interpretability tools.

::::{grid} 1 1 2 2

:::{grid-item-card} Embeddings & Positions
:link: building-a-transformer/01_embeddings.ipynb
Token embeddings, ALiBi, RoPE
:::

:::{grid-item-card} Attention
:link: building-a-transformer/02_attention.ipynb
Scaled dot-product attention with causal masking
:::

:::{grid-item-card} Multi-Head Attention
:link: building-a-transformer/03_multi_head_attention.ipynb
Parallel attention heads
:::

:::{grid-item-card} Transformer Block
:link: building-a-transformer/05_transformer_block.ipynb
Pre-LN, residuals, and all components combined
:::

:::{grid-item-card} Training
:link: building-a-transformer/07_training.ipynb
Gradient accumulation, validation splits
:::

:::{grid-item-card} KV-Cache
:link: building-a-transformer/08_kv_cache.ipynb
Fast inference through caching
:::

:::{grid-item-card} Interpretability
:link: building-a-transformer/09_interpretability.ipynb
Logit lens, attention analysis, induction heads
:::
::::

---

### Fine-Tuning a Transformer

Fine-tuning really should be called "necessary tuning" because the output of the previous section doesn't look anything like the GPT-style assistants you are used to. As such, this section teaches a baseline pre-trained model to follow instructions. We go into detail on SFT, reward modeling, RLHF with PPO, DPO, and other acronyms we will explain later—the techniques that turn base models into safe assistants.

::::{grid} 1 1 2 2

:::{grid-item-card} Supervised Fine-Tuning
:link: fine-tuning-a-transformer/03_sft_introduction.ipynb
Instruction formatting, loss masking, LoRA
:::

:::{grid-item-card} Reward Modeling
:link: fine-tuning-a-transformer/08_reward_introduction.ipynb
Preference data and training reward models
:::

:::{grid-item-card} RLHF
:link: fine-tuning-a-transformer/12_rlhf_introduction.ipynb
PPO algorithm, KL penalty, training dynamics
:::

:::{grid-item-card} DPO
:link: fine-tuning-a-transformer/17_dpo_introduction.ipynb
Direct preference optimization without RL
:::
::::

---

### From Noise to Images

Neat. But what if we aren't generating text but want a different medium? Here we will learn how AI generates images from text prompts. This section builds from flow matching fundamentals to a working latent diffusion model (you'll know what that means later).

::::{grid} 1 1 2 2

:::{grid-item-card} Flow Matching
:link: from-noise-to-images/01_flow_matching_basics.ipynb
Velocity fields, noise-to-data paths
:::

:::{grid-item-card} Diffusion Transformer
:link: from-noise-to-images/02_diffusion_transformer.ipynb
Patchifying images, attention for generation
:::

:::{grid-item-card} Class Conditioning
:link: from-noise-to-images/03_class_conditioning.ipynb
Classifier-free guidance (CFG)
:::

:::{grid-item-card} Text Conditioning
:link: from-noise-to-images/04_text_conditioning.ipynb
CLIP embeddings, cross-attention
:::

:::{grid-item-card} Latent Diffusion
:link: from-noise-to-images/05_latent_diffusion.ipynb
VAE compression, scaling to larger images
:::
::::
