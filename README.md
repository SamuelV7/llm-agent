# Transcript Compliance Analyzer

A modern AI-powered content compliance checker using Streamlit and Groq's LLM APIs, built with Python's UV package manager.

## Features

- 🚀 **UV Package Management** - Faster dependency resolution and installation
- 📁 **Dual Input Modes** - Direct text upload or audio transcription
- 🛡️ **Brand Safety Engine** - Custom rule-based compliance checks
- 📈 **Structured Analysis** - Pydantic-validated result reporting
- 🔊 **Audio Processing** - Integrated Whisper transcription pipeline

## License
This project is licensed under the AGPL-3.0 License.
See the LICENSE file for details.

## Technical Approach

### Architecture
1. **Streamlit Frontend** (`app.py`):
   - File upload widget with type detection
   - Result visualization components
   - Error boundary management

2. **Verification Engine** (`req_check.py`):
   - Rule template system with JSON schema
   - LLM-powered analysis via Groq's API
   - Structured output validation with Pydantic

3. **Audio Pipeline** (`transcription.py`):
   - Whisper-large-v3-turbo integration
   - Byte stream handling for MP3 processing
   - Audio metadata preservation

### Key Decisions
- **UV Package Manager**: Chosen for its 10-100x faster dependency resolution
- **Pydantic Models**: Ensure type-safe API responses and data validation
- **Chunked Processing**: Text truncation (5700 chars) handles API token limits
- **Async-Ready**: Structured for future async/await implementation
- **Error Isolation**: Separate processing paths for text/audio inputs
- **Used Dev Containers**: Easy to deploy to Digital Ocean etc

## Future Ideas
- **Graph Engine**: Requests to the large language model should be 
    done after converting requirements to a DAG (Directed Acyclic Graph)
- **Reasoning Model Fine Tune**: Reasoning models do well in these 
    kinds of tasks, given the data on the csv they could be fine 
    tuned for this downstream task like verfication etc.

## Installation

1. **Install UV** (if not present):
   ```bash
   pip install uv
   ```
2. git clone https://github.com/yourusername/transcript-compliance.git
cd transcript-compliance

# Install dependecies
```bash
uv install
```
# Activate environment
```bash
source .venv/bin/activate  # Linux/Mac
```
