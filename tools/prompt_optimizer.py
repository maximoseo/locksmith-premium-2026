#!/usr/bin/env python3
"""
Prompt Optimizer - Implements Anthropic Prompt Caching
Automatically structures prompts to maximize cache hits
"""

from anthropic import Anthropic
import os
import sys
import json


class PromptOptimizer:
    """Optimizes prompts for Anthropic's Prompt Caching"""

    def __init__(self, api_key=None):
        """Initialize with Anthropic API"""
        self.client = Anthropic(
            api_key=api_key or os.getenv('ANTHROPIC_API_KEY')
        )

    def create_cached_message(self, system_prompt, user_message, model='claude-3-5-sonnet-20241022'):
        """
        Create a message with prompt caching enabled

        Args:
            system_prompt: Static instructions to cache
            user_message: Dynamic user query
            model: Claude model to use

        Returns:
            API response with caching metadata
        """
        # Structure for caching: static content first with cache_control
        response = self.client.messages.create(
            model=model,
            max_tokens=1024,
            system=[
                {
                    "type": "text",
                    "text": system_prompt,
                    "cache_control": {"type": "ephemeral"}  # Mark for caching
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response

    def get_seo_response(self, user_query):
        """
        SEO-optimized response with cached system prompt

        Args:
            user_query: User's SEO question

        Returns:
            Response with cache statistics
        """
        # This system prompt will be cached across calls
        system_prompt = """You are an expert SEO copywriter for a locksmith business in San Antonio, Texas.

GUIDELINES:
1. Always include local keywords: San Antonio, Bexar County, Texas
2. Focus on service areas and neighborhoods
3. Use professional, trustworthy tone
4. Include specific locksmith services
5. Emphasize 24/7 availability and fast response
6. Highlight licensing, insurance, and experience
7. Use action-oriented language
8. Optimize for Google local search
9. Include relevant CTAs
10. Follow E-E-A-T principles (Experience, Expertise, Authority, Trust)

SERVICES TO HIGHLIGHT:
- Residential: lockouts, rekeying, smart locks, deadbolts, safes
- Commercial: access control, master keys, panic bars, high-security locks
- Automotive: car lockouts, key programming, transponder keys, ignition repair

NEIGHBORHOODS TO MENTION:
Alamo Heights, Stone Oak, The Dominion, Northwest Hills, Medical Center,
Downtown, Southtown, King William, Olmos Park, Terrell Hills

KEYWORDS TO USE:
locksmith San Antonio, emergency locksmith, 24/7 locksmith, mobile locksmith,
residential locksmith, commercial locksmith, automotive locksmith, lock repair,
key replacement, rekey service, smart lock installation

Write clear, concise, and engaging content that ranks well in local search."""

        response = self.create_cached_message(system_prompt, user_query)

        # Extract usage stats
        usage = response.usage
        cache_info = {
            'input_tokens': usage.input_tokens,
            'cache_creation_input_tokens': getattr(usage, 'cache_creation_input_tokens', 0),
            'cache_read_input_tokens': getattr(usage, 'cache_read_input_tokens', 0),
            'output_tokens': usage.output_tokens
        }

        return {
            'content': response.content[0].text,
            'cache_stats': cache_info,
            'model': response.model
        }


def main():
    """Demo the prompt optimizer"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("❌ Error: ANTHROPIC_API_KEY environment variable required")
        print("Set it in Doppler or export it:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)

    optimizer = PromptOptimizer()

    print("🚀 Prompt Caching Demo")
    print("=" * 60)

    queries = [
        "Write a meta description for residential locksmith services",
        "Create an H1 heading for commercial locksmith page",
        "Generate FAQ answer about emergency lockout response time"
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n📝 Query {i}: {query}")
        print("-" * 60)

        result = optimizer.get_seo_response(query)

        print(f"✅ Response: {result['content'][:200]}...\n")
        print(f"📊 Cache Stats:")
        print(f"   Input tokens: {result['cache_stats']['input_tokens']}")
        print(f"   Cache creation: {result['cache_stats']['cache_creation_input_tokens']}")
        print(f"   Cache reads: {result['cache_stats']['cache_read_input_tokens']}")
        print(f"   Output tokens: {result['cache_stats']['output_tokens']}")

        if result['cache_stats']['cache_read_input_tokens'] > 0:
            savings = (result['cache_stats']['cache_read_input_tokens'] /
                      (result['cache_stats']['input_tokens'] or 1)) * 100
            print(f"   💰 Cache savings: ~{savings:.1f}%")


if __name__ == '__main__':
    main()
