# 芯路 · Waferpath

美国半导体求职与出口许可的中英文资料站。访客可以在首页或联系页扫码添加 Cecilia Y. 的微信，咨询美国 Export License 申请。站点由 HTML、CSS 和图片组成，不接收或保存访客留言。

## 本机预览

使用 Python 3.8 或更高版本。在仓库根目录执行：

```sh
SITE_URL=http://localhost:8000 python3 src/build.py
python3 -m http.server 8000 --directory dist/client
```

浏览器打开 http://localhost:8000/ 。源文件在 `src/`，输出在 `dist/client/`。

## GitHub Pages

如用于符合 [GitHub Pages 使用规则](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) 的资料站，将源文件推送到仓库的 `main` 分支，在 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。在 **Actions → Publish static website → Run workflow** 首次发布。以后推送到 `main` 会自动部署。工作流会使用仓库实际的 Pages 网址生成页面链接和站点地图。

其他静态托管服务可使用相同的构建命令，将 `SITE_URL` 设为最终公开网址（包含项目子路径），发布 `dist/client/`。
