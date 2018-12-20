## Build document

1. `sphinx-apidoc -F -a -o ./doc ./src`
1. doc/conf.pyを開いてsrc以下を**相対パスに書き換える**  
`sys.path.insert(0, os.path.abspath('../src'))`
1. google style へ対応 `sphinx.ext.napoleon`をextensionに追加  
[sphinx.ext.napoleon – NumPy および Google スタイルの docstring をドキュメントに取り込む — Sphinx 1.5.6 ドキュメント](http://www.sphinx-doc.org/ja/stable/ext/napoleon.html)
1. conf.pyを変更 `html_theme = 'sphinx_rtd_theme'`
1. **index.rst の　toctree:: を`modules`にする**
1. `sphinx-apidoc --implicit-namespaces -f -o ./doc ./src`
1. `sphinx-build -a ./doc ./publish`

Reference: [sphinx-apidoc — Sphinx 2.0.0+/54565ec ドキュメント](https://www.sphinx-doc.org/ja/master/man/sphinx-apidoc.html)