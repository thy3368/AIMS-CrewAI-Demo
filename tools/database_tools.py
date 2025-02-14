from langchain.tools import tool
import sqlite3
from typing import Dict, List, Any

class DatabaseTools:
    def __init__(self):
        self.db_path = "stock_data.db"
        self._init_db()

    def _init_db(self):
        """初始化数据库和表"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 创建股票数据表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
            symbol TEXT PRIMARY KEY,
            price REAL,
            volume INTEGER,
            date TEXT
        )
        ''')
        conn.commit()
        conn.close()

    @tool("Query Stock Data")
    def query_stock(symbol: str) -> Dict[str, Any]:
        """查询股票数据。输入股票代码，返回该股票的最新数据。"""
        conn = sqlite3.connect("stock_data.db")
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM stock_data WHERE symbol = ?", 
            (symbol,)
        )
        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                "symbol": result[0],
                "price": result[1],
                "volume": result[2],
                "date": result[3]
            }
        return {"error": "Stock not found"}

    @tool("Insert Stock Data")
    def insert_stock(data: Dict[str, Any]) -> str:
        """插入股票数据。输入格式: {"symbol": "AAPL", "price": 150.0, "volume": 1000000, "date": "2024-01-01"}"""
        conn = sqlite3.connect("stock_data.db")
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT OR REPLACE INTO stock_data (symbol, price, volume, date) VALUES (?, ?, ?, ?)",
                (data["symbol"], data["price"], data["volume"], data["date"])
            )
            conn.commit()
            return "Data inserted successfully"
        except Exception as e:
            return f"Error inserting data: {str(e)}"
        finally:
            conn.close()