# CVE Migrator

This application migrates CVEs from cve.lineageos.org to your own instance of the CVE tracker.

You probably want to edit the `migrator.py` to your own url. You also need two patches that are not in upstream cve_tracker which is https://github.com/z3ntu/cve_tracker/commit/29d3428d907f51690b99a153e27fb907483f716f and https://github.com/z3ntu/cve_tracker/commit/73f0d4e102909a9bbbd04d139c67cd45ec413ede .

Also you need to copy `config.DEFAULT.py` to `config.py` and enter your CVE tracker API key (see first patch).
