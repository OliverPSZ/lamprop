.PHONY: help install dist clean backup

help:
	@echo "Use 'make install' as root to install py-lamprop."
	@echo "Use 'make dist' to create a software distribution."
	@echo "Use 'make clean' to remove all generated files."
	@echo "Use 'make backup' to create a complete backup."

MANBASE=/usr/local/man/

install: lamprop.1
	@if [ `id -u` != 0 ]; then \
		echo "You must be root to install the program!"; \
		exit 1; \
	fi
	@python setup.py install
	@gzip -k lamprop.1 lamprop.5
	@install -m 644 lamprop.1.gz $(MANBASE)/man1
	@install -m 644 lamprop.5.gz $(MANBASE)/man5
	@rm -f lamprop.1.gz lamprop.5.gz

dist::
	@python setup.py sdist

clean::
	@rm -rf dist build py-lamprop-*.tar.gz *.pyc

backup::
	@sh tools/genbackup

# This also recreates lamprop.5, PDF documentation and lpver.py.
lamprop.1: lamprop.1.in
	tools/post-commit
