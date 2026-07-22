class StockSpanner:
    def __init__(self):
        # stack holds (price, span) pairs, price decreasing from bottom to top
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # today itself always counts as 1

        # Pop every entry that is <= today's price — it's now "absorbed"
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append((price, span))
        return span
