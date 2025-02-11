from datetime import datetime, timedelta

def is_within_this_week(date_str) -> bool:
    date = datetime.fromisoformat(date_str)
    now = datetime.now()
    start_of_week = now - timedelta(days=now.isoweekday() - 1)  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday
    return start_of_week <= date <= end_of_week

def is_within_this_month(date_str) -> bool:
    date = datetime.fromisoformat(date_str)
    now = datetime.now()
    return date.year == now.year and date.month == now.month

def is_within_today(date_str) -> bool:
    date = datetime.fromisoformat(date_str)
    now = datetime.now()
    return date.now() == now.date()