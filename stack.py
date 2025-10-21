from typing import TypeVar, Generic, Optional, Iterator, List
from collections.abc import Iterable

T = TypeVar('T')

class Stack(Generic[T]):
    """A generic stack data structure implementation."""
    
    def __init__(self, items: Optional[Iterable[T]] = None):
        """Initialize a stack, optionally from an iterable."""
        self._items: List[T] = list(items) if items else []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> T:
        """
        Pop an item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def pop_safe(self) -> Optional[T]:
        """Pop an item from the stack, returning None if empty."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> T:
        """
        View the top item without removing it.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def peek_safe(self) -> Optional[T]:
        """View the top item, returning None if empty."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()
    
    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
    
    def __bool__(self) -> bool:
        """Return True if stack is non-empty."""
        return bool(self._items)
    
    def __iter__(self) -> Iterator[T]:
        """Iterate from top to bottom (non-destructive)."""
        return reversed(self._items)
    
    def __repr__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack({self._items})"
    
    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        if self.is_empty():
            return "Stack([])"
        items_str = ", ".join(repr(item) for item in reversed(self._items))
        return f"Stack([{items_str}]) ← top"
    
    def __eq__(self, other) -> bool:
        """Check equality with another stack."""
        if not isinstance(other, Stack):
            return NotImplemented
        return self._items == other._items
    
    def __contains__(self, item: T) -> bool:
        """Check if an item is in the stack."""
        return item in self._items
    
    @property
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)


class BoundedStack(Stack[T]):
    """A stack with a maximum capacity."""
    
    def __init__(self, capacity: int, items: Optional[Iterable[T]] = None):
        """Initialize a bounded stack with a maximum capacity."""
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        super().__init__(items)
        if len(self._items) > capacity:
            raise ValueError(f"Too many items for capacity {capacity}")
    
    def push(self, item: T) -> None:
        """
        Push an item onto the stack.
        
        Raises:
            OverflowError: If the stack is at capacity.
        """
        if len(self._items) >= self._capacity:
            raise OverflowError(f"Stack overflow: capacity is {self._capacity}")
        super().push(item)
    
    def is_full(self) -> bool:
        """Check if the stack is at capacity."""
        return len(self._items) >= self._capacity
    
    @property
    def capacity(self) -> int:
        """Return the maximum capacity of the stack."""
        return self._capacity


def demonstrate_basic_operations():
    """Demonstrate basic stack operations."""
    print("=== Basic Stack Operations ===")
    stack = Stack[int]()
    
    # Push items
    for i in [1, 2, 3, 4, 5]:
        stack.push(i)
    print(f"After pushing 1-5: {stack}")
    print(f"Length: {len(stack)}")
    
    # Peek
    print(f"Top element: {stack.peek()}")
    
    # Pop items
    print("\nPopping items:")
    while stack:
        print(f"  Popped: {stack.pop()}")
    
    print(f"Is empty? {stack.is_empty()}")


def demonstrate_string_stack():
    """Demonstrate stack with strings."""
    print("\n=== Stack with Strings ===")
    stack = Stack(["Hello", "Rust", "Python"])
    print(f"Stack: {stack}")
    
    # Check containment
    print(f"'Python' in stack? {'Python' in stack}")
    
    # Iterate (non-destructive)
    print("Iterating from top to bottom:")
    for item in stack:
        print(f"  {item}")
    
    print(f"Stack after iteration: {stack}")


def demonstrate_bounded_stack():
    """Demonstrate bounded stack."""
    print("\n=== Bounded Stack ===")
    bounded = BoundedStack[str](capacity=3)
    
    bounded.push("first")
    bounded.push("second")
    bounded.push("third")
    print(f"Bounded stack: {bounded}")
    print(f"Is full? {bounded.is_full()}")
    
    try:
        bounded.push("overflow!")
    except OverflowError as e:
        print(f"Caught error: {e}")


def is_balanced(expression: str) -> bool:
    """Check if parentheses/brackets/braces are balanced."""
    stack = Stack[str]()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:  # Opening bracket
            stack.push(char)
        elif char in pairs.values():  # Closing bracket
            if stack.is_empty():
                return False
            opening = stack.pop()
            if pairs[opening] != char:
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression: str) -> float:
    """Evaluate a postfix (RPN) expression."""
    stack = Stack[float]()
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    
    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.push(result)
        else:
            stack.push(float(token))
    
    return stack.pop()


def reverse_string(s: str) -> str:
    """Reverse a string using a stack."""
    stack = Stack[str]()
    for char in s:
        stack.push(char)
    
    result = []
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)


def demonstrate_practical_examples():
    """Demonstrate practical stack applications."""
    print("\n=== Practical Example: Balanced Parentheses ===")
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((()))", True),
        ("((())", False),
    ]
    
    for expr, expected in test_cases:
        result = is_balanced(expr)
        status = "✓" if result == expected else "✗"
        print(f"{status} {expr}: {'balanced' if result else 'not balanced'}")
    
    print("\n=== Practical Example: Postfix Evaluation ===")
    postfix_expressions = [
        ("3 4 +", 7.0),
        ("3 4 + 2 *", 14.0),
        ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5.0),
    ]
    
    for expr, expected in postfix_expressions:
        result = evaluate_postfix(expr)
        print(f"{expr} = {result} (expected: {expected})")
    
    print("\n=== Practical Example: String Reversal ===")
    test_string = "Hello, World!"
    reversed_str = reverse_string(test_string)
    print(f"Original: {test_string}")
    print(f"Reversed: {reversed_str}")


if __name__ == "__main__":
    demonstrate_basic_operations()
    demonstrate_string_stack()
    demonstrate_bounded_stack()
    demonstrate_practical_examples()
