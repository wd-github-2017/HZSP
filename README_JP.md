# 作文評価システム：HZSP（Hanyu Zuowen Shuiping Pingjia）
本プロジェクトは、大規模言語モデル（LLMs）を使った作文評価Webフロントエンドシステムの動作原理をデモンストレーションするためのものです。

## 機能の特徴
- コードが非常にシンプルで、原理の理解に適しています
- ストリーム出力に対応し、評価結果をリアルタイムで表示
- デフォルトでOpenAI SDKを利用（少し修正すれば他のモデルも利用可能、例：[DeepSeek](https://api-docs.deepseek.com/zh-cn/)）。ローカルモデルも利用可能、参考：[Transformers](https://huggingface.co/docs/transformers/index)。
- LLMベースなので、応用環境（デフォルトは中国語教育で、日本語教育・英語教育にも対応可能）評価項目を高度にカスタマイズ可能（`app.py`で修正）
- フロントエンドと出力言語の多言語対応、さまざまなブラウザサイズに対応

## 利用方法

1. プロジェクトをローカルにダウンロード
2. 依存ライブラリをインストール（新しいPython環境 [python＝3.12] の使用推奨）:
   ```bash
   pip install -r requirements.txt
   ```
3. システム環境変数にOPENAI_API_KEYを追加し、APIキーを設定
4. プロジェクトディレクトリでFlaskサーバーを起動:
   ```bash
   python app.py
   ```
5. ブラウザで `http://localhost:5000` にアクセス

## 使い方

1. 左側のテキストボックスに評価したい作文を入力
2. 「実行評価」ボタンをクリック
3. 右側のテキストボックスに評価結果がリアルタイムで表示されるのを待つ

## 注意事項

- 有効なAPIキーが必要です
- 主なブラウザ（Chrome、Edge、Safariなど）の利用を推奨します