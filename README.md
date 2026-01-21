# An Introduction to Transformers

**Understanding Modern AI from the Inside Out**

This is an educational resource that teaches how modern AI systems work by building them yourself. No black boxes - just the actual math and code that powers language models and image generators.

📖 **[Read Online](https://www.zhubert.com/intro-to-transformers/)**

## What's Inside

### Understanding Gradients

Calculate a complete transformer forward and backward pass **by hand**. Using only basic Python (no NumPy, no PyTorch), you compute every matrix multiplication, every activation function, every gradient. By the end, you understand transformers not because someone explained them in abstract terms, but because you calculated every operation yourself.

- Tokenization & Embeddings - How text becomes vectors
- QKV Projections - What Query, Key, Value actually mean
- Attention - The softmax-weighted sum that made transformers possible
- Multi-Head Attention - Running parallel attention operations
- Feed-Forward Network - The MLP that processes attended information
- Layer Normalization - Stabilizing activations for training
- Cross-Entropy Loss - Measuring prediction quality
- Loss Gradients & Backpropagation - The complete backward pass
- AdamW Optimizer - How weights actually get updated

### Building a Transformer

Build a complete GPT-style transformer in PyTorch. This section covers the architecture that powers modern language models, from embeddings to interpretability tools.

- Embeddings & Positions - Token embeddings, ALiBi, RoPE
- Scaled Dot-Product Attention - Attention with causal masking
- Multi-Head Attention - Parallel attention heads
- Feed-Forward Networks - Position-wise MLPs with GELU
- Transformer Block - Pre-LN, residuals, and all components combined
- Complete Model - Stacking blocks with embedding and output layers
- Training at Scale - Gradient accumulation, validation splits
- KV-Cache - Fast inference through caching
- Interpretability - Logit lens, attention analysis, induction heads

### Fine-Tuning a Transformer

Take a pretrained model and adapt it for specific tasks using modern techniques.

- **Supervised Fine-Tuning (SFT)** - Instruction formatting, loss masking, LoRA
- **Reward Modeling** - Preference data, training reward models, evaluation
- **RLHF** - PPO algorithm, KL penalty, training dynamics, reference models
- **DPO** - Direct Preference Optimization as an alternative to RLHF
- **Advanced Topics** - Memory optimization, hyperparameter tuning, evaluation metrics, common pitfalls

### Reasoning with Transformers

Explore how models can "think" before answering. This section covers techniques from simple prompting to training your own reasoning model.

- Chain-of-Thought - Prompting models to show their work
- Self-Consistency - Sampling multiple chains, majority voting
- Tree of Thoughts - Exploring and pruning reasoning paths
- Process Reward Models - Scoring individual reasoning steps
- Best-of-N Sampling - Using verification to select best solutions
- Monte Carlo Tree Search - Search algorithms for reasoning
- Budget Forcing - Controlling reasoning length with "Wait" tokens
- GRPO - RL without a critic (DeepSeek's approach)
- Distillation - Transferring reasoning to smaller models

### From Noise to Images

Learn how AI generates images from text prompts. This section builds from flow matching fundamentals to a working latent diffusion model.

- Flow Matching - Velocity fields, noise-to-data paths
- Diffusion Transformer - Patchifying images, attention for generation
- Class Conditioning - Classifier-free guidance (CFG)
- Text Conditioning - CLIP embeddings, cross-attention
- Latent Diffusion - VAE compression, scaling to larger images

## Philosophy

These materials follow a simple principle: **the best way to understand something is to build it yourself**.

- No hand-waving. Every operation is explicit.
- No magic. You see exactly what the computer sees.
- No shortcuts. Understanding comes from doing the work.

The architecture that powers GPT, Claude, Stable Diffusion, and other frontier models isn't beyond comprehension. It's just matrix multiplications, attention mechanisms, and optimization - repeated at scale.

## Getting Started

### Prerequisites

- Python 3.12
- A GPU is recommended for the PyTorch sections (CUDA or MPS)
- Basic understanding of calculus (chain rule, partial derivatives)
- Familiarity with Python

### Installation

```bash
# Clone the repository
git clone https://github.com/zhubert/intro-to-transformers.git
cd intro-to-transformers

# Install dependencies with uv (recommended)
uv sync

# Or with pip
pip install -e .
```

### Running the Notebooks

```bash
# Activate the virtual environment
source .venv/bin/activate

# Start Jupyter
jupyter notebook
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017)
- [Andrej Karpathy's educational videos](https://www.youtube.com/@AndrejKarpathy) and [nanoGPT](https://github.com/karpathy/nanoGPT)
- The [PyTorch](https://pytorch.org/) and [Hugging Face](https://huggingface.co/) teams
- Everyone who has worked to make AI more understandable
