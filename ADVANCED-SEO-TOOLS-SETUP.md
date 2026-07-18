# 🛠️ Advanced SEO/GEO Tools - Implementation Plan

## 📋 Available Tools Analysis

Based on the technical guide, here are the tools we can integrate:

### ✅ **Priority 1: Immediate Implementation**

#### 1. **Frase.io** (Content Optimization - ALREADY HAVE API KEY)
- **Status**: ✅ API Key Available: `a64b05b7b8dd48d3a5380a8330a55d39`
- **Transport**: `stdio` (NPM)
- **Installation**:
```bash
claude mcp add frase -e FRASE_API_KEY=a64b05b7b8dd48d3a5380a8330a55d39 -- npx -y @frase/mcp-server
```
- **Use Cases**:
  - Create content briefs for target keywords
  - Optimize existing content for 85+ score
  - Full content lifecycle automation

#### 2. **Semrush** (Competitive Analysis - ALREADY CONNECTED)
- **Status**: ✅ Already integrated via MCP
- **Transport**: `http` (Remote)
- **Endpoint**: `https://mcp.semrush.com/v1/mcp`
- **Use Cases**:
  - Competitor research
  - Keyword gap analysis
  - Backlink opportunities
  - Traffic analysis

#### 3. **LanguageTool** (Grammar & Quality)
- **Status**: 🟡 Can install locally (FREE)
- **Installation**:
```bash
docker run -d -p 8081:8010 erikvl87/languagetool
```
- **Endpoint**: `http://localhost:8081/v2/check`
- **Use Cases**:
  - Grammar checking
  - Spell checking
  - Writing quality improvement

---

### 🎯 **Priority 2: Advanced Tools (Require Sign-up)**

#### 4. **Otterly.ai** (AI Visibility Tracking)
- **Transport**: `http` (Remote)
- **Endpoint**: `https://data.otterly.ai/mcp`
- **Auth**: OAuth 2.0
- **Use Cases**:
  - Track brand mentions in ChatGPT
  - Monitor AI search visibility
  - Share of Voice analysis

#### 5. **Peec AI** (AI Search Optimization)
- **Transport**: `http` (Remote)
- **Endpoint**: `https://api.peec.ai/mcp`
- **Auth**: OAuth 2.0 or Bearer token
- **Use Cases**:
  - AI search optimization
  - GEO (Generative Engine Optimization)
  - AI citation tracking

#### 6. **NeuronWriter** (NLP Term Optimization)
- **Endpoint**: `https://app.neuronwriter.com/neuron-api/0.5/writer`
- **Auth**: `X-API-KEY` header
- **Workflow**:
  1. `/new-query` - Create task for keyword
  2. `/get-query` - Get NLP term recommendations
  3. Write content with recommended terms
  4. `/evaluate-content` - Get SEO score
- **Use Cases**:
  - NLP-driven content optimization
  - Semantic keyword coverage
  - Content scoring

#### 7. **Originality.ai** (AI Detection & Quality)
- **Endpoint**: `https://api.originality.ai/api/v3/scan/ai`
- **Auth**: `X-OAI-API-KEY` header
- **Use Cases**:
  - AI content detection
  - Plagiarism checking
  - Content authenticity verification

---

## 🚀 Implementation Strategy

### Phase 1: Setup LanguageTool (Immediate - FREE)
```bash
# Install local LanguageTool server
docker run -d --name languagetool -p 8081:8010 erikvl87/languagetool

# Test endpoint
curl -X POST http://localhost:8081/v2/check \
  -d "text=This is a test sentance with a mistake." \
  -d "language=en-US"
```

### Phase 2: Optimize with Frase.io (Using existing API key)
```bash
# Create MCP server config
cat > ~/frase-mcp-config.json << 'FRASE_EOF'
{
  "mcpServers": {
    "frase": {
      "command": "npx",
      "args": ["-y", "@frase/mcp-server"],
      "env": {
        "FRASE_API_KEY": "a64b05b7b8dd48d3a5380a8330a55d39"
      }
    }
  }
}
FRASE_EOF
```

### Phase 3: Create Automation Scripts

#### Script 1: Content Quality Checker
```javascript
// ~/tools/content-quality-check.js
const https = require('https');

async function checkGrammar(text) {
  const data = new URLSearchParams({
    text: text,
    language: 'en-US'
  });

  const options = {
    hostname: 'localhost',
    port: 8081,
    path: '/v2/check',
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': data.toString().length
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => resolve(JSON.parse(body)));
    });
    req.on('error', reject);
    req.write(data.toString());
    req.end();
  });
}

// Usage: node content-quality-check.js "Your text here"
if (require.main === module) {
  checkGrammar(process.argv[2]).then(console.log);
}
```

---

## 📊 Automation Workflows

### Workflow 1: Full Content Optimization Pipeline
```bash
# 1. Generate content brief with Frase
# 2. Write content with Claude
# 3. Check grammar with LanguageTool
# 4. Optimize with Frase
# 5. Score 85+ before publishing
```

### Workflow 2: Competitor Analysis & Content Gap
```bash
# 1. Use Semrush to find top 5 competitors
# 2. Extract their top keywords
# 3. Identify content gaps
# 4. Create optimized content for gaps
```

### Workflow 3: AI Visibility Monitoring (Future)
```bash
# 1. Track brand mentions in ChatGPT (Otterly)
# 2. Monitor Share of Voice
# 3. Identify lost visibility
# 4. Create recovery content
```

---

## 💡 Recommended Actions

### Immediate (Today):
1. ✅ Install LanguageTool Docker container
2. ✅ Setup Frase MCP server
3. ✅ Create content quality checker script
4. ✅ Test grammar checking on existing content

### Short-term (This Week):
1. 🔲 Sign up for NeuronWriter trial
2. 🔲 Sign up for Otterly.ai (AI visibility)
3. 🔲 Create automated content pipeline
4. 🔲 Implement quality gates

### Long-term (This Month):
1. 🔲 Full Frase workflow integration
2. 🔲 AI visibility tracking dashboard
3. 🔲 Automated competitor monitoring
4. 🔲 Content performance tracking

---

## 🎯 Expected Benefits

### Content Quality:
- ✅ Grammar-perfect content (LanguageTool)
- ✅ SEO-optimized briefs (Frase)
- ✅ 85+ optimization scores
- ✅ NLP term coverage

### AI Visibility:
- 📈 Track ChatGPT mentions
- 📈 Monitor Perplexity citations
- 📈 Improve Claude recommendations
- 📈 Increase AI Share of Voice

### Competitive Edge:
- 🎯 Gap analysis (Semrush)
- 🎯 Better keyword targeting
- 🎯 Faster content production
- 🎯 Higher quality outputs

---

## 📝 Integration Commands

### Add to Doppler:
```bash
# Save all API keys
doppler secrets set FRASE_API_KEY="a64b05b7b8dd48d3a5380a8330a55d39"
# (Add others as obtained)
```

### Claude MCP Setup:
```bash
# Frase
claude mcp add frase -e FRASE_API_KEY=$(doppler secrets get FRASE_API_KEY --plain) -- npx -y @frase/mcp-server

# Semrush (already configured)
# claude mcp add semrush https://mcp.semrush.com/v1/mcp -t http
```

---

**Ready to implement! Starting with LanguageTool and Frase integration.**
