#!/usr/bin/env python3
"""
Content Compressor - LLMLingua-2 Integration
Compresses long text content to reduce token usage by 50-80%
"""

from llmlingua import PromptCompressor
import sys
import json

def compress_text(text, compression_rate=0.5):
    """
    Compress text using LLMLingua-2

    Args:
        text: Original text to compress
        compression_rate: How much to compress (0.5 = 50% reduction)

    Returns:
        dict: Original text, compressed text, and compression stats
    """
    try:
        compressor = PromptCompressor()

        # Compress the text
        result = compressor.compress_prompt(
            text,
            rate=compression_rate,
            force_tokens=[],  # Tokens to always keep
            drop_consecutive=True  # Remove consecutive similar tokens
        )

        original_length = len(text)
        compressed_length = len(result['compressed_prompt'])
        savings_percent = ((original_length - compressed_length) / original_length) * 100

        return {
            'original': text,
            'compressed': result['compressed_prompt'],
            'original_length': original_length,
            'compressed_length': compressed_length,
            'savings_percent': round(savings_percent, 2),
            'compression_rate': compression_rate
        }

    except Exception as e:
        return {
            'error': str(e),
            'original': text
        }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python content_compressor.py 'your text here' [compression_rate]")
        print("Example: python content_compressor.py 'Long text...' 0.5")
        sys.exit(1)

    text = sys.argv[1]
    rate = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    result = compress_text(text, rate)
    print(json.dumps(result, indent=2, ensure_ascii=False))
