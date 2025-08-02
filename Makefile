.PHONY: docker claude

nvim:
	nvim --listen /tmp/nvim_product_management

claude:
	echo "My Neovim editor is listening on /tmp/nvim_product_management" | claude --add-dir /Users/olivierdupuis/dev/PKM

test:
	python -m pytest $(ARGS)
