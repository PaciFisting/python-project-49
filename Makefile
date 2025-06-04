install: 
	uv sync
brain-games: 
	uv run brain-games
brain-even:
	uv run brain-even
brain-gcd:
	uv run brain-gcd
brain-calc:
	uv run brain-calc
brain-progression:
	uv run brain-progression
brain-prime:
	uv run brain-prime
build:
	uv build
package-install:
	uv tool install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall
lint:
	uv run ruff check brain_games