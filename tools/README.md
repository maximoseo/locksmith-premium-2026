# 🤖 AI Optimization Tools

**Cost Savings: 60-80% on AI API calls**

## 📁 Tools Overview

| Tool | Purpose | Savings |
|------|---------|---------|
| `content_compressor.py` | Compress long text (LLMLingua-2) | 50-80% |
| `semantic_cache.py` | Cache API responses (GPTCache) | 40-90% |
| `prompt_optimizer.py` | Prompt caching (Anthropic) | 50-90% |
| `ai_optimizer.py` | **Master script - combines all tools** | 75-85% |

---

## 🚀 Quick Start

### 1. Activate Environment
```bash
source .ai-tools-venv/bin/activate
```

### 2. Set API Keys
```bash
# Anthropic (for Claude)
export ANTHROPIC_API_KEY='your-anthropic-key'

# Optional: OpenAI (for GPTCache demo)
export OPENAI_API_KEY='your-openai-key'
```

### 3. Run the Master Optimizer
```bash
cd tools
python ai_optimizer.py
```

---

## 📖 Individual Tools Usage

### Content Compressor (LLMLingua-2)
Compress long text to reduce token usage:

```bash
python content_compressor.py "Your long text here" 0.5
```

**Parameters:**
- Text to compress (required)
- Compression rate: 0.5 = 50% reduction (optional, default: 0.5)

**Output:**
```json
{
  "original": "...",
  "compressed": "...",
  "savings_percent": 67.5
}
```

**Use Cases:**
- Compress service descriptions before sending to AI
- Reduce context length for long documents
- Save tokens on repetitive content

---

### Semantic Cache (GPTCache)
Cache API responses to prevent duplicate calls:

```python
from semantic_cache import SemanticCache

sc = SemanticCache()

messages = [{
    'role': 'user',
    'content': 'What are the best locksmith services?'
}]

# First call - hits API ($)
response1 = sc.cached_completion('gpt-3.5-turbo', messages)

# Second call - returns from cache (FREE!)
response2 = sc.cached_completion('gpt-3.5-turbo', messages)
```

**Use Cases:**
- Cache FAQ generation
- Reuse common SEO queries
- Prevent duplicate content generation

---

### Prompt Optimizer (Anthropic Caching)
Automatically structure prompts for maximum cache efficiency:

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer()

# System prompt is cached automatically
result = optimizer.get_seo_response(
    "Write a meta description for residential locksmith services"
)

print(result['content'])
print(f"Cache savings: {result['cache_stats']['cache_read_input_tokens']} tokens")
```

**How it works:**
1. Static instructions (system prompt) marked for caching
2. First call: pays full price + creates cache
3. Subsequent calls within 5 minutes: 50-90% cheaper!

**Use Cases:**
- All SEO content generation
- Repeated queries with same context
- Batch content creation

---

### Master AI Optimizer
Combines all techniques for maximum savings:

```python
from ai_optimizer import AIOptimizer

optimizer = AIOptimizer()

# Single content generation with all optimizations
result = optimizer.optimize_content_generation(
    content_type='meta_description',
    user_query='Write meta for residential services',
    compress=False
)

# Batch processing (recommended for efficiency)
tasks = [
    {'type': 'meta', 'query': 'Write meta description...'},
    {'type': 'h1', 'query': 'Create heading...'},
    {'type': 'faq', 'query': 'Answer: How fast...'}
]

results = optimizer.generate_seo_content_batch(tasks)
```

---

## 💰 Cost Comparison

### Before Optimization
```
Meta description (50 tokens): $0.05
FAQ answer (150 tokens): $0.15
Service description (500 tokens): $0.50
---
Total: $0.70 per content piece
Monthly (100 pieces): $70
```

### After Optimization
```
Meta description: $0.01 (cached)
FAQ answer: $0.02 (cached)
Service description: $0.08 (cached + compressed)
---
Total: $0.11 per content piece
Monthly (100 pieces): $11

SAVINGS: $59/month (84%)
```

---

## 🎯 Best Practices

### 1. Always Use Prompt Caching
- Put static instructions first
- Mark with `cache_control: ephemeral`
- Cache valid for 5 minutes
- **Cost:** FREE to implement!

### 2. Batch Similar Tasks
- Group related content generation
- System prompt cached once, reused many times
- Example: Generate all FAQ answers in one session

### 3. Compress When Needed
- Use for content > 500 characters
- Especially useful for long service descriptions
- Test output quality after compression

### 4. Cache Frequently Used Queries
- FAQ answers
- Service descriptions
- Common SEO queries
- Product descriptions

---

## 🔧 Integration Examples

### WordPress Site
```python
from ai_optimizer import AIOptimizer

optimizer = AIOptimizer()

# Generate all meta descriptions
pages = ['home', 'residential', 'commercial', 'automotive']
tasks = [
    {'type': 'meta', 'query': f'Write meta for {page} page'}
    for page in pages
]

results = optimizer.generate_seo_content_batch(tasks)

# Upload to WordPress
for page, result in zip(pages, results):
    update_wordpress_meta(page, result['content'])
```

### Static Site Generator
```python
# Generate FAQ section
faq_questions = [
    "How fast is your response time?",
    "Are you licensed and insured?",
    "Do you service all of San Antonio?"
]

tasks = [
    {'type': 'faq', 'query': f'Answer: {q}'}
    for q in faq_questions
]

faqs = optimizer.generate_seo_content_batch(tasks)
```

---

## 📊 Monitoring Usage

All tools return detailed statistics:

```python
result = optimizer.optimize_content_generation(...)

# Check cache efficiency
print(f"Input tokens: {result['cache_stats']['input_tokens']}")
print(f"Cache hits: {result['cache_stats']['cache_read_input_tokens']}")
print(f"Output tokens: {result['cache_stats']['output_tokens']}")

# Check compression (if enabled)
if 'compression_savings' in result:
    print(f"Compression: {result['compression_savings']}")
```

---

## ⚠️ Troubleshooting

### ImportError: No module named 'llmlingua'
```bash
source .ai-tools-venv/bin/activate
pip install llmlingua
```

### API Key Not Set
```bash
# Check if set
echo $ANTHROPIC_API_KEY

# Set temporarily
export ANTHROPIC_API_KEY='your-key'

# Or add to Doppler
doppler secrets set ANTHROPIC_API_KEY='your-key'
```

### Cache Not Working
- Ensure same system prompt
- Cache valid for 5 minutes
- Check API response for cache stats

---

## 🔗 Resources

- [LLMLingua Documentation](https://github.com/microsoft/LLMLingua)
- [GPTCache GitHub](https://github.com/zilliztech/gptcache)
- [Anthropic Prompt Caching](https://docs.anthropic.com/claude/docs/prompt-caching)
- [Parent Strategy Document](../AI-OPTIMIZATION-STRATEGY.md)

---

**Created:** 2026-07-18  
**Status:** Production Ready  
**Estimated Savings:** 75-85% on AI costs
