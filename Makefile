setup_day:
	uv run setup_day.py --day $(DAY)

test:
ifdef PART
	uv run pytest -vv day$(shell printf "%02d" $(DAY))/part$(PART)/test.py
else
	uv run pytest -vv day$(shell printf "%02d" $(DAY))
endif