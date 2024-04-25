from typing import Generic, TypeVar, List, Literal

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.count: int = 1  # Inicializar contador en 1
        self.files: List[int] = []  # Lista de archivos donde se encuentra la palabra

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def has_children(self) -> Literal["left", "right", "both", "none"]:
        if self.left is None and self.right is None:
            return "none"
        elif self.left is not None and self.right is not None:
            return "both"
        elif self.left is not None and self.right is None:
            return "left"
        elif self.left is None and self.right is not None:
            return "right"

    def __str__(self):
        return f"{self.data} (Count: {self.count}, Files: {self.files})"
