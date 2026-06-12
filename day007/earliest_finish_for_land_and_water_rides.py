class Solution(object):
    def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
        if not landStartTime or not waterStartTime:
            return -1

        min_land_end = min(s + d for s, d in zip(landStartTime, landDuration))
        min_water_end = min(s + d for s, d in zip(waterStartTime, waterDuration))

        best = float("inf")

        # land first then water
        for ws, wd in zip(waterStartTime, waterDuration):
            best = min(best, max(min_land_end, ws) + wd)

        # water first then land
        best_land_dur_when_open = float("inf")
        best_land_start_plus_dur_after_open = float("inf")
        for ls, ld in zip(landStartTime, landDuration):
            if ls <= min_water_end:
                best_land_dur_when_open = min(best_land_dur_when_open, ld)
            else:
                best_land_start_plus_dur_after_open = min(best_land_start_plus_dur_after_open, ls + ld)

        if best_land_dur_when_open != float("inf"):
            best = min(best, min_water_end + best_land_dur_when_open)
        if best_land_start_plus_dur_after_open != float("inf"):
            best = min(best, best_land_start_plus_dur_after_open)

        return best if best != float("inf") else -1

print(Solution.earliestFinishTime([2,8],[4,1],[6],[3]))
print(Solution.earliestFinishTime([5],[3],[1],[10]))       