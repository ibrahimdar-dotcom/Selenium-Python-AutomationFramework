pytest -v -s -m "smoke" --html=Reports\report.html  --browser Firefox
pytest -v -s -n=4 -m "smoke or regression" --html=Reports\report.html  --browser Chrome
rem pytest -v -s -n=2 -m "smoke or regression" --html=Reports\report.html  --browser Firefox