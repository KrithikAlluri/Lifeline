# Local Gemma 3n Inference Implementation

This document explains how the chatbot now uses local Gemma 3n inference instead of the OpenRouter API.

## Changes Made

### 1. Model Manager (model_manager.py)
- Created separate module for model management to avoid circular imports
- Added global `tokenizer` and `model` variables
- Created `load_model()` function that loads the model once at startup
- Model is loaded with 4-bit quantization for memory efficiency
- Fallback to CPU if GPU loading fails
- Contains `local_gemma_inference()` function for running inference

### 2. Updated Chatbot Page (chatbot_page.py)
- Replaced all OpenRouter API calls with `local_gemma_inference()` from model_manager
- Removed duplicate inference function to avoid code duplication
- Imports from model_manager instead of main to avoid circular imports

### 3. Dependencies (requirements.txt)
- Added `transformers>=4.35.0`
- Added `torch>=2.0.0`
- Added `accelerate>=0.20.0`
- Added `bitsandbytes>=0.41.0`

## How It Works

### Message to Prompt Conversion
The function converts the message history from this format:
```python
[
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "How are you?"}
]
```

To this prompt format:
```
User: Hello
Assistant: Hi there!
User: How are you?
Assistant: 
```

### Inference Process
1. Tokenize the prompt
2. Generate response with max 256 new tokens
3. Decode the response
4. Extract only the new assistant response

## Usage

### Testing
Run the test script to verify everything works:
```bash
cd lifeline_app_rpi
python test_local_inference.py
```

### Running the Application
```bash
cd lifeline_app_rpi
python main.py
```

## Configuration

### Model Path
The model path is configured in `model_manager.py`:
```python
MODEL_PATH = "/Users/krithikalluri/Documents/GitHub/Lifeline/software/gemma3n_e2b_finetuned"
```

### Model Settings
- **Device**: Auto (GPU if available, CPU fallback)
- **Quantization**: 4-bit for memory efficiency
- **Max tokens**: 256 for responses
- **Temperature**: 0.7 for balanced creativity

## Benefits

1. **No API costs**: Completely free to use
2. **No internet required**: Works offline
3. **Faster responses**: No network latency
4. **Privacy**: All data stays local
5. **Customizable**: Can fine-tune the model further

## Troubleshooting

### Model Loading Issues
- Check if the model path exists
- Ensure you have enough RAM (8GB+ recommended)
- Try CPU fallback if GPU fails

### Inference Issues
- Check if transformers and torch are installed
- Verify the model files are complete
- Check console output for error messages

### Performance Issues
- Reduce `max_new_tokens` for faster responses
- Use CPU if GPU memory is insufficient
- Consider further model quantization

## Future Improvements

1. **Async inference**: Run inference in background thread
2. **Model caching**: Cache responses for common queries
3. **Streaming**: Stream responses as they're generated
4. **Model switching**: Allow switching between different models 