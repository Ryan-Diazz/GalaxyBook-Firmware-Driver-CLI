
# Optional: import helpers for easy access
from .sysfs import read, write
from .perm import require_root

__all__ = ["read", "write", "requireRoot" ]