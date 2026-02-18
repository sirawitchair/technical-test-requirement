<!-- @format -->

# Technical Test Requirement Testing 
## มีทั้งสองข้อใน project เดียว สามารถเทสได้ตามที่เขียนไว้เลย

## 1. Users Profile API

### How to Run

1. Copy environment file

```bash
cp .env.example .env
```

2. Run with Docker

```bash
docker-compose up
```

### API Testing

```bash
# swagger
localhost:8000/api/v1/docs/
```

## 2. SQL Testing

ตารางและข้อมูลทดสอบจะถูกสร้างอัตโนมัติเมื่อ run Docker ครั้งแรก (จากไฟล์ `init-db/01_init_tables.sql`)

### รันไฟล์ SQL

```bash
# sql-1.sql
docker compose exec db psql -U postgres -d users_profile_db -f /sql/sql-1.sql

# sql-2.sql
docker compose exec db psql -U postgres -d users_profile_db -f /sql/sql-2.sql

# sql-3.sql
docker compose exec db psql -U postgres -d users_profile_db -f /sql/sql-3.sql
```

### เข้า psql interactive mode

```bash
docker compose exec db psql -U postgres -d users_profile_db
```

### Reset Database (ลบข้อมูลเก่าและสร้างใหม่)

```bash
docker compose down -v
docker compose up -d
```
