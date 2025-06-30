# Time Complexity : O(n log k)
# Space Complexity : Auxiliary O(k) : for the heap
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Three line explanation of solution in plain english:
#1. We use a min heap to keep track of the end times of meetings.
#2. We sort the intervals by their start times and iterate through them, using the heap to manage room availability.
#3. If the start time of the current meeting is greater than or equal to the earliest
#   end time in the heap, we can reuse that room; otherwise, we need a new room.


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        h=[]
        heapq.heapify(h)
        if not intervals:
            return 0
        #sorting the intervals based on start time
        intervals.sort(key=lambda i: i.start)
        first_int=intervals[0]
        #push first interval on to the min heap
        heapq.heappush(h,first_int.end)
        #iterate throught the list of intervals
        for inter in range(1,len(intervals)):
            #check if the start time of next interval is greater than the end time of the root of min heap i.e the interval with smaller start time
            if intervals[inter].start>=h[0]:
                #replacing the root of min heap since start time is greater so we can reuse the room
                heapq.heapreplace(h,intervals[inter].end)
            else:
                #keep pushing the intervals with lesser start time on to the heap
                heapq.heappush(h,intervals[inter].end)
        #now the heap has the minimum number of rooms required
        return len(h)