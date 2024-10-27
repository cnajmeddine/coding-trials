class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()  # The right-moving asteroid is smaller and explodes
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both asteroids explode
                break
            else:
                stack.append(asteroid)  # Add the asteroid if no collision occurs
        return stack
