---
name: openclaw-deploy
description: One-click remote deployment for OpenClaw. Set up OpenClaw on any server (Linux/Mac/cloud) with one script. Includes systemd service, nginx reverse proxy, and SSL setup.
version: 1.0.0
author: fast118
license: MIT
applies_to: [openclaw]
---

# openclaw-deploy

> OpenClaw 一键远程部署
>
> 在任何服务器(本地 / 云) 5 分钟装好 OpenClaw,带 systemd + nginx + SSL

## 这是什么?

`openclaw-deploy` 是一个远程部署脚本,自动完成:

1. 安装 OpenClaw CLI
2. 配置 systemd 服务(开机自启 / 自动重启)
3. 配置 nginx 反向代理
4. 一键申请 Let's Encrypt SSL 证书
5. 配置防火墙规则

## 适用场景

- 自托管 OpenClaw 实例(不想用官方云)
- 内网部署给团队用
- 私人 AI 编程助手

## 系统要求

- Linux (Ubuntu 20.04+ / Debian 11+ / CentOS 8+)
- macOS(部分支持,无 systemd)
- 2GB+ RAM
- 公网 IP(可选,用于 SSL)

## 一键安装

SSH 登录服务器后:

```bash
curl -fsSL https://raw.githubusercontent.com/fast1188/ai-agent-skills/main/openclaw/openclaw-deploy/install.sh | bash
```

或下载手动:

```bash
git clone https://github.com/fast1188/ai-agent-skills
cd ai-agent-skills/openclaw/openclaw-deploy
chmod +x install.sh
./install.sh
```

## 安装过程

```
====================================
 OpenClaw Deploy v1.0
====================================

[1/6] 检测系统...
  OS: Ubuntu 22.04 LTS ✓

[2/6] 安装依赖...
  - nodejs (v20) ✓
  - nginx ✓
  - certbot ✓

[3/6] 安装 OpenClaw...
  - npm install -g @openclaw/cli ✓

[4/6] 配置 systemd 服务...
  - /etc/systemd/system/openclaw.service ✓
  - systemctl enable openclaw ✓
  - systemctl start openclaw ✓

[5/6] 配置 nginx 反向代理...
  - /etc/nginx/sites-available/openclaw.conf ✓
  - nginx -t ✓
  - systemctl reload nginx ✓

[6/6] 配置 SSL(Let's Encrypt)...
  - 域名: openclaw.example.com
  - 邮箱: admin@example.com
  - 证书申请... ✓

====================================
 完成!
====================================

访问: https://openclaw.example.com
默认账号: admin
默认密码: 请立即修改!
```

## 配置说明

`/etc/openclaw/config.yaml`:

```yaml
server:
  port: 3000
  host: 127.0.0.1

auth:
  jwt_secret: change-me-in-production
  session_timeout: 86400

storage:
  type: sqlite
  path: /var/lib/openclaw/db.sqlite

proxy:
  api_base: https://api.skillai.top  # 国内直连
  api_key: your-key-here
```

## systemd 服务管理

```bash
# 查看状态
sudo systemctl status openclaw

# 重启
sudo systemctl restart openclaw

# 查看日志
sudo journalctl -u openclaw -f

# 开机自启
sudo systemctl enable openclaw
```

## nginx 配置示例

```nginx
server {
    listen 80;
    server_name openclaw.example.com;
    
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 故障排查

### 服务起不来

```bash
sudo journalctl -u openclaw -n 50
```

### 502 Bad Gateway

```bash
# 检查 OpenClaw 是否在跑
sudo systemctl status openclaw
# 检查端口
sudo ss -tlnp | grep 3000
```

### SSL 证书问题

```bash
# 强制续期
sudo certbot renew --force-renewal
```

## 安全建议

部署后必须:

1. ✅ 改默认密码
2. ✅ 改 jwt_secret
3. ✅ 启用防火墙(只开 80/443/22)
4. ✅ 配置 fail2ban
5. ✅ 定期更新 `sudo apt update && sudo apt upgrade`
6. ✅ 配置自动备份

## 卸载

```bash
./uninstall.sh
```

会:
- 停止 systemd 服务
- 删除 nginx 配置
- 删除 OpenClaw 包
- **保留**数据库(你需要手动备份)

## 相关项目

- [free-ai-router](https://github.com/fast1188/free-ai-router)
- [ai-agent-skills](https://github.com/fast1188/ai-agent-skills)
- [api.skillai.top](https://api.skillai.top) - 国内直连 API

## 许可证

MIT