#!/usr/bin/env python3
"""
AI Optimizer - Master Script
Combines all optimization tools for maximum cost savings
"""

import sys
import json
import os
from pathlib import Path

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

from content_compressor import compress_text
from prompt_optimizer import PromptOptimizer


class AIOptimizer:
    """
    Combines multiple optimization techniques:
    1. Content compression (LLMLingua)
    2. Prompt caching (Anthropic)
    3. Semantic caching (GPTCache)
    """

    def __init__(self):
        """Initialize all optimizers"""
        self.prompt_optimizer = PromptOptimizer()
        print("✅ AI Optimizer initialized")

    def optimize_content_generation(self, content_type, user_query, compress=True):
        """
        Generate optimized content with caching and compression

        Args:
            content_type: Type of content (meta, heading, faq, etc.)
            user_query: Specific request
            compress: Whether to compress the result

        Returns:
            Optimized content with stats
        """
        # Generate with prompt caching
        result = self.prompt_optimizer.get_seo_response(user_query)

        response = {
            'content': result['content'],
            'content_type': content_type,
            'cache_stats': result['cache_stats'],
            'original_length': len(result['content'])
        }

        # Optionally compress the output
        if compress and len(result['content']) > 500:
            compressed = compress_text(result['content'], compression_rate=0.3)
            if 'compressed' in compressed:
                response['compressed_content'] = compressed['compressed']
                response['compressed_length'] = compressed['compressed_length']
                response['compression_savings'] = f"{compressed['savings_percent']}%"

        return response

    def generate_seo_content_batch(self, tasks):
        """
        Generate multiple SEO content pieces efficiently

        Args:
            tasks: List of dicts with 'type' and 'query'

        Returns:
            List of results
        """
        results = []

        print(f"\n📦 Batch processing {len(tasks)} tasks...")
        print("=" * 60)

        for i, task in enumerate(tasks, 1):
            print(f"\n[{i}/{len(tasks)}] {task['type']}: {task['query'][:50]}...")

            result = self.optimize_content_generation(
                task['type'],
                task['query'],
                compress=task.get('compress', False)
            )

            results.append(result)

            # Show cache efficiency
            cache_reads = result['cache_stats']['cache_read_input_tokens']
            if cache_reads > 0:
                print(f"   ✅ Used cache ({cache_reads} tokens)")
            else:
                print(f"   📝 Created cache")

        return results


def demo():
    """Demonstration of the optimizer"""
    print("🚀 AI Optimizer Demo")
    print("=" * 60)

    optimizer = AIOptimizer()

    # Example tasks for locksmith website
    tasks = [
        {
            'type': 'meta_description',
            'query': 'Write a meta description for residential locksmith services in San Antonio',
            'compress': False
        },
        {
            'type': 'h1_heading',
            'query': 'Create an H1 heading for emergency locksmith page',
            'compress': False
        },
        {
            'type': 'faq_answer',
            'query': 'Answer: How fast is your emergency lockout response time?',
            'compress': False
        },
        {
            'type': 'service_description',
            'query': 'Write a detailed description of commercial access control systems (200 words)',
            'compress': True  # Compress longer content
        }
    ]

    # Process batch
    results = optimizer.generate_seo_content_batch(tasks)

    # Summary
    print("\n\n📊 OPTIMIZATION SUMMARY")
    print("=" * 60)

    total_cache_savings = 0
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['content_type'].upper()}")
        print(f"   Content: {result['content'][:80]}...")
        print(f"   Length: {result['original_length']} chars")

        if 'compression_savings' in result:
            print(f"   Compression: {result['compression_savings']} saved")

        cache_reads = result['cache_stats']['cache_read_input_tokens']
        if cache_reads > 0:
            total_cache_savings += cache_reads
            print(f"   Cache: ✅ {cache_reads} tokens reused")

    print(f"\n💰 Total cache tokens saved: {total_cache_savings}")
    print("✅ Demo complete!")


if __name__ == '__main__':
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("⚠️  Warning: ANTHROPIC_API_KEY not set")
        print("Some features require API key. Set it with:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        print("\nRunning limited demo...\n")

    demo()
