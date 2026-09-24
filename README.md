<div align="center">
  <img src="https://jichangbay.com/images/logos/梯子云.webp" width="80" alt="JichangBay Logo" style="border-radius: 20px;">
  <h1>✈️ 机场湾 (JichangBay)</h1>
  <p><strong>2026 稳定专线与优质 VPN 套餐选购指南</strong></p>
  
  <p>
    <a href="https://jichangbay.com">🌐 访问线上网站 (jichangbay.com)</a>
  </p>

  <p>
    <a href="https://hexo.io/"><img src="https://img.shields.io/badge/Framework-Hexo_7.3-0f172a?style=flat-square&logo=hexo" alt="Hexo"></a>
    <a href="https://github.com/Colasaiko/jichangbay.com/actions"><img src="https://img.shields.io/github/actions/workflow/status/Colasaiko/jichangbay.com/deploy.yml?style=flat-square&logo=github" alt="Build Status"></a>
    <a href="https://github.com/Colasaiko/jichangbay.com/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-0891b2?style=flat-square" alt="License"></a>
  </p>
</div>

---

## 📖 项目简介

**机场湾 (JichangBay)** 是一个基于 Hexo 构建的高性能、SEO 友好的单页面（Pillar Page）静态博客应用。专注于提供高质量的中文机场、专线与 VPN 推荐，帮助用户快速对比套餐价格、流量与节点线路，并实现自动跳转。

项目采用了高度解耦的**数据驱动架构 (Data-Driven)**，所有内容（例如全站 31+ 机场品牌数据）通过 `source/_data/providers.yml` 进行集中管理，免去手动编写冗长 EJS 页面模板的繁琐。

## ✨ 核心亮点

- ⚡️ **极致性能 & 纯原生前端**
  不依赖任何沉重的前端框架（No React/Vue/jQuery/Bootstrap），使用纯原生 JavaScript 和纯 CSS 编写。确保极速的页面加载体验，适合大内容量的单页面呈现。
- 📊 **智能数据驱动**
  品牌信息、价格、流量等数据统一通过 YAML 管理。模板会自动计算并提取每个品牌的 **最低真实月付价格**，并动态渲染首页的参数对比表、快速选购区及专属品牌详情块。
- 🛡️ **自动化推广链接保护 (Link Cloaking)**
  内建一套数据驱动的 Link Cloaking 机制，将外部 Affiliate 链接安全隐藏为 `/go/{slug}/` 的内部重定向格式。Node 脚本在构建时自动生成所有相关的 301/JS 跳转页，防止权重流失与恶意爬虫嗅探。
- 🔍 **顶级 SEO 优化**
  自动生成精简的 `sitemap.xml` 和 `robots.txt`；内嵌 Schema JSON-LD 结构化数据，规范化 `<link rel="canonical">`。支持基于 IndexNow 的搜索引擎自动推送（免 HTTP 惩罚预备机制）。
- 📱 **优雅的响应式设计**
  精美的深海蓝（`#0f172a`）UI 风格。桌面端自带平滑滚动（Smooth Scroll）的高亮悬浮侧边目录 (Sticky TOC)，移动端配备原生开发的侧边抽屉目录。

## 🛠️ 目录结构说明

- `_config.yml`: 站点全局配置文件（URL、元数据、部署配置）。
- `source/_data/providers.yml`: **核心数据文件**，管理所有的机场、VPN品牌数据。
- `source/CNAME`: 绑定的自定义域名 (`jichangbay.com`)。
- `scripts/go-redirects.js`: 自动生成安全跳转页的 Hexo 脚本。
- `themes/jichangbay/layout/index.ejs`: 网站唯一个核心 EJS 渲染模板。
- `themes/jichangbay/source/css/style.css`: 统一化原生层叠样式表。
- `themes/jichangbay/source/js/main.js`: 前端原生交互逻辑脚本。
- `.github/workflows/deploy.yml`: GitHub Actions CI/CD 自动化构建与部署流。

## 🚀 本地开发指南

### 1. 环境依赖
- Node.js (v18+)
- Git

### 2. 安装与运行

```bash
# 克隆仓库
git clone https://github.com/Colasaiko/jichangbay.com.git
cd jichangbay.com

# 安装依赖
npm install

# 启动本地开发服务器
npx hexo server
```
运行后，在浏览器中打开 `http://localhost:4000/` 即可实时预览并进行开发。

## 📦 内容管理 (修改数据)

本项目最大的特色在于**模板与数据分离**，更新网站时几乎不需要接触 HTML/EJS 代码。

**新增或修改品牌：**
1. 用文本编辑器打开 `source/_data/providers.yml`
2. 添加或修改品牌块（遵循现存 YAML 格式）：
```yaml
- name: 示例机场
  slug: example-vpn
  relationship: partner
  targetUrl: https://affiliate.example.com/register?code=XXXX  # 真实的购买链接
  affUrl: /go/example-vpn/  # 必须保持 /go/slug/ 这种隐匿格式
  coupon: 8888
  couponDiscount: 8折
  aiSupport: 支持 AI
  streamingSupport: 支持流媒体解锁
  clientSupport: 3-5台设备同时在线
  bestFor:
    - 低预算
    - 大流量
  features:
    - 海外中转，低延迟
    - 智能路由自动择优
  plans:
    - name: 基础月付
      traffic: 100 GB
      monthly: ¥10.00
      annual: ¥100.00
```
3. 保存后执行重新构建，首页**参数对比表**、**快速选购**区及**品牌详情**会**自动**抓取该品牌的“最低代表月付价”并无缝嵌入页面流中。

## ☁️ 部署与发布

项目自带 `.github/workflows/deploy.yml` 工作流，支持向 **GitHub Pages** 的零配置全自动部署。

1. **推送代码** 到 `main` 分支。
2. 前往 GitHub 仓库顶部，点击 **Settings -> Pages**。
3. 将 **Source** 设置为 **GitHub Actions**。
4. 在 **Custom domain** 中填入您的自定义域名（如 `jichangbay.com`），并确保 DNS CNAME 配置正确。

每次进行 `git push` 到 `main` 分支后，GitHub Actions 将会自动执行 Hexo 静态编译、自动 SEO 检测并将生成的 `public/` 静态文件推送到上线环境。

## 📄 特别声明

- 机场湾 (JichangBay) 站点内所有品牌数据及售价均根据服务商公开页面整理，仅供用户做信息参考。
- 本项目开源的网站前端代码、SEO 实践代码及 Link Cloaking 技术，仅供开发者用于静态建站技术交流与学习使用。

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/Colasaiko">Colasaiko</a> &middot; 2026</sub>
</div>
