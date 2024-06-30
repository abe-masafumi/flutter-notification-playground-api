# API Documentation

## エンドポイント一覧

- **<新規登録>**
**POST /user/：新しいユーザーオブジェクトを作成**

**<ユーザー情報編集>**
PUT /maleuser/{id}/：introductionを更新
PATCH /maleuser/{id}/：introductionを更新

**<趣味を追加>**
POST /hobby/：新しい趣味オブジェクトを作成

**<ユーザー情報詳細取得>**
GET /maleuser/{id}/：特定のオブジェクトの詳細を取得

**<趣味を削除>**
DELETE /hobby/{id}/：趣味オブジェクトを削除

**<ユーザーを削除>**
DELETE /maleuser/{id}/：オブジェクトを削除
