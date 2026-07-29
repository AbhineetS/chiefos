from pydantic import BaseModel, Field
from typing import Dict, Any

class SharedMemory(BaseModel):
    """Shared memory object to maintain state across agents."""
    context: Dict[str, Any] = Field(default_factory=dict)
    
    def set(self, key: str, value: Any):
        self.context[key] = value
        
    def get(self, key: str, default: Any = None) -> Any:
        return self.context.get(key, default)
    
    def get_all(self) -> Dict[str, Any]:
        return self.context

# A global instance for the MVP shared context
global_memory = SharedMemory()
