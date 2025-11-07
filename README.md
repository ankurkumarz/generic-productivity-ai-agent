# Generic Productivity AI Agent

A sophisticated AI agent system built with LangGraph for enhanced productivity and intelligent task automation.

## 🚀 Overview

This project implements a generic productivity AI agent that leverages advanced graph-based workflows, memory management, and skill-based task execution. The agent is designed to handle complex multi-step tasks with intelligent reasoning and adaptive behavior.

## 🏗️ Architecture

The system follows a modular architecture with the following key components:

### Core Components

- **Graph Workflow Engine** - LangGraph-based state management and execution flow
- **Memory System** - Persistent and contextual memory for conversation continuity
- **Skills Framework** - Modular capabilities for task execution
- **API Layer** - RESTful interface for external integrations
- **MCP Tools** - Model Context Protocol tools for enhanced functionality
- **Reflection Module** - Self-assessment and improvement capabilities
- **UI Interface** - User interaction layer

### Directory Structure

    ```
    generic-productivity-ai-agent/
    ├── agent_docs/          # Agent documentation and guides
    ├── api/                 # API endpoints and handlers
    ├── feedback/            # Feedback collection and processing
    ├── graph/               # LangGraph workflow definitions
    ├── mcp/                 # Model Context Protocol tools
    │   └── tools/          # MCP tool implementations
    ├── memory/              # Memory management system
    ├── prompts/             # Prompt templates and management
    ├── reflection/          # Self-reflection and improvement
    ├── skills/              # Agent skill modules
    └── ui/                  # User interface components
        └── src/            # UI source code
    ```

## 🛠️ Key Features

### Intelligent Workflow Management
- **State-based Execution**: Utilizes LangGraph for complex workflow orchestration
- **Dynamic Routing**: Intelligent decision-making for task routing
- **Error Handling**: Robust error recovery and fallback mechanisms

### Memory & Context
- **Persistent Memory**: Long-term information retention across sessions
- **Contextual Awareness**: Maintains conversation context and user preferences
- **Adaptive Learning**: Improves performance based on interaction history

### Extensible Skills System
- **Modular Design**: Easy addition of new capabilities
- **Skill Composition**: Combine multiple skills for complex tasks
- **Dynamic Loading**: Runtime skill discovery and activation

### Advanced Tooling
- **MCP Integration**: Enhanced model capabilities through protocol tools
- **Reflection Capabilities**: Self-assessment and performance optimization
- **Feedback Loop**: Continuous improvement through user feedback

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+ (for UI components)
- Required dependencies (see requirements.txt)

### Installation

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd generic-productivity-ai-agent
    ```

2. **Set up Python environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    pip install -r requirements.txt
    ```

3. **Install UI dependencies**
    ```bash
    cd ui
    npm install
    cd ..
    ```

4. **Configure environment variables**
    ```bash
    cp .env.example .env
    # Edit .env with your configuration
    ```

### Quick Start

1. **Start the agent**
    ```bash
    python -m graph.workflow
    ```

2. **Launch the UI** (optional)
    ```bash
    cd ui
    npm start
    ```

3. **Access the API**
    - API endpoint: `http://localhost:8000`
    - UI interface: `http://localhost:3000`

## 📖 Usage

### Basic Interaction

The agent can be interacted with through multiple interfaces:

#### API Usage
    ```python
    import requests
    
    response = requests.post('http://localhost:8000/chat', {
        'message': 'Help me organize my tasks for today',
        'user_id': 'user123'
    })
    ```

#### Direct Python Integration
    ```python
    from graph.workflow import ProductivityAgent
    
    agent = ProductivityAgent()
    result = agent.process_request("Schedule a meeting for tomorrow")
    ```

### Advanced Features

#### Custom Skills
Create custom skills by extending the base skill class:

    ```python
    from skills.base import BaseSkill
    
    class CustomSkill(BaseSkill):
        def execute(self, context):
            # Your skill implementation
            return result
    ```

#### Memory Configuration
Configure memory settings in your environment:

    ```python
    MEMORY_TYPE = "persistent"  # or "session"
    MEMORY_RETENTION_DAYS = 30
    ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `AGENT_NAME` | Name of the AI agent | "ProductivityAgent" |
| `LOG_LEVEL` | Logging level | "INFO" |
| `API_PORT` | API server port | 8000 |
| `MEMORY_BACKEND` | Memory storage backend | "sqlite" |
| `SKILLS_PATH` | Path to skills directory | "./skills" |

### Customization

#### Adding New Skills
1. Create a new skill file in the [skills/](skills/) directory
2. Implement the required interface
3. Register the skill in the skills registry

#### Extending Workflows
1. Modify [graph/workflow.py](graph/workflow.py) to add new states
2. Define transitions and conditions
3. Test the new workflow paths

## 🧪 Testing

Run the test suite:

    ```bash
    python -m pytest tests/
    ```

Run specific test categories:

    ```bash
    # Test workflows
    python -m pytest tests/test_workflow.py
    
    # Test skills
    python -m pytest tests/test_skills.py
    
    # Test memory
    python -m pytest tests/test_memory.py
    ```

## 📊 Monitoring & Debugging

### Logging
The agent provides comprehensive logging:

    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```

### Performance Metrics
Monitor agent performance through built-in metrics:

- Task completion rates
- Response times
- Memory usage
- Skill utilization

### Debugging Tools
- **Workflow Visualization**: Generate workflow diagrams
- **State Inspection**: Real-time state monitoring
- **Trace Analysis**: Detailed execution traces

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests**
5. **Submit a pull request**

### Development Setup

    ```bash
    # Install development dependencies
    pip install -r requirements-dev.txt
    
    # Set up pre-commit hooks
    pre-commit install
    
    # Run linting
    flake8 .
    black .
    ```

## 📚 Documentation

- **API Documentation**: Available at `/docs` when running the server
- **Architecture Guide**: See [agent_docs/](agent_docs/) directory
- **Skills Reference**: Individual skill documentation in [skills/](skills/)
- **Workflow Guide**: Detailed workflow documentation

## 🔒 Security

- **Input Validation**: All inputs are validated and sanitized
- **Rate Limiting**: API endpoints include rate limiting
- **Authentication**: Configurable authentication mechanisms
- **Data Privacy**: User data handling follows privacy best practices

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Issues**: Report bugs and feature requests on GitHub
- **Discussions**: Join community discussions
- **Documentation**: Comprehensive docs available
- **Examples**: Sample implementations in the examples directory

## 🗺️ Roadmap

### Upcoming Features
- [ ] Enhanced natural language understanding
- [ ] Multi-modal input support
- [ ] Advanced scheduling capabilities
- [ ] Integration with popular productivity tools
- [ ] Mobile application support

### Version History
- **v1.0.0**: Initial release with core functionality
- **v1.1.0**: Added MCP tools integration
- **v1.2.0**: Enhanced memory system
- **v2.0.0**: Complete UI overhaul (planned)

---

**Built with ❤️ by the Productivity AI Team**

For more information, visit our [documentation](agent_docs/) or check out the [API reference](api/).