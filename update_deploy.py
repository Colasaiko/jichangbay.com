import re

yml_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\.github\workflows\deploy.yml'
with open(yml_path, 'r', encoding='utf-8') as f:
    yml = f.read()

# Build step
build_old = """      - name: Build Hexo
        run: |
          npx hexo clean
          npx hexo generate"""

build_new = """      - name: Build Hexo
        run: |
          npx hexo clean
          npx hexo generate
          if [ -n "$INDEXNOW_KEY" ]; then
            echo "$INDEXNOW_KEY" > "public/${INDEXNOW_KEY}.txt"
          fi
        env:
          INDEXNOW_KEY: ${{ secrets.INDEXNOW_KEY }}"""

if 'if [ -n "$INDEXNOW_KEY" ]; then' not in yml:
    yml = yml.replace(build_old, build_new)

# Deploy step
deploy_old = """      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4"""

deploy_new = """      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4

      - name: Checkout for IndexNow
        uses: actions/checkout@v4

      - name: Setup Node.js for IndexNow
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Submit IndexNow
        run: node tools/submit-indexnow.js
        env:
          INDEXNOW_KEY: ${{ secrets.INDEXNOW_KEY }}"""

if 'Submit IndexNow' not in yml:
    yml = yml.replace(deploy_old, deploy_new)

with open(yml_path, 'w', encoding='utf-8') as f:
    f.write(yml)
