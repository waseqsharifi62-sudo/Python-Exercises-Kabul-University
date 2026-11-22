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

    def peek(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

int_stack = Stack[int]()
int_stack.push(10)
str_stack = Stack[str]()
str_stack.push("Hello")

empty_stack = Stack[int]()
try:
    empty_stack.pop()
except IndexError:
    pass