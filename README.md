# 机场湾 (JichangBay) - 2026 推荐机场与 VPN 使用指南

这是一个基于 Hexo 构建的高性能、SEO 优化的单页面 (Pillar Page) 博客，专门针对中文用户的机场和 VPN 推荐。

## 项目特点

1. **完全自定义单页主题** (`themes/jichangbay`)：
   - 深海蓝 (`#0f172a`) / 海湾青 (`#0891b2`) 设计，现代且专业。
   - 桌面端悬浮目录 (Sticky TOC) 与移动端折叠目录 (Drawer TOC)，自动高亮当前阅读章节。
   - 轻量级，无大型框架 (No jQuery/React/Bootstrap)，纯原生 JS 实现所有交互。
2. **SEO 友好**：
   - 包含 Schema JSON-LD、Canonical 规范标签、Open Graph 标签。
   - `sitemap.xml` 自动生成。
   - 配置了 IndexNow 脚本 (`scripts/indexnow.js`)，可以自动向搜索引擎推送更新。
3. **数据分离**：
   - 所有的推荐品牌数据都在 `source/_data/providers.yml` 中管理。
   - 通过修改此 YML 文件，自动渲染到主页的参数对比表、快速推荐卡片和具体的品牌介绍区块。

## 目录结构说明

- `_config.yml`: 站点全局配置文件（URL、主题等）。
- `source/_data/providers.yml`: **核心数据文件**，编辑这里即可修改页面上的所有机场/VPN数据。
- `source/CNAME`: 绑定的自定义域名 (`jichangbay.com`)。
- `themes/jichangbay/layout/index.ejs`: 页面主体模板，包含了首页结构、循环输出数据等逻辑。
- `themes/jichangbay/source/css/style.css`: 主题 CSS 样式文件。
- `themes/jichangbay/source/js/main.js`: 交互逻辑 (TOC、进度条等)。
- `.github/workflows/deploy.yml`: GitHub Actions 自动化部署脚本。

## 部署与发布指南 (非常重要)

### 1. 怎样修改数据
所有推荐的机场/VPN 数据均通过 Hexo Data Files 实现。
请打开 `source/_data/providers.yml`，参考里面的 Demo 数据结构添加或修改您自己的推荐。
字段包括 `name`（名称）、`price`（价格）、`traffic`（流量）、`advantages`（优点列表）、`affiliateUrl`（你的推广链接）等。

### 2. 怎样建立 GitHub Repository 并推送代码
本地代码已经完全准备好，请按照以下步骤推送到 GitHub：

1. 登录 GitHub，点击右上角 `+`，选择 **New repository**。
2. 填写 Repository name（例如 `jichangbay.com`），设为 Public，**不要** 勾选 "Add a README file"。点击 Create。
3. 在本地项目的根目录（即 `c:\Users\USER\Desktop\BLOG\jichangbay.com`）下，打开命令行或终端，执行以下命令：
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/Colasaiko/您的仓库名.git
   git push -u origin main
   ```

### 3. GitHub Actions 自动部署 (GitHub Pages)
因为本项目已经包含了 `.github/workflows/deploy.yml`，当你将代码推送到 GitHub 的 `main` 分支后，GitHub Actions 会自动触发构建和发布。
- 打开你在 GitHub 的 Repository 页面，点击顶部的 **Settings**。
- 左侧找到 **Pages** (GitHub Pages)。
- 将 **Source** (Build and deployment) 设置为 **`GitHub Actions`**。

### 4. 绑定自定义域名 (jichangbay.com)
由于使用了 `actions/deploy-pages`，项目中的 `source/CNAME` 仅作为记录保存。**你必须在 GitHub 中手动设置自定义域名**：
- 前往 Repository 的 **Settings** -> **Pages**。
- 在 **Custom domain** 一栏输入 `jichangbay.com`，然后点击 Save 并在验证通过后勾选 "Enforce HTTPS"。

同时，你需要前往你的域名注册商（如 Cloudflare / 阿里云 / Namecheap 等）配置 DNS 记录：
- **Apex 域名 (jichangbay.com)**:
  - 推荐使用 **ALIAS 或 ANAME 记录** 指向 `colasaiko.github.io`（如果支持）。
  - 或者设置 **A 记录** 指向 GitHub Pages 的 IP：
    - `185.199.108.153`
    - `185.199.109.153`
    - `185.199.110.153`
    - `185.199.111.153`
- **子域名 (www.jichangbay.com)**:
  - 设置 **CNAME 记录** 指向 `colasaiko.github.io`。

### 5. IndexNow 搜索引擎推送
配置了 `scripts/indexnow.js`。您可以通过设置环境变量 `INDEXNOW_KEY`（在 GitHub Repository 的 Settings -> Secrets and variables -> Actions 中设置）来提供您的密钥。
部署时会自动生成 `<您的密钥>.txt` 以供验证。目前配置仅生成验证文件并不发送真实HTTP请求（以防未上线被惩罚）。

