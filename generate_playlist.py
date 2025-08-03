import os
import json

# 获取当前脚本所在目录
base_path = os.path.dirname(os.path.abspath(__file__))

# MUSIC 文件夹路径（脚本同级）
music_dir = os.path.join(base_path, "MUSIC")

# 支持的音乐格式
music_exts = (".mp3", ".ogg", ".wav", ".flac")

# 检查目录是否存在
if not os.path.exists(music_dir):
    print(f"❌ 找不到音乐文件夹：{music_dir}")
    exit()

songs = []
for file in os.listdir(music_dir):
    if file.lower().endswith(music_exts):
        song_name = os.path.splitext(file)[0]
        # 相对路径（用于网页访问）
        songs.append({"title": song_name, "src": f"MUSIC/{file}"})

# 保存 playlist.json
playlist_path = os.path.join(base_path, "playlist.json")
with open(playlist_path, "w", encoding="utf-8") as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)

print(f"✅ 已生成 playlist.json，共找到 {len(songs)} 首歌。")
