# ConvertImageLookingGlassPortrait
- 画像+深度画像からLookingGlassPortrait用の画像or動画を生成するスクリプト

# 深度画像の準備
- https://huggingface.co/spaces/nielsr/dpt-depth-estimation
- https://huggingface.co/spaces/akhaliq/DPT-Large

# 実行環境
- Windows 11
- ffmpeg : https://ffmpeg.org/
  - インストール後、環境変数に追加しておく
- Python : 3.8以上

# 実行
## 画像
- `python concat_side.py <画像> <深度画像>`
## 動画
- `python image2video.py <画像> <深度画像>`
