#!/usr/bin/env python3
"""
Semantic Cache - GPTCache Integration
Caches API responses to prevent duplicate expensive LLM calls
"""

from gptcache import cache
from gptcache.adapter import openai
from gptcache.embedding import Onnx
from gptcache.manager import CacheBase, VectorBase, get_data_manager
from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation
import os
import sys
import json


class SemanticCache:
    """Semantic caching for LLM responses"""

    def __init__(self, cache_dir='./cache'):
        """Initialize the semantic cache"""
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self._init_cache()

    def _init_cache(self):
        """Setup GPTCache with semantic similarity"""
        onnx = Onnx()
        cache_base = CacheBase('sqlite')
        vector_base = VectorBase('faiss', dimension=onnx.dimension)
        data_manager = get_data_manager(cache_base, vector_base)

        cache.init(
            embedding_func=onnx.to_embeddings,
            data_manager=data_manager,
            similarity_evaluation=SearchDistanceEvaluation(),
        )

    def cached_completion(self, model, messages, api_key=None):
        """
        Make a cached OpenAI API call

        Args:
            model: Model name (gpt-4, gpt-3.5-turbo, etc.)
            messages: List of message dicts
            api_key: OpenAI API key (or use env var)

        Returns:
            API response (from cache if available)
        """
        if api_key:
            openai.api_key = api_key
        elif not os.getenv('OPENAI_API_KEY'):
            raise ValueError("OpenAI API key required")

        # This call will be cached automatically
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )

        return response


def test_cache():
    """Test the caching system"""
    sc = SemanticCache()

    print("🧪 Testing Semantic Cache...")
    print("-" * 50)

    messages = [{
        'role': 'user',
        'content': 'What are the best locksmith services in San Antonio?'
    }]

    # First call - will hit the API
    print("📞 First call (API)...")
    result1 = sc.cached_completion('gpt-3.5-turbo', messages)
    print(f"✅ Response: {result1.choices[0].message.content[:100]}...")

    # Second call - should return from cache
    print("\n📞 Second call (Cache)...")
    result2 = sc.cached_completion('gpt-3.5-turbo', messages)
    print(f"✅ Response: {result2.choices[0].message.content[:100]}...")

    print("\n✅ Cache test complete!")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_cache()
    else:
        print("Semantic Cache Module")
        print("Usage: python semantic_cache.py test")
        print("\nOr import in your code:")
        print("  from semantic_cache import SemanticCache")
        print("  sc = SemanticCache()")
        print("  response = sc.cached_completion('gpt-4', messages)")
