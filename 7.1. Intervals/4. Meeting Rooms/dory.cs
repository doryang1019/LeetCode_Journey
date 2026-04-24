# Runtime 132ms
# Beats 61.36%

# Memory 29.0 MB
# Beats 84.09%

/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    public bool CanAttendMeetings(List<Driver.Interval> intervals) {
        intervals.Sort((a, b) => a.start.CompareTo(b.start));
        for(int i = 0; i < intervals.Count - 1; i++) {
            if(intervals[i].end > intervals[i+1].start) {
                return false;
            }
        }
        return true;
    }
}
