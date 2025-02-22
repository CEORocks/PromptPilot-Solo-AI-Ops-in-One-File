# aider --model groq/deepseek-r1-distill-llama-70b --no-detect-urls --no-auto-commit --yes-always --file *.py --message "$1"
# aider --deepseek --no-detect-urls --no-auto-commit --yes-always --file *.py --message "$1"

aider \
    --model o3-mini \
    --architect \
    --reasoning-effort high \
    --editor-model sonnet \
    --no-detect-urls \
    --no-auto-commit \
    --yes-always \
    --file *.py