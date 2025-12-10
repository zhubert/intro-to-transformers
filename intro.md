# An Introduction to Transformers

:::{pull-quote}
**Understanding Transformers from the Inside Out**

This book teaches you how fairly modern AI systems work by building miniature versions of them yourself. I don't want to hand wave anything, because I'm learning this as we go too. Real math, straightforward code...that's the goal.
:::

## What You'll Find Here

---

### Understanding Gradients

Using only basic Python (no NumPy, no PyTorch), we'll compute every matrix multiplication, every activation function, every gradient. If you want to be pragmatic, you can skip this one and go to the next section. But if you want to reach for glory which is meticulous mathematical matrix multiplications, then get ready to calculate!

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

This is our transformer. There are many like it, but this one is ours. This section shows you how to build a complete GPT-style transformer in PyTorch. All that heavy lifting we did in the last section is now hidden behind simple `backward()`-like calls. It covers the architecture that powers modern language models (circa 2023), from embeddings to interpretability tools. In the end, you'll have a new toy.

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

Fine-tuning really should be called "necessary tuning" because the output of the previous section doesn't look anything like the GPT-style assistants we are used to. As such, this section teaches a baseline pre-trained model to follow instructions. We go into detail on SFT, reward modeling, RLHF with PPO, DPO, and other acronyms we will explain later, the techniques that turn base models into safer assistants.

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

But what if we aren't generating text? Here we will learn how AI generates images from text prompts. This section builds from flow matching fundamentals to a working latent diffusion model (you'll know what that means later).

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

---

### Reasoning with Transformers

How do models like o1 and DeepSeek-R1 "think"? This section covers the techniques that make transformers reason: from simple prompting tricks to full reinforcement learning pipelines. We'll build chain-of-thought, tree search, and train our own reasoning models.

::::{grid} 1 1 2 2

:::{grid-item-card} Chain-of-Thought
:link: reasoning-with-transformers/01_chain_of_thought.ipynb
The simple prompt that started it all
:::

:::{grid-item-card} Self-Consistency
:link: reasoning-with-transformers/02_self_consistency.ipynb
Sample many reasoning paths, vote on the answer
:::

:::{grid-item-card} Tree of Thoughts
:link: reasoning-with-transformers/03_tree_of_thoughts.ipynb
Explore and backtrack through reasoning trees
:::

:::{grid-item-card} Process Reward Models
:link: reasoning-with-transformers/04_process_reward_model.ipynb
Score each reasoning step, not just the answer
:::

:::{grid-item-card} Best-of-N Verification
:link: reasoning-with-transformers/05_best_of_n.ipynb
Generate many solutions, pick the best
:::

:::{grid-item-card} Monte Carlo Tree Search
:link: reasoning-with-transformers/06_mcts.ipynb
The algorithm that powered AlphaGo, for language
:::

:::{grid-item-card} Budget Forcing
:link: reasoning-with-transformers/07_budget_forcing.ipynb
Control how long the model "thinks"
:::

:::{grid-item-card} GRPO Training
:link: reasoning-with-transformers/08_grpo.ipynb
RL for reasoning without a critic
:::

:::{grid-item-card} Reasoning Distillation
:link: reasoning-with-transformers/09_distillation.ipynb
Transfer reasoning to smaller models
:::
::::
