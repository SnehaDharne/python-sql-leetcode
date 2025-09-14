from typing import List
from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        queue = deque(range(1, n))  # Initialize the queue with players 1 to n-1
        ele = 0
        w = 0  # ele is the current winner, w is the win count
        
        while True:
            num = queue.popleft()
            if skills[num] < skills[ele]:
                w += 1  # Current winner wins again
                queue.append(num)  # Loser goes to end of queue
            else:
                w = 1  # New winner found
                queue.append(ele)  # Previous winner goes to end of queue
                ele = num  # Update current winner
                
            if w == k or w >= n - 1:
                return ele  # Check for win condition
        return 1