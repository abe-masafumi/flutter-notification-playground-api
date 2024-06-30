# データベース設計

このプロジェクトのデータベース設計は以下の通りです。
```mermaid
erDiagram
    CUSTOMUSER {
        UUID id PK "default=uuid.uuid4, editable=False"
        string firebase_uid "max_length=255, unique=True"
        string role "max_length=10, choices=ROLES"
        string username "max_length=100"
        date birthday
    }
    MALEUSER {
        UUID user PK "OneToOneField(CustomUser, on_delete=models.CASCADE)"
        string address "max_length=255"
        text introduction "blank=True, null=True"
    }
    FEMALEUSER {
        UUID user PK "OneToOneField(CustomUser, on_delete=models.CASCADE)"
        text introduction "blank=True, null=True"
    }
    PROFILEIMAGE {
        UUID id PK "default=uuid.uuid4, editable=False"
        UUID user FK "ForeignKey(CustomUser, on_delete=models.CASCADE)"
        string image_url "URLField"
    }
    HOBBY {
        UUID id PK "default=uuid.uuid4, editable=False"
        string type "max_length=100"
        UUID user FK "ForeignKey(CustomUser, on_delete=models.CASCADE)"
    }
    APILOG {
        UUID id PK "default=uuid.uuid4, editable=False"
        string endpoint "max_length=255"
        datetime request_time "auto_now_add=True"
        string method "max_length=10"
        int status_code
        UUID user FK "ForeignKey(CustomUser, on_delete=models.CASCADE)"
    }
  CUSTOMUSER ||--o{ MALEUSER : "has"
  CUSTOMUSER ||--o{ FEMALEUSER : "has"
  MALEUSER ||--o{ PROFILEIMAGE : "has"
  FEMALEUSER ||--o{ PROFILEIMAGE : "has"
  MALEUSER ||--o{ HOBBY : "has"
```