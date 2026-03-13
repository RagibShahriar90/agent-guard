import time
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from rich.console import Console

console = Console()

class TraceStep(BaseModel):
    timestamp: float = Field(default_factory=time.time)
    action: str
    input_data: Any
    output_data: Optional[Any] = None
    status: str = "pending"

class AgentGuard:
    def __init__(self):
        self.traces: Dict[str, List[TraceStep]] = {}
        console.print("[bold green]🛡️ AgentGuard Initialized[/bold green]")

    def start_trace(self, session_id: str):
        self.traces[session_id] = []
        console.print(f"[blue]Starting trace for session: {session_id}[/blue]")

    def log_step(self, session_id: str, action: str, input_data: Any, output_data: Any = None):
        step = TraceStep(action=action, input_data=input_data, output_data=output_data, status="completed")
        self.traces[session_id].append(step)
        console.print(f"  [yellow]LOG:[/yellow] Action '{action}' recorded.")

    def analyze(self, session_id: str):
        steps = self.traces.get(session_id, [])
        console.print(f"\n[bold underline]Analysis Report for {session_id}[/bold underline]")
        if not steps:
            print("No steps found.")
            return

        # Simple heuristic: Check for repetitive actions (potential loops)
        actions = [s.action for s in steps]
        if len(actions) != len(set(actions)):
            console.print("[bold red]⚠️ Potential Loop Detected:[/bold red] Repeated actions found in trace.")
        else:
            console.print("[green]✅ No obvious loops detected.[/green]")
        
        console.print(f"Total steps: {len(steps)}")

if __name__ == "__main__":
    # Example usage
    guard = AgentGuard()
    session = "research-task-001"
    
    guard.start_trace(session)
    guard.log_step(session, "web_search", {"query": "AIOps trends 2025"}, "Success")
    guard.log_step(session, "summarize", "Text content...", "Summary generated")
    guard.log_step(session, "web_search", {"query": "AIOps trends 2025"}, "Success") # Duplicate action
    
    guard.analyze(session)