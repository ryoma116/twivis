from datetime import timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")
WEEKDAYS = ["月", "火", "水", "木", "金", "土", "日"]

MAX_SEARCH_COUNT = 100
FULL_TEXT_TWEET_MODE = "extended"

# 当日のツイートを除外したい場合はTrueとする（時間帯分析時は24時間分取得できない当日は除外した方がよさそう）
TODAY_EXCLUDED = False