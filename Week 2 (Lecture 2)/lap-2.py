from typing import Generic, TypeVar, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()