#!/bin/bash
###############################################################################
# AI Optimization Tools - Automated Setup Script
# Installs and configures all cost-saving AI tools
###############################################################################

set -e  # Exit on error

echo "🚀 AI Optimization Tools Setup"
echo "================================"
echo ""

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if in project root
if [ ! -f "index.html" ]; then
    echo -e "${RED}❌ Error: Run this script from project root${NC}"
    echo "Usage: cd /tmp/locksmith-premium-2026 && bash tools/setup.sh"
    exit 1
fi

# Step 1: Create virtual environment
echo -e "${YELLOW}📦 Step 1: Creating Python virtual environment...${NC}"
if [ ! -d ".ai-tools-venv" ]; then
    python3 -m venv .ai-tools-venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi

# Step 2: Activate and install packages
echo -e "${YELLOW}📦 Step 2: Installing AI optimization packages...${NC}"
source .ai-tools-venv/bin/activate

pip install --quiet --upgrade pip
pip install --quiet -r tools/requirements.txt

echo -e "${GREEN}✅ All packages installed${NC}"

# Step 3: Verify installations
echo -e "${YELLOW}🔍 Step 3: Verifying installations...${NC}"
python3 -c "import llmlingua; print('✅ LLMLingua-2 installed')"
python3 -c "import gptcache; print('✅ GPTCache installed')"
python3 -c "import anthropic; print('✅ Anthropic SDK installed')"
python3 -c "import openai; print('✅ OpenAI SDK installed')"

# Step 4: Make scripts executable
echo -e "${YELLOW}🔧 Step 4: Setting permissions...${NC}"
chmod +x tools/*.py
echo -e "${GREEN}✅ Scripts are now executable${NC}"

# Step 5: Test basic functionality
echo -e "${YELLOW}🧪 Step 5: Testing content compressor...${NC}"
TEST_TEXT="This is a test of the content compression system. It should reduce the text length significantly while maintaining meaning."
python3 tools/content_compressor.py "$TEST_TEXT" 0.5 > /dev/null 2>&1
echo -e "${GREEN}✅ Compressor test passed${NC}"

# Step 6: Check for API keys
echo ""
echo -e "${YELLOW}🔑 Step 6: Checking API keys...${NC}"

if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo -e "${GREEN}✅ ANTHROPIC_API_KEY is set${NC}"
else
    echo -e "${YELLOW}⚠️  ANTHROPIC_API_KEY not set${NC}"
    echo "   Set it with: export ANTHROPIC_API_KEY='your-key'"
fi

if [ -n "$OPENAI_API_KEY" ]; then
    echo -e "${GREEN}✅ OPENAI_API_KEY is set${NC}"
else
    echo -e "${YELLOW}⚠️  OPENAI_API_KEY not set (optional)${NC}"
fi

# Final summary
echo ""
echo "================================"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "================================"
echo ""
echo "📚 Next Steps:"
echo "  1. Activate environment: source .ai-tools-venv/bin/activate"
echo "  2. Set API keys (if not already set):"
echo "     export ANTHROPIC_API_KEY='your-key'"
echo "  3. Run demo: python tools/ai_optimizer.py"
echo "  4. Read docs: cat tools/README.md"
echo ""
echo "💰 Expected Savings: 75-85% on AI costs"
echo ""
