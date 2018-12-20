## Build document

1. `sphinx-apidoc -F -a -o ./doc ./src`
1. doc/conf.pyを開いてsrc以下を**相対パスに書き換える**  
	- なぜか絶対パスでパスが追加されるのでgit管理下に入れるのであれば修正
	- ex:`sys.path.insert(0, os.path.abspath('../src'))`
1. google style へ対応 `sphinx.ext.napoleon`をextensionに追加  
	- デフォルトではnumpyやgoogleスタイルのdocstringには対応していない
	- 参照: [sphinx.ext.napoleon – NumPy および Google スタイルの docstring をドキュメントに取り込む — Sphinx 1.5.6 ドキュメント](http://www.sphinx-doc.org/ja/stable/ext/napoleon.html)
1. conf.pyを変更 `html_theme = 'sphinx_rtd_theme'`
	- よく見る[このタイプ](https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html)のスタイル。
1. **index.rst の　toctree:: に`modules`を加える**
	- sphinx-apidocでmodule.rstというmoduleのindex的なtreeが作られるのでそれをindexに入れる
1. `sphinx-apidoc --implicit-namespaces -f -o ./doc ./src`
	- *.rstファイルを生成
1. `sphinx-build -a ./doc ./publish`
	- *.rstからhtmlを生成

Reference: [sphinx-apidoc — Sphinx 2.0.0+/54565ec ドキュメント](https://www.sphinx-doc.org/ja/master/man/sphinx-apidoc.html)