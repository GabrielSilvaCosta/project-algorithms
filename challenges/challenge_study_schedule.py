def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for period1, period2 in permanence_period:
        if not isinstance(period1, int) or not isinstance(period2, int):
            return
        if period1 <= target_time <= period2:
            count += 1
    return count
