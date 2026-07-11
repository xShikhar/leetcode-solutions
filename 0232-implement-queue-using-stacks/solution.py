class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        # Add the element to the input stack
        self.input_stack.append(x)

    def pop(self) -> int:
        # Transfer elements only when output_stack is empty
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        # Remove the front element of the queue
        return self.output_stack.pop()

    def peek(self) -> int:
        # Transfer elements only when output_stack is empty
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        # Return the front element without removing it
        return self.output_stack[-1]

    def empty(self) -> bool:
        # Queue is empty only when both stacks are empty
        return not self.input_stack and not self.output_stack
