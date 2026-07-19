class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # holds indices, heights at these indices are increasing
        max_area = 0
        extended = heights + [0]  # sentinel to flush remaining bars

        for i in range(len(extended)):
            current_height = extended[i]

            while stack and extended[stack[-1]] > current_height:
                top_index = stack.pop()
                height = extended[top_index]

                if stack:
                    left_boundary = stack[-1]
                else:
                    left_boundary = -1

                width = i - left_boundary - 1
                area = height * width

                if area > max_area:
                    max_area = area

            stack.append(i)

        return max_area
