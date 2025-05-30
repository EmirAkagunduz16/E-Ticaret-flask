from config.mysql_db import get_mysql_connection
from config.mongodb_db import get_db

def init_tables():
    """Veritabanı tablolarını başlat"""
    print("Veritabanı tabloları başlatılıyor...")
    
    # MySQL tablolarını başlat
    conn = get_mysql_connection()
    if not conn:
        print("MySQL veritabanına bağlanılamadı")
        return False
    
    cursor = conn.cursor()
    
    # Users tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(20) NOT NULL DEFAULT 'customer',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login DATETIME NULL,
        reset_token VARCHAR(100),
        reset_token_expires DATETIME
    )
    ''')
    
    
    conn.commit()
    cursor.close()
    conn.close()
    
    # MongoDB toplamlarını başlat
    db = get_db()
    
    # MongoDB toplamlarını başlat
    if 'products' not in db.list_collection_names():
        db.create_collection('products')
        db.products.create_index('supplier_id')
        db.products.create_index('name')
    
    if 'carts' not in db.list_collection_names():
        db.create_collection('carts')
        db.carts.create_index('user_id')
        db.carts.create_index('product_id')
    
    print("Veritabanı tabloları başarıyla başlatıldı!")
    return True 