1. `sphinx-apidoc -F -o ./doc ./src`
1. google style へ対応 `sphinx.ext.napoleon`をconf.pyのextensionに追加
[sphinx.ext.napoleon – NumPy および Google スタイルの docstring をドキュメントに取り込む — Sphinx 1.5.6 ドキュメント](http://www.sphinx-doc.org/ja/stable/ext/napoleon.html)
1. conf.pyを変更 `html_theme = 'sphinx_rtd_theme'`
1. `sphinx-apidoc -a -f -o ./doc ./src`
1. `sphinx-build -a ./doc ./publish`