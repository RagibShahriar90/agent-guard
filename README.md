# 🛡️ AgentGuard

**AgentGuard** is a lightweight, extensible framework designed to monitor, debug, and improve the reliability of LLM-based agents. As agents become more complex (using tools, multi-step reasoning, and memory), they become prone to specific failure modes like tool-misuse, infinite loops, and hallucinated logic.

AgentGuard provides a structured way to intercept agent "traces" and apply heuristic or model-based validators to ensure high-fidelity execution.

## ✨ Features
- **Trace Interception:** Capture and log every step of an agent's reasoning process.
- **Pluggable Validators:** Easily add checks for:
  - Tool execution safety.
  - Logic consistency.
  - Hallucination detection.
  - Token/Cost limits.
- **Automated Labeling:** Automatically categorize agent bugs based on trace patterns (inspired by recent research).
- **AIOps Integration:** Export metrics to Prometheus/Grafana for real-time agent health monitoring.

## 🚀 Quick Start

### Installation
`ash
pip install agent-guard
`

### Basic Usage
`python
from agent_guard import AgentGuard, ToolValidator

# Initialize Guard
guard = AgentGuard()

# Add a validator
guard.add_validator(ToolValidator(allowed_tools=["search", "calculator"]))

# Wrap your agent loop
with guard.trace("task_id_123") as trace:
    # Your agent logic here
    response = my_llm_agent.run("Calculate the distance to Mars")
    trace.log_step(action="calculator", input="...", output="...")

# Check for reliability issues
report = guard.get_report()
print(report.summary())
`

## 📊 Roadmap
- [ ] Integration with LangChain and AutoGen.
- [ ] Real-time hallucination check using cross-model validation.
- [ ] GUI for trace visualization.

## 🤝 Contributing
Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📜 License
MIT License.