# 🚀 Django Deployment + AWS S3 Setup Guide

This guide explains how to deploy a Django application on AWS EC2 using Gunicorn + Nginx and configure AWS S3 for media storage.

---

# 🧱 Architecture

User → Nginx → Gunicorn → Django → S3 (Media Storage)
↓
Database

---

# 🖥️ PART 1 — EC2 DEPLOYMENT

## 1. Launch EC2 Instance

* Ubuntu 22.04
* Open ports:

  * 22 (SSH)
  * 80 (HTTP)
  * 443 (HTTPS)

---

## 2. Connect to EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

---

## 3. Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx git -y
```

---

## 4. Clone Project

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

---

## 5. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 6. Configure Django Settings

Edit `settings.py`:

```python
DEBUG = False

ALLOWED_HOSTS = ["your-ec2-ip", "your-domain.com"]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

## 7. Run Migrations & Collect Static

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

---

## 8. Test Gunicorn

```bash
gunicorn --bind 0.0.0.0:8000 project_name.wsgi
```

Open:
http://your-ec2-ip:8000

---

## 9. Setup Gunicorn Service

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Paste:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/your-project
ExecStart=/home/ubuntu/your-project/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/ubuntu/your-project/gunicorn.sock \
          project_name.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

---

## 10. Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/project
```

Paste:

```nginx
server {
    listen 80;
    server_name your-ec2-ip;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/ubuntu/your-project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/your-project/gunicorn.sock;
    }
}
```

Enable:

```bash
sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

✅ Your app is now live:
http://your-ec2-ip

---

# ☁️ PART 2 — AWS S3 SETUP (MEDIA FILES)

## 1. Create S3 Bucket

* Go to AWS S3
* Create bucket: `your-project-media`
* Disable "Block Public Access"

---

## 2. Install Packages

```bash
pip install boto3 django-storages
```

---

## 3. Update Django Settings

```python
INSTALLED_APPS += ['storages']
```

Add:

```python
AWS_STORAGE_BUCKET_NAME = "your-project-media"
AWS_S3_REGION_NAME = "ap-south-1"

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
```

---

## 4. Use IAM Role (Recommended)

* Go to AWS IAM
* Create Role → EC2
* Attach policy: AmazonS3FullAccess
* Attach role to EC2 instance

⚠️ Do NOT use access keys in production

---

## 5. Test Upload

* Create a blog post
* Upload image
* Check in S3 bucket

---

# ⚠️ TROUBLESHOOTING

## Internal Server Error

```bash
sudo journalctl -u gunicorn -n 50
```

---

## Gunicorn Permission Issue

```bash
sudo chown -R ubuntu:www-data /home/ubuntu/your-project
```

---

## Images Not Showing

```python
MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
```

---

## S3 Access Denied

Bucket Policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::your-project-media/*"]
    }
  ]
}
```

---

# 🔒 OPTIONAL — HTTPS SETUP

Install Certbot:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

# ✅ FINAL CHECKLIST

* EC2 running
* Gunicorn active
* Nginx configured
* S3 working
* Images uploading
* Static files working

---
