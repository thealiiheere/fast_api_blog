from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas
from ..database import get_db
from ..utils.hashing import hash_password, verify_password
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# ─── CREATE USER ──────────────────────────────
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Email allaqachon borligini tekshirish
    existing = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bu email allaqachon ro'yxatdan o'tgan"
        )

    # Parolni xashlash
    hashed = hash_password(user.password)
    user.password = hashed

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# ─── JORIY FOYDALANUVCHI ──────────────────────
# Diqqat: "/me" yo'llari "/{user_id}" dan OLDIN turishi kerak,
# aks holda "me" user_id deb o'qiladi va 422 qaytadi
@router.get("/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(get_current_user)):
    return current_user

# ─── PAROL O'ZGARTIRISH ───────────────────────
@router.put("/me/password")
def change_password(
    passwords: schemas.PasswordChange,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if not verify_password(passwords.old_password, current_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Eski parol noto'g'ri"
        )

    current_user.password = hash_password(passwords.new_password)
    db.commit()

    return {"xabar": "Parol muvaffaqiyatli o'zgartirildi"}

# ─── GET USER ─────────────────────────────────
@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={user_id} bo'lgan foydalanuvchi topilmadi"
        )

    return user


# ─── READ ALL (qidiruv + pagination) ─────────
@router.get(
    "/",
    response_model=List[schemas.PostResponse]
)
def get_all_posts(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = ""
):
    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)
    ).limit(limit).offset(skip).all()

    return posts