#!/bin/bash
# install.sh - One-click OpenClaw deployment on Linux
# Run as root or with sudo

set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root: sudo ./install.sh"
    exit 1
fi

echo "===================================="
echo " OpenClaw Deploy v1.0"
echo "===================================="
echo

# 1. Detect OS
echo "[1/6] Detecting system..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "  OS: $PRETTY_NAME"
else
    echo "  [ERROR] Cannot detect OS"
    exit 1
fi

# 2. Install dependencies
echo "[2/6] Installing dependencies..."
if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq
    apt-get install -y -qq nodejs npm nginx certbot python3-certbot-nginx
elif command -v yum >/dev/null 2>&1; then
    yum install -y nodejs npm nginx certbot python3-certbot-nginx
else
    echo "  [ERROR] Unsupported package manager"
    exit 1
fi

# 3. Install OpenClaw
echo "[3/6] Installing OpenClaw..."
npm install -g @openclaw/cli

# 4. Setup systemd
echo "[4/6] Setting up systemd service..."
cat > /etc/systemd/system/openclaw.service <<EOF
[Unit]
Description=OpenClaw AI Agent Service
After=network.target

[Service]
Type=simple
User=openclaw
WorkingDirectory=/opt/openclaw
ExecStart=/usr/bin/openclaw serve
Restart=always
RestartSec=10
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
EOF

# Create user and dirs
id openclaw >/dev/null 2>&1 || useradd -r -s /bin/false openclaw
mkdir -p /opt/openclaw /var/lib/openclaw
chown -R openclaw:openclaw /opt/openclaw /var/lib/openclaw

systemctl daemon-reload
systemctl enable openclaw
systemctl start openclaw

# 5. Configure nginx
echo "[5/6] Configuring nginx..."
cat > /etc/nginx/sites-available/openclaw.conf <<EOF
server {
    listen 80 default_server;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

ln -sf /etc/nginx/sites-available/openclaw.conf /etc/nginx/sites-enabled/openclaw.conf
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl reload nginx

# 6. SSL setup (optional)
echo "[6/6] SSL setup (optional)..."
read -p "Domain for SSL (leave empty to skip): " DOMAIN
read -p "Email for Let's Encrypt: " EMAIL

if [ -n "$DOMAIN" ]; then
    sed -i "s/server_name _;/server_name $DOMAIN;/" /etc/nginx/sites-available/openclaw.conf
    nginx -t && systemctl reload nginx
    certbot --nginx -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive
fi

# Generate default config
cat > /etc/openclaw/config.yaml <<EOF
server:
  port: 3000
  host: 127.0.0.1

auth:
  jwt_secret: $(openssl rand -hex 32)
  session_timeout: 86400

storage:
  type: sqlite
  path: /var/lib/openclaw/db.sqlite

proxy:
  api_base: https://api.skillai.top
  api_key: REPLACE_ME
EOF

mkdir -p /etc/openclaw
chown -R openclaw:openclaw /etc/openclaw

echo
echo "===================================="
echo " Done!"
echo "===================================="
echo
if [ -n "$DOMAIN" ]; then
    echo "Access: https://$DOMAIN"
else
    echo "Access: http://$(hostname -I | awk '{print $1}'):80"
fi
echo
echo "Next steps:"
echo "  1. Edit /etc/openclaw/config.yaml"
echo "  2. Restart: sudo systemctl restart openclaw"
echo "  3. Change default password"
echo