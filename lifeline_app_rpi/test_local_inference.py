#!/usr/bin/env python3
"""
Test script for local Gemma inference
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model_manager import load_model, local_gemma_inference

def test_inference():
    """Test the local inference with a simple prompt"""
    print("Loading model...")
    load_model()
    
    # Test with a simple prompt
    test_messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    
    print("\nTesting inference...")
    try:
        response = local_gemma_inference(test_messages)
        print(f"✅ Inference successful!")
        print(f"Response: {response}")
        return True
    except Exception as e:
        print(f"❌ Inference failed: {e}")
        return False

if __name__ == "__main__":
    success = test_inference()
    if success:
        print("\n🎉 Local inference is working! You can now run the main application.")
    else:
        print("\n💥 Local inference failed. Please check the model path and dependencies.") 